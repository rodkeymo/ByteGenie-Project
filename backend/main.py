from flask import Flask, request, jsonify
import json
from gradientai import Gradient
from flask_cors import CORS
import os
import sqlite3

os.environ['GRADIENT_ACCESS_TOKEN'] = "csHNcQXaMC90iFMMpWG2I3YGMsWQ7Aon"
os.environ['GRADIENT_WORKSPACE_ID'] = "ad9c8d41-700b-4b30-af7c-6e24098ddb6d_workspace"



app = Flask(__name__)

CORS(app)

DATABASE_FILE = './data/database.db'
MODEL_ADAPTER_ID_FILE = 'model_adapter_id.json'




def query_database(query):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def save_model_adapter_id(model_adapter_id):
    with open(MODEL_ADAPTER_ID_FILE, 'w') as f:
        json.dump({"model_adapter_id": model_adapter_id}, f)

def load_model_adapter_id():
    try:
        with open(MODEL_ADAPTER_ID_FILE, 'r') as f:
            data = json.load(f)
            return data["model_adapter_id"]
    except (FileNotFoundError, KeyError):
        return None

def get_model_adapter():
    model_adapter_id = load_model_adapter_id()
    with Gradient() as gradient:
        if model_adapter_id:
            print(f"Loading existing model adapter with id {model_adapter_id}")
            return gradient.get_model_adapter(model_adapter_id=model_adapter_id)
        else:
            base_model = gradient.get_base_model(base_model_slug="nous-hermes2")
            new_model_adapter = base_model.create_model_adapter(name="test model 3")
            print(f"Created new model adapter with id {new_model_adapter.id}")
            save_model_adapter_id(new_model_adapter.id)
            return new_model_adapter

@app.route('/fine_tune', methods=['POST'])
def fine_tune():
    data = request.json
    if not data or 'samples' not in data:
        return jsonify({"error": "No samples provided"}), 400

    samples = data['samples']
    new_model_adapter = get_model_adapter()    
    new_model_adapter.fine_tune(samples=samples)
    print(f"Fine-tuned model adapter with id {new_model_adapter.id}")

    return jsonify({"message": "Model fine-tuned successfully"})




@app.route('/predict', methods=['POST'])
def generate_response():
    data = request.json

    print(data)
    if not data or 'userInput' not in data:
        return jsonify({"error": "No query provided"}), 400

    sample_query = data['userInput']
    new_model_adapter = get_model_adapter()

    generated_query = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
    print(f"Generated response: {generated_query}")

    try:
        query_result = query_database(generated_query)
        print(f"Query result: {query_result}")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    natural_language_response = format_query_result_to_natural_language(query_result)

    return jsonify({
        "generated_query": generated_query,
        "query_result": query_result,
        "natural_language_response": natural_language_response
    })


def format_query_result_to_natural_language(query_result):
    if not query_result:
        return "No results found."
    
    # Convert the query result into a string format
    result_str = "\n".join([", ".join([str(item) for item in row]) for row in query_result])

    # Use the original base model to generate a natural language response
    with Gradient() as gradient:
        base_model = gradient.get_base_model(base_model_slug="nous-hermes2")
        response = base_model.complete(query=f"### Instruction: Convert the following query result into natural language.\n\n### Query Result:\n{result_str}\n\n### Response:", max_generated_token_count=500).generated_output
        return response

if __name__ == '__main__':
    app.run(debug=True)

# BYTEGENIE AI TEST APPLICATION

Welcome to the BYTEGENIE AI TEST APPLICATION project! This README serves as a comprehensive guide to the key aspects of this project.

# Table Of Contents
<!-- TOC -->
* [Introduction](#introduction)
* [Getting started](#getting-started)
  * [Installation](#installation)
    * [API's](#apis-)
  * [Motivation for Data Engineering/Processing](#Motivation-for-Data-Engineering/Processing)
  * [Main Functionalities of the API](#Main-Functionalities-of-the-API)
  * [Key Challenges(API)](#Key-Challenges(API))
  * [Future Improvements(API)](#Future-Improvements(API))
  * [Key Functionalities of the React UI](#Key-Functionalities-React)
  * [Challenges Faced(React)](#Challenges-Faced-React)
  * [Future Improvements(React)](#Future-Improvements(React))
  * [SQLite Database Challenges Faced](#SQLite-Database-Challenges-Faced)
  * [Future Improvements of Database](#Future-Improvements-of-Database)
  
<!-- TOC -->

# Introduction

BYTEGENIE AI TEST APPLICATION is aN AI powered chat application that utilises the fine-tuned LLM of Nous-Hermes-Llama-2-13B. 
A user is be able to interact with the application in the form of natural language, quering datasets including events, people and companies that are specific tot he fine-tuned LLM. 
The trained LLM provides SQL queries which in turn query the sqllite database and returns the output in natural language format to the user.


# Getting started

Follow the instructions below to get the project running locally.

## installation

### prerequisites

- **npm**
- **python**

Clone this repository.


## Running the backend
```bash 
cd backend
``` 
### Recreate Virtual Environment
```bash 
# Using venv (Python 3.x)
python3 -m venv venv

# Using virtualenv
virtualenv venv

``` 
### activate virtual env

```bash
source venv/Scripts/activate
```
### install dependencies
```bash
pip install -r requirements.txt

```
### Run the application
```bash
python main.py
```


### Running the frontend
```bash 
cd frontend
```

### Install dependencies
```bash
npm install
```

### Run the frontend app
```bash
npm start
```

## API's 

You can navigate to `http://127.0.0.1:5000/predict`. 
This Api is responsibe for making a 'POST' request from the frontend to the backend application to get user data queries. It returns a response with a `200` for a valid request, `400` for a bad request and `500` for an internal server error

You can navigate to `http://127.0.0.1:5000/fine_tune`. 
This api is responsible for training the LLM model based on specific data. Training of the model can be done more by making a `POST` request to the api with json structure:
```json
{
  "samples" : [  
  {
    "inputs": "### Instruction: List the names of startups participating in marketing events. \n\n### Response:\nSELECT company_name FROM company WHERE company_type='Startup' AND event_url IN (SELECT event_url FROM event WHERE company_industry LIKE '%Marketing%');"
  }
  ]
}
```

## Motivation for Data Engineering/Processing

Before making data available through the API, several data engineering and processing steps were undertaken:

1. **Data Cleaning**: Raw data obtained from external sources, such as databases or APIs, often requires cleaning to remove inconsistencies, duplicates, or errors.
   
2. **Data Transformation**: Data might need to be transformed into a format suitable for storage and efficient retrieval. This includes structuring data into relational tables or other suitable formats.
   
3. **Data Integration**: Combining data from multiple sources into a unified format to provide comprehensive responses to API queries.
   

## Main Functionalities of the API

The API provides the following main functionalities:

**Prediction and Processing**: Endpoint (`/predict`) for processing user queries or requests, such as natural language processing, data retrieval, or predictive modeling.

   Example usage:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"query": "example query"}' http://localhost:5000/predict

```
## Key Challenges(API)

### Challenges Faced

1. **Data Consistency**: Ensuring data consistency across different data sources and versions.
   
2. **Performance Optimization**: Optimizing API response times, especially with large datasets or complex queries.
      
4. **Scalability**: Designing the application to handle increasing volumes of requests and data without compromising performance.



## Future Improvements(API)

Given more time, several improvements could enhance the backend application:

1. **Enhanced Query Optimization**: Implementing advanced query optimization techniques to improve response times and efficiency.
   
2. **Integration of advanced Machine Learning Models**: Incorporating advanced machine learning models for predictive analytics or personalized responses based on user data.
   
3. **Real-time Data Processing**: Implementing real-time data processing capabilities to handle streaming data and provide up-to-date responses.
   



   ## Key Functionalities of the React UI

The frontend application includes the following key functionalities:
  
- **Data Display**: Presentation of data retrieved from the backend API, such as company information, event details, etc.
  
- **Interaction**: User-friendly interfaces for submitting queries, viewing results, and navigating through application features.

## API Endpoints Used

The frontend interacts with the following API endpoints from the backend:

- **POST `/predict`**: Endpoint for making predictions or processing requests.


## Challenges Faced(React)

### Challenges in Building the Frontend

1. **Data Integration**: Displaying complex data structures from API responses in a user-friendly manner.
   
2. **State Management**: Efficiently managing application state and ensuring data consistency across components.
      
4. **Performance Optimization**: Optimizing frontend performance, especially with data-heavy operations and rendering.

## Future Improvements(React)

### Improvements for the Frontend Application

1. **UI/UX Enhancements**: Improving user interface design for better usability and accessibility. This would include authentification and session logging to save user history from search.
  
2. **Performance Optimization**: Implementing caching strategies, lazy loading, or pagination to improve loading times and responsiveness.
  
3. **Error Handling**: Enhancing error handling mechanisms to provide informative error messages and better user feedback.
  
4. **Integration Testing**: Implementing comprehensive integration testing to ensure smooth interaction with backend APIs and components.
  
5. **Enhanced State Management**: Implementing state management solutions like Redux or Context API for better scalability and maintainability.




##  SQLite Database Challenges Faced

### Challenges in Working with This Data


   
1. **Schema Design**: Designing an efficient schema that accommodates the application's requirements and optimizes query performance.
   
2. **Scaling Limitations**: Addressing potential scaling limitations of SQLite, especially with larger datasets or high concurrency requirements.
   
3. **Data Validation**: Ensuring accurate data entry and validation to prevent errors and maintain data quality over time.


## Future Improvements of Database

1. **Normalization**: Further normalizing the database schema to reduce redundancy and improve data integrity.
  
2. **Indexes**: Implementing appropriate indexes on frequently queried columns to enhance query performance.
  
3. **Partitioning**: Considering table partitioning strategies to manage large datasets more efficiently.
  
4. **Backup and Recovery**: Establishing robust backup and recovery procedures to safeguard data against potential loss or corruption.
  
5. **Concurrency Control**: Implementing effective concurrency control mechanisms to handle multiple simultaneous transactions.

import React,{useState,useEffect} from 'react';
import './styles/ChatSection.css';
import send from './send.svg';
import { Input } from 'dracula-ui'
import { useNavigate } from 'react-router-dom';
import 'react-awesome-button/dist/styles.css';
import './customButtonStyles.scss';
import AwesomeButtonStyles from 'react-awesome-button/src/styles/styles.scss';
import Loader from './Loader';
import './customButtonStyles.scss'
import '../App.css';
import {
    AwesomeButton,
  } from 'react-awesome-button';
import axios from 'axios'


const ChatSection = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [messages, setMessages] = useState([]);
    const [userInput, setUserInput] = useState('');
    const [disabled,setDisabled]=useState(false);
       
   
   
   
   
   
   
    const handleSend = async () => {
        if(disabled){
            return ;
        }
        setUserInput('');
        const currentTime = new Intl.DateTimeFormat('default', {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true
        }).format(new Date()); // Client's local time
        if(userInput === '') return;
        setMessages([...messages,
        {text: userInput, timestamp: currentTime }
        ]);
        setIsLoading(true);
        setDisabled(true)

        const data=await sendMessage();
        
        setIsLoading(false);
        if(data){
           setMessages(prevMessages => [...prevMessages,
               { type: 'bot', text: data, timestamp:currentTime }
           ]);
        }
        else{
            setMessages(prevMessages => [...prevMessages,
                { type: 'bot', text: "Some Error Occurred", timestamp: currentTime }
            ]);
        }

        setDisabled(false)
          
    }
    const sendMessage = async () => {
        try {
            const response = await axios.post('http://localhost:5000/predict', { userInput });
            // setResponse(response.data.natural_language_response);
            
            console.log(response.data.natural_language_response);

            const data = response.data.natural_language_response;

            return data;

          } catch (error) {
                console.log('An error occured',error);
          }
    }
    
    return (
        <div> 

            <section style={{ height: '100vh !important' }}>
                <div className="container py-5" >

                    <div style={{ height: "100vh" }} className="row d-flex justify-content-center">
                        <div className="col-md-10 col-lg-8 col-xl-6">

                            <div className="card" style={{borderRadius:'20px'}} id="chat2">
                                <span style={{display: 'flex', justifyContent: 'center', alignItems: 'center',marginTop:'20px',textAlign:'center',color:'blue'}}>ByteGenie Project Test</span>
                                <div  className="card-body" data-mdb-perfect-scrollbar="true" style={{height: "600px", overflow: "scroll" }}>
                                   
                                    {messages.map((message, index) => (
                                        <div key={index} style={{ position: "relative"}}  className={`d-flex flex-row ${message.type === 'user' ? 'justify-content-end' : 'justify-content-start'}`}>
                                           { message.type==='user'?<></>:
                                            <img  src="https://media.istockphoto.com/id/1010001882/vector/%C3%B0%C3%B0%C2%B5%C3%B1%C3%B0%C3%B1%C3%B1.jpg?s=612x612&w=0&k=20&c=1jeAr9KSx3sG7SKxUPR_j8WPSZq_NIKL0P-MA4F1xRw="
                                            alt="avatar 1" style={{ marginTop:"-5px",width: "45px", height: "100%" }} />
                                            }
                                            <p style={{ position:"relative",minWidth:'90px',minHeight:"50px",backgroundColor:`${message.type==='bot'?"#f5f6f7":"#FAE4CB"}`,fontWeight:"500"}} className={`small p-2 ${message.type === 'user' ? 'me-3' : 'ms-1'} rounded-3`}>
                                              {message.text}
                                              
                                              <small style={{position:"absolute",bottom:'0%',right:'5%',fontSize:'10px',marginTop:'10px'}} className="text-muted"> {message.timestamp}</small>
                                            </p>
                                           
                                        </div>
                                    ))}
                                    {isLoading && <Loader />}
                                </div>
                                <div id="move" style={{background:"#F5F5F7",borderTop:"none",borderBottomLeftRadius:'40px',borderBottomRightRadius:"40px"}} className="card-footer text-muted d-flex justify-content-center align-items-center p-6">
                                <Input color="white" size="lg" placeholder="Ask Away..." m="xs" style={{fontWeight:"500",backgroundColor:"#F1F1F1",width:"90%",marginRight:'10px'}} value={userInput} className="form-control form-control-lg" onChange={(e) => {
                                        setUserInput(e.target.value) }}/>
                                <span onClick={()=>{
                                    handleSend();
                                }}>
                                    <AwesomeButton disabled={disabled}  cssModule={AwesomeButtonStyles} type="primary"><img src={send} alt="Send Icon" /></AwesomeButton>
                                </span>                                   
                                </div>
                            </div>

                        </div>
                    </div>

                </div>
            </section>
             
        </div>
    );
}


export default ChatSection;




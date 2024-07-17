import './App.css';
import ChatSection from './components/ChatSection';
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
  return (
    <BrowserRouter>
    <Routes>
        <Route exact path="/" element={<ChatSection />} />
       </Routes>
  </BrowserRouter>
  );
}

export default App;

import Routes from "./router"
import "react-toastify/dist/ReactToastify.css"
import { ToastContainer } from "react-toastify";

export default function App(){
  return(
    <div>
      <Routes/>
      <ToastContainer autoClose={3000}/>
    </div>
  );

};
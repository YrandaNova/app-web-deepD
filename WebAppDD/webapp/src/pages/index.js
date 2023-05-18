import Image from 'next/image'
import { Inter } from 'next/font/google'
import Container from 'react-bootstrap/Container';
import { useState } from 'react';

export default function Home() {

  const [email, setEmail]=useState("")
 // const [currentDate, setCurrentDate] = useState(new Date().toLocaleDateString());
  const [file, setFile]= useState("")
  const[logo, setLogo]=useState("")
  
  
const formData=new FormData();
formData.append('email', email);
//formData.append('currentDate', currentDate);
formData.append('file', file);
formData.append('logo', logo)




  const handleSubmit= async (event)=>{
      event.preventDefault();
      
      
      try{
        alert("file sent")
        const res = await fetch ("https://api.yranda.com/submit-form",{
        //const res = await fetch ("http://localhost:3001/submit-form",{
        method:"POST",
         body: formData
        
  
      });

      }catch (error){
        alert("error")
        console.error(error);
      }
  };

  const handleFileChange=(event)=>{

      setFile(event.target.files[0]);

      console.log("tengo el archivo")
  }  



  return (
    <>
     
      <div className=' flex h-screen items-center justify-center '>
        <form onSubmit={handleSubmit} className='border border-solid rounded-md bg-stone-950 text-slate-50'>
          <label className='text-2xl my-5 flex justify-center'>
            Mail   
          </label>
          <input type="text" id ='email'  value={email} onChange={(event)=>setEmail(event.target.value)} className=' text-2xl border-2  mx-10 px-10 rounded-md border-stone-950 border-solid text-slate-950'/>
       
          <div className='my-5 flex justify-center '>
            <label className='text-2xl  flex'>
              watermark text: 
            </label>
               
          </div>
          <input type='text' id='logo'   value={logo} onChange={(event)=>setLogo(event.target.value)}  className=' text-2xl border-2  mx-10 px-10 rounded-md border-stone-950 border-solid text-slate-950' ></input> 

          <div className='my-5 flex '>
            <label></label>
            <input type='file'accept='pdf'  onChange={handleFileChange} className='ms-5'></input>
          </div>


          <div className='my-2 flex  justify-center'>

          <button type="submit" className='text-2xl p-2 px-4 bg-sky-500 hover:bg-sky-700 rounded-md  '>Submit</button>
          </div>
        </form>
      </div>
    </>
  )
}
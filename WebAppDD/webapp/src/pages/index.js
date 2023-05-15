import Image from 'next/image'
import { Inter } from 'next/font/google'
import Container from 'react-bootstrap/Container';
import { useState } from 'react';

export default function Home() {

  const [email, setEmail]=useState("")
  const currentDate = new Date();
  const [file, setfile]= useState(null)
  

  const handleSubmit=(event)=>{
      console.log("email", email, currentDate)
      alert("email", email)

  }

  const handleFileChange=(event)=>{
      console.log("tengo el archivo")
  }  



  return (
    <>
     
      <div className=' flex h-screen items-center justify-center'>
        <form onSubmit={handleSubmit}>
          <label className='text-2xl'>
            Mail 
            <input type="text" id ='email'  value={email} onChange={(event)=>setEmail(event.target.value)} className=' text-2xl border-2  mx-5 px-10 rounded-md border-stone-950 border-solid border-3'/>
          </label>
          <div className='my-5 flex '>
            <label></label>
            <input type='file'accept='pdf' onChange={handleFileChange}></input>
          </div>
          <div className='my-7 flex  justify-center'>

          <button type="submit" className='text-2xl p-2 px-4 bg-sky-500 hover:bg-sky-700 rounded-md '>Submit</button>
          </div>
        </form>
      </div>
    </>
  )
}
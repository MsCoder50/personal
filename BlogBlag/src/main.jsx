import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './index.css'
import Signup from './Signup.jsx';
import Blogs from './Blogs.jsx';
import Blog from './Blog.jsx';
import Create from './Create.jsx';
import Profile from './Profile.jsx';
import Edit from './Edit.jsx'
ReactDOM.createRoot(document.getElementById('root')).render(
  
    <BrowserRouter>
    <Routes>
      <Route index element= {<App />}></Route>
      <Route path="Signup" element= {<Signup />}></Route>
      <Route path="Blogs" element= {<Blogs />}></Route>
      <Route path="Blog" element= {<Blog />}></Route>
      <Route path="Create" element= {<Create />}></Route>
      <Route path="Profile" element= {<Profile />}></Route>
      <Route path="Edit" element= {<Edit />}></Route>
    </Routes>
    
    
    </BrowserRouter>
)

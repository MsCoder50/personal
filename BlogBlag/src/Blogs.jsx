import React, { useEffect, useState } from 'react';
import Navbar from './components/Navbar';
import Card from './components/Card';

const Blogs = () => {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const response = await fetch('http://127.0.0.1:4000/Blog');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setBlogs(data);
      } catch (error) {
        console.error('Error fetching blogs:', error);
      }
    };

    fetchBlogs();
  }, []);

  return (
    <div className='flex flex-col w-[100vw] h-[100vh] overflow-x-hidden'>
      <Navbar />
      <div className="p-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-10">
        {blogs.map(blog => (
          <Card 
            key={blog.UID} 
            image={blog.Image} 
            title={blog.Title} 
            content={blog.Content} 
          />
        ))}
      </div>
    </div>
  );
};

export default Blogs;

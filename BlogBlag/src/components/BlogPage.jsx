import React, { useEffect, useState } from 'react';
import Card from './Card';
import './index.css'; // Ensure you have the necessary CSS

const BlogPage = () => {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const response = await fetch('http://127.0.0.1:4000/blogs');
        const data = await response.json();
        setBlogs(data);
      } catch (error) {
        console.error('Failed to fetch blogs', error);
      }
    };

    fetchBlogs();
  }, []);

  return (
    <div className="blogs-container">
      {blogs.map((blog) => (
        <Card key={blog.UID} blog={blog} />
      ))}
    </div>
  );
};

export default BlogPage;

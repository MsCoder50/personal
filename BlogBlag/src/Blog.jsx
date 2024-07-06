import React, { useEffect, useState } from 'react';
import Navbar from './components/Navbar';
import { useLocation } from 'react-router-dom';
import Footer from './components/Footer';

const Blog = () => {
  const [blog, setBlog] = useState(null);
  const location = useLocation();

  useEffect(() => {
    const queryParams = new URLSearchParams(location.search);
    const imageName = queryParams.get('image');

    const fetchBlog = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:4000/Blog?image=${imageName}`);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setBlog(data);
      } catch (error) {
        console.error('Error fetching blog:', error);
      }
    };

    if (imageName) {
      fetchBlog();
    }
  }, [location]);

  if (!blog) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  return (
    <div className="bg-white font-sans leading-normal tracking-normal min-h-screen">
      <Navbar />

      {/* Hero Section */}
      <section className="w-full h-96 bg-cover bg-center" style={{ backgroundImage: `url('${blog.Image}')` }}>
        <div className="flex items-center justify-center w-full h-full bg-black bg-opacity-50">
          <h1 className="text-white text-4xl font-bold">{blog.Title}</h1>
        </div>
      </section>

      {/* Blog Content */}
      <section className="max-w-4xl mx-auto mt-10 px-6">
        <div className="py-12">
          <h2 className="text-3xl font-semibold text-gray-800">{blog.Title}</h2>
          <p className="mt-4 text-gray-700">{blog.Content}</p>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default Blog;

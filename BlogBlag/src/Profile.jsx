import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom'; // Import useLocation and useNavigate
import Navbar from './components/Navbar';
import Footer from './components/Footer';

const Profile = () => {
  const [blogs, setBlogs] = useState([]);
  const UID = sessionStorage.getItem('UID');
  const location = useLocation(); // useLocation hook
  const navigate = useNavigate(); // useNavigate hook

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:4000/Blogs/${UID}`);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setBlogs(data);
      } catch (error) {
        console.error('Error fetching blogs:', error.message);
        // Handle error state or show user-friendly message
      }
    };

    if (UID) {
      fetchBlogs();
    }
  }, [UID]);

  const handleDeleteBlog = async (imgname) => {
    const confirmDelete = window.confirm('Are you sure you want to delete this blog?');
    if (!confirmDelete) {
      return; // Cancel deletion if user cancels confirmation
    }
    
    try {
      const response = await fetch('http://127.0.0.1:4000/deleteBlog', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ imgname }),
      });
  
      if (response.ok) {
        console.log('Blog deleted successfully');
        // Update state or refresh blogs list after successful deletion
        const updatedBlogs = blogs.filter(blog => blog.Image !== imgname);
        setBlogs(updatedBlogs);
      } else {
        console.error('Failed to delete blog:', response.status);
        // Handle error response
      }
    } catch (error) {
      console.error('Error deleting blog:', error);
      // Handle network error
    }
  };
  
  const handleEditBlog = (imgname) => {
    navigate(`/Edit?imgname=${encodeURIComponent(imgname)}`);
  };

  return (
    <div>
      <Navbar />
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-center mb-8">Your Blogs</h1>
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {blogs.map(blog => (
            <div key={blog.Image} className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
              <a href="#">
                <img className="rounded-t-lg" src={`${blog.Image}`} alt={blog.Title} />
              </a>
              <div className="p-5">
                <a href="#">
                  <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{blog.Title}</h5>
                </a>
                {blog.Content ? (
                  <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">{blog.Content.slice(0, 50)}...</p>
                ) : (
                  <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">No content available</p>
                )}
                <div className="flex justify-between items-center">
                  <button
                    onClick={() => handleEditBlog(blog.Image)}
                    className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => handleDeleteBlog(blog.Image)}
                    className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-red-700 rounded-lg hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Profile;

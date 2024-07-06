import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

const Edit = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [image, setImage] = useState(null);
  const queryParams = new URLSearchParams(location.search);
  const imagePath = queryParams.get('imgname');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:4000/fetchBlog/${encodeURIComponent(imagePath)}`);
        if (!response.ok) {
          console.log(imagePath);
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        var data = await response.json();
        data = data[0];
        setTitle(data.Title);
        setContent(data.Content);
        setCategory(data.Category);
      } catch (error) {
        console.error('Error fetching blog:', error.message);
      }
    };

    fetchData();
  }, [imagePath]);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('imagePath', imagePath);
    formData.append('title', title);
    formData.append('content', content);
    formData.append('category', category);
    if (image) {
      formData.append('image', image);
    }

    try {
      const response = await fetch('http://127.0.0.1:4000/editBlog', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const result = await response.json();
      alert("Blog Updated Successfully")
      window.location.href = "/blogs";
      console.log('Blog updated successfully:', result);
    } catch (error) {
      console.error('Error updating blog:', error.message);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      <div className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-center mb-8">Edit Blog</h1>
        <form className="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-md" onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="image" className="block text-gray-700 font-bold mb-2">Image</label>
            <input type="file" id="image" name="image" className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500" onChange={handleImageChange} />
          </div>
          <div className="mb-4">
            <label htmlFor="title" className="block text-gray-700 font-bold mb-2">Blog Title</label>
            <input type="text" id="title" name="title" value={title} onChange={(e) => setTitle(e.target.value)} className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500" required />
          </div>
          <div className="mb-4">
            <label htmlFor="content" className="block text-gray-700 font-bold mb-2">Blog Content</label>
            <textarea id="content" name="content" rows="5" value={content} onChange={(e) => setContent(e.target.value)} className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500" required></textarea>
          </div>
          <div className="mb-4">
            <label htmlFor="category" className="block text-gray-700 font-bold mb-2">Blog Category</label>
            <input type="text" id="category" name="category" value={category} onChange={(e) => setCategory(e.target.value)} className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500" required />
          </div>
          <div className="text-center">
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Update Blog</button>
          </div>
        </form>
      </div>
      <Footer />
    </div>
  );
};

export default Edit;

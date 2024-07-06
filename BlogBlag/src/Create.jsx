import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

const Create = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [image, setImage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Check if all fields are filled
    if (!title || !content || !category || !image) {
      alert('Please fill in all fields');
      return;
    }

    // Validate file type
    const allowedTypes = ['image/png', 'image/jpeg', 'image/jpg', 'image/svg+xml', 'image/gif'];
    if (!allowedTypes.includes(image.type)) {
      alert('Only PNG, JPEG, JPG, SVG, and GIF files are allowed');
      return;
    }

    const formData = new FormData();
    formData.append('uid', sessionStorage.getItem('UID')); // Get UID from session storage
    formData.append('title', title);
    formData.append('content', content);
    formData.append('category', category);
    formData.append('image', image);

    try {
      const response = await fetch('http://127.0.0.1:4000/create', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        alert('Blog created successfully');
        // Reset form fields
        setTitle('');
        setContent('');
        setCategory('');
        setImage(null);
        // Redirect to Blogs route programmatically
        window.location.href = '/Blogs';
      } else {
        console.error('Failed to create blog:', response.status);
        alert('Failed to create blog');
        // Handle error response
      }
    } catch (error) {
      console.error('Error creating blog:', error);
      alert('Error creating blog. Please try again.');
      // Handle network error
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      <div className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-center mb-8">Create a New Blog</h1>
        <form className="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-md" onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="image" className="block text-gray-700 font-bold mb-2">Image</label>
            <input type="file" id="image" name="image" onChange={handleFileChange} accept=".png, .jpg, .jpeg, .svg, .gif" className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500" required />
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
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Create Blog</button>
          </div>
        </form>
      </div>
      <Footer />
    </div>
  );
};

export default Create;

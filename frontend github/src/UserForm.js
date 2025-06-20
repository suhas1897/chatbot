import React, { useState } from 'react';
import axios from 'axios';

export default function UserForm() {
  const [formData, setFormData] = useState({ name: '', email: '', contact: '' });
  const [message, setMessage] = useState('');

  const handleChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/create-user', formData);
      setMessage(res.data.message);
    } catch (err) {
      setMessage(err.response?.data?.error || 'Error registering user.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Register New User</h3>
      <input name="name" placeholder="Full Name" onChange={handleChange} />
      <input name="email" placeholder="Email" onChange={handleChange} />
      <input name="contact" placeholder="Contact Number" onChange={handleChange} />
      <button type="submit">Register</button>
      <p>{message}</p>
    </form>
  );
}

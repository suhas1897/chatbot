import axios from 'axios';

export const sendMessage = async (message, context) => {
  try {
    const response = await axios.post('http://localhost:8000/api/chat', { message, context });
    return response.data;
  } catch (error) {
    console.error('API error:', error);
    return { response: 'Sorry, something went wrong.', context: {} };
  }
};
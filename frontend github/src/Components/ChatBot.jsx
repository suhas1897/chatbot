import { useState, useEffect, useRef } from 'react';
import ChatMessages from './ChatMessages';
import ChatInput from './ChatInput';
import { sendMessage } from '../api';
import './Chatbot.css';

const Chatbot = () => {
  const [messages, setMessages] = useState([
    {
      text: 'Welcome to the Medical Chatbot! How can I assist you today?',
      isBot: true,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    },
  ]);
  const [context, setContext] = useState({});
  const [typing, setTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const handleSend = async (input) => {
    if (!input.trim()) return;

    const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    const userMessage = { text: input, isBot: false, timestamp };
    setMessages((prev) => [...prev, userMessage]);
    setTyping(true);

    const { response, context: newContext } = await sendMessage(input, context);
    const botTimestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const botMessage = { text: response, isBot: true, timestamp: botTimestamp };
    setMessages((prev) => [...prev, botMessage]);
    setContext(newContext);
    setTyping(false);
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, typing]);

  return (
    <div className="chat-container">
      <div className="chat-header">Medical Chatbot</div>
      <ChatMessages messages={messages} typing={typing} />
      <ChatInput onSend={handleSend} />
      <div ref={messagesEndRef} />
    </div>
  );
};

export default Chatbot;

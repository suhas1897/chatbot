Medical & Pharmacy AI Chatbot 🤖💊
Welcome to the Medical & Pharmacy AI Chatbot! This project is a full-stack application built to assist users with medical queries, appointment booking, and medicine ordering. Powered by FastAPI, MongoDB, React.js, and Ollama (phi3 model), it runs locally on your Windows machine (D:\medical chat bot) and provides a seamless user experience. 🚀
✨ Features

General Medical Queries ❓: Ask questions like "What are flu symptoms?" and get accurate responses from the phi3 model.
Appointment Booking 📅: Book appointments by providing patient name, date, time, and address.
Medicine Ordering 💊: Order medicines with a comma-separated list (e.g., "Paracetamol 10, Ibuprofen 5"), followed by name and address.
Context Persistence 🔄: Fixed empty context ({}) issues to ensure smooth appointment and medicine ordering flows.
Local LLM 🧠: Uses Ollama’s phi3 model, avoiding API keys and ensuring privacy.

🏗️ Project Structure

Backend (backend/): FastAPI server, MongoDB integration, and Ollama for LLM processing.
Frontend (frontend/): React.js client running on Vite (port 5173).

🛠️ Prerequisites

Windows 🖥️: Tested on Windows 10/11.
Python 3.8+ 🐍: For the backend.
Node.js 18+ 🚀: For the frontend.
MongoDB 🗄️: Local MongoDB server or Atlas.
Ollama 🤖: For running the phi3 model locally.

🚀 Setup Instructions
1. Clone the Repository 📦
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot

2. Install MongoDB 🗄️

Download MongoDB Community Server from mongodb.com.
Install and start MongoDB:mongod


Verify:mongo --host localhost --port 27017
show databases



3. Install Ollama 🤖

Download Ollama for Windows from ollama.com.
Install and verify:ollama --version


Pull the phi3 model:ollama pull phi3


Start the Ollama server:ollama serve


Test:curl http://localhost:11434/api/generate -d '{"model": "phi3", "prompt": "Test", "stream": false}'



4. Set Up the Backend 🐍

Navigate to the backend directory:cd backend


Create and activate a virtual environment:python -m venv venv
venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Create a .env file in backend/ with:MONGODB_URI=mongodb://localhost:27017/medical_chatbot
PORT=8000


Run the FastAPI server:python main.py


Verify logs for:INFO:llm:Ollama phi3 initialized successfully



5. Set Up the Frontend ⚛️

Navigate to the frontend directory:cd frontend


Install dependencies:npm install


Run the development server:npm run dev


Open http://localhost:5173 in your browser.

🎨 How It Looks

Frontend: A clean React.js interface with a chat window, styled with CSS for user and bot messages.
User messages: Green background 🌟
Bot messages: Light blue background 💬


Backend: FastAPI handles requests, with MongoDB storing appointments and orders, and Ollama (phi3) powering medical responses.

🐛 Troubleshooting
Empty Context ({}) Issue 🔄

Symptom: Appointment flow skips prompts (e.g., name, date).
Fix:
Backend Logs: Check backend/main.py logs for Received message: ..., Context: .... Ensure Context: {"action":"book_appointment","step":"name"} after “book appointment”.
Frontend Logs: Open browser console (F12 → Console) and verify Sending message: ..., Context: ... and Received response: ..., New context: ....
Solution: Ensured setContext(newContext) in frontend/src/components/Chatbot.jsx and proper context handling in backend/routes/chat.py.



Ollama Issues 🤖

Symptom: LLM not initialized or Connection refused.
Fix:ollama serve
ollama list
curl http://localhost:11434/api/generate -d '{"model": "phi3", "prompt": "Test", "stream": false}'


Pull phi3 if missing: ollama pull phi3.

MongoDB Issues 🗄️

Symptom: Connection errors or No default database defined.
Fix:
Verify .env: MONGODB_URI=mongodb://localhost:27017/medical_chatbot.
Start MongoDB: mongod.
Test: mongo --host localhost --port 27017.



CORS Issues 🌐

Symptom: Frontend fails to connect (browser console errors).
Fix: Ensure main.py CORS allows http://localhost:5173.

📝 Notes

Context Fix ✅: Added logging in chat.py and Chatbot.jsx to ensure context persistence.
Ollama 🧠: phi3 is lightweight; consider llama3 for better performance with GPU.
Production 🔒: Add input validation for medicine names and secure MongoDB access.
Grok API 🌟: Check x.ai/api for future integration.
Contributing 🤝: Feel free to submit issues or PRs to improve the chatbot!

📜 License
MIT License. See LICENSE for details.

Happy Chatting! 😊💉

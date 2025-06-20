# Save the provided markdown content to a README.md file

markdown_content = """
# Medical & Pharmacy AI Chatbot 🤖💊

Welcome to the Medical & Pharmacy AI Chatbot! This project is a full-stack application built to assist users with medical queries, appointment booking, and medicine ordering. Powered by FastAPI, MongoDB, React.js, and Ollama (phi3 model), it runs locally on your Windows machine (`D:\\medical chat bot`) and provides a seamless user experience. 🚀

## ✨ Features

- **General Medical Queries ❓**: Ask questions like "What are flu symptoms?" and get accurate responses from the phi3 model.
- **Appointment Booking 📅**: Book appointments by providing patient name, date, time, and address.
- **Medicine Ordering 💊**: Order medicines with a comma-separated list (e.g., "Paracetamol 10, Ibuprofen 5"), followed by name and address.
- **Context Persistence 🔄**: Fixed empty context (`{}`) issues to ensure smooth appointment and medicine ordering flows.
- **Local LLM 🧠**: Uses Ollama’s phi3 model, avoiding API keys and ensuring privacy.

## 🏗️ Project Structure

- **Backend (`backend/`)**: FastAPI server, MongoDB integration, and Ollama for LLM processing.
- **Frontend (`frontend/`)**: React.js client running on Vite (port 5173).

## 🛠️ Prerequisites

- **Windows 🖥️**: Tested on Windows 10/11.
- **Python 3.8+ 🐍**: For the backend.
- **Node.js 18+ 🚀**: For the frontend.
- **MongoDB 🗄️**: Local MongoDB server or Atlas.
- **Ollama 🤖**: For running the phi3 model locally.

## 🚀 Setup Instructions

### 1. Clone the Repository 📦

```bash
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot

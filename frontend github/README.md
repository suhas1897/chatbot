📁 project-root/
├── 📁 client/                  # ReactJS Frontend
│   ├── 📁 src/
│   │   ├── 📁 components/
│   │   │   ├── ChatBot.js
│   │   │   ├── Cart.js
│   │   │   ├── Checkout.js
│   │   │   └── Login.js
│   │   ├── 📁 pages/
│   │   │   ├── Home.js
│   │   │   ├── AdminDashboard.js
│   │   │   └── Orders.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── 📁 server/                  # Node.js + Express Backend
│   ├── 📁 controllers/
│   │   ├── authController.js
│   │   ├── medicineController.js
│   │   ├── orderController.js
│   │   └── paymentController.js
│   ├── 📁 models/
│   │   ├── User.js
│   │   ├── Medicine.js
│   │   └── Order.js
│   ├── 📁 routes/
│   │   ├── auth.js
│   │   ├── medicines.js
│   │   ├── orders.js
│   │   └── payments.js
│   ├── 📁 utils/
│   │   └── verifyToken.js
│   ├── index.js
│   └── package.json
│
├── 📁 chatbot-api/             # Python FastAPI LLM Chatbot
│   ├── main.py
│   ├── model.py
│   └── requirements.txt
│
├── 📁 config/                  # Environment and shared config
│   └── .env
└── README.md
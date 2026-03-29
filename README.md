# 🤖CLI – AI-Powered Personal Assistant

A modular command-line AI assistant that can **take notes, send WhatsApp messages, and generate intelligent responses using Groq LLM**.

Built with a clean architecture separating **Brain, Tools, and AI**, making it easy to extend into a full AI agent system.

---

## 🚀 Features

* 📝 **Timestamped Notes**

  * Save notes with date & time
* 💬 **WhatsApp Automation**

  * Send messages directly via WhatsApp Web
* 🧠 **AI Responses (Groq LLM)**

  * Ask anything and get intelligent replies
* 🧩 **Modular Architecture**

  * Easily extend with more tools or AI capabilities
* 💻 **CLI Interface**

  * Lightweight and fast

---

## 🧠 Architecture

```
User Input → Brain → Tool / AI → Output
```

* **Brain** → decides intent (note / whatsapp / AI)
* **Tools** → perform actions (notes, messaging)
* **AI Layer** → handles general queries using LLM

---

## 📁 Project Structure

```
CLI_AGENT_V1/
├── main.py
├── brain.py
├── tools/
│   ├── notes.py
│   └── whatsapp.py
├── ai/
│   └── llm.py
├── memory/
│   └── notes.txt
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/CLI-AGENT.git
cd cli-agent
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Assistant

```
python main.py
```

---

## 🧪 Usage Examples

### 📝 Save Notes

```
You: note
→ Enter content: Buy groceries
```

---

### 💬 Send WhatsApp Message

```
You: send whatsapp
→ Enter number: +91XXXXXXXXXX
→ Enter message: Hello!
```

---

### 🧠 Ask AI

```
You: what is operating system
→ AI responds with explanation
```

---

## ⚠️ Important Notes

* WhatsApp automation uses **WhatsApp Web**
* You must be **logged in**
* Message is scheduled **~2 minutes ahead**
* Do not interact with keyboard/mouse during sending

---

## 🛠️ Tech Stack

* Python
* Groq LLM (via LangChain)
* PyWhatKit (WhatsApp automation)
* dotenv

---

## 🔮 Future Improvements

* AI-generated WhatsApp messages 🤖
* Voice input/output 🎤
* RAG-based memory system 🧠
* Fully autonomous AI agent (tool-calling) ⚡
* GUI/Web interface 🌐

---

## 👨‍💻 Author

Soumitra Rajguru

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!

---

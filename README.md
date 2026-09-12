# 🤖 Multi-Chat AI — Multi-Agent Chatbot

> An intelligent multi-agent AI chatbot that uses specialized AI agents and tools to handle different types of user queries.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Gemini](https://img.shields.io/badge/Google%20Gemini-LLM-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Multi--Agent-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

**Multi-Chat AI** is a Generative AI application designed to provide intelligent responses through a multi-agent architecture.

Instead of relying on a single AI workflow, the system can route user requests to specialized agents based on the task.

The project demonstrates concepts such as:

* Generative AI
* LLMs
* Prompt Engineering
* AI Agents
* Tool Calling
* Multi-Agent Systems
* Context-aware conversations
* Streamlit AI applications

---

## ✨ Features

### 💬 Intelligent Chat

Interact with the AI through a simple conversational interface.

### 🤖 Multiple AI Agents

Different agents can be designed for different responsibilities.

Example:

```text
User
  ↓
AI Router
  ↓
┌───────────────┬───────────────┬───────────────┐
│               │               │               │
▼               ▼               ▼               ▼
General Agent   Coding Agent    Data Agent      Tool Agent
│               │               │               │
└───────────────┴───────────────┴───────────────┘
                       ↓
                  Final Response
```

### 🧠 LLM Integration

Uses a modern Large Language Model to understand user questions and generate responses.

### 🛠️ Tool Integration

The architecture can be extended with tools such as:

* Calculator
* Database search
* Document search
* Web search
* Data analysis

### 🎨 Streamlit Interface

A clean web interface built using Streamlit for easy interaction with the AI system.

---

# 🏗️ Architecture

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Chat Interface│
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  AI Router    │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │ General  │   │ Coding   │   │ Data     │
       │ Agent    │   │ Agent    │   │ Agent    │
       └────┬─────┘   └────┬─────┘   └────┬─────┘
            │              │              │
            └──────────────┼──────────────┘
                           ▼
                    ┌───────────────┐
                    │      LLM      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Final Response │
                    └───────────────┘
```

---

# 🔄 Workflow

### Step 1 — User Input

The user enters a question through the Streamlit interface.

### Step 2 — Request Analysis

The AI analyzes the user's request and determines what type of task is required.

### Step 3 — Agent Selection

The appropriate specialized agent is selected.

For example:

```text
"What is Python?"
        ↓
General Agent
```

```text
"Write a Python program for sorting"
        ↓
Coding Agent
```

```text
"Calculate the average salary"
        ↓
Data / Tool Agent
```

### Step 4 — AI Processing

The selected agent sends the request to the LLM with the appropriate system instructions.

### Step 5 — Response

The generated response is returned to the user through the chat interface.

---

# 🧰 Tech Stack

| Technology         | Purpose              |
| ------------------ | -------------------- |
| Python             | Core programming     |
| Google Gemini      | Large Language Model |
| Streamlit          | Web interface        |
| AI Agents          | Task specialization  |
| Prompt Engineering | Agent instructions   |
| Tool Calling       | External actions     |
| GitHub             | Version control      |

---

# 📁 Project Structure

```text
multi-chat-ai/
│
├── app.py
│
├── agents/
│   ├── general_agent.py
│   ├── coding_agent.py
│   └── data_agent.py
│
├── tools/
│   ├── calculator.py
│   └── ...
│
├── utils/
│   └── ...
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
```

> Update the structure above according to the actual files in your repository.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

## 2. Navigate to the project

```bash
cd YOUR_REPOSITORY
```

## 3. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your API key to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💡 Example Queries

Try questions such as:

```text
Explain Python functions.
```

```text
Write a Python program to find duplicate values.
```

```text
Calculate 25% of 8500.
```

```text
Explain machine learning.
```

```text
Create an SQL query to find the second highest salary.
```

The system can route different requests to different agents/tools.

---

# 🧠 Multi-Agent Concept

The key idea behind this project is **specialization**.

Instead of:

```text
User → One AI → Response
```

the architecture can use:

```text
User
 ↓
Router
 ↓
Specialized Agent
 ↓
Tool / LLM
 ↓
Response
```

This approach makes it easier to build AI systems that handle multiple types of tasks.

---

# 📈 Future Enhancements

Planned improvements:

* [ ] Add more specialized agents
* [ ] Add RAG
* [ ] Add PDF document search
* [ ] Add web search
* [ ] Add SQL database agent
* [ ] Add calculator tool
* [ ] Add conversation memory
* [ ] Add LangGraph workflow
* [ ] Add authentication
* [ ] Add chat history
* [ ] Deploy on Streamlit Cloud
* [ ] Add monitoring and logging

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

* Large Language Models
* Generative AI
* Prompt Engineering
* AI Agents
* Multi-Agent Architecture
* Tool Calling
* API Integration
* Python
* Streamlit
* AI Application Development

---

# 📸 Screenshots

Add screenshots of your application here.

```text
docs/
├── home.png
├── chat.png
├── agents.png
└── workflow.png
```

Example:

```markdown
![Application Screenshot](docs/home.png)
```

---

# 👨‍💻 About the Developer

**Suriya Prakash**

AI/ML Trainer | Data Analytics | Generative AI | Agentic AI

Interested in building practical solutions using:

```text
Python
SQL
Data Analytics
Machine Learning
Generative AI
RAG
Agentic AI
LangGraph
CrewAI
Power BI
AWS
```

---

# 🔗 Connect

* GitHub: `https://github.com/suriyaprakash-dev`
* LinkedIn: Add your LinkedIn profile here
* Portfolio: Add your portfolio URL here

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub.



# 🧠 Mental Health Chatbot (PHQ-9 & GAD-7 Assessment)

This Python chatbot helps assess symptoms of **depression** and **anxiety** using clinically recognized tools: **PHQ-9** and **GAD-7**. It uses Google’s **Gemini Pro (via LangChain)** to provide AI-enhanced analysis based on user responses and a PDF reference document.

---

## 🚀 Features

- Asks **PHQ-9** and **GAD-7** mental health questions
- Accepts **natural English responses** (like "yes", "no", "a little")
- Converts them into clinical scoring (0–3 scale)
- Analyzes responses using a **Gemini-powered RetrievalQA agent**
- Uses a **PDF file as vector knowledge base**
- Designed using **LangGraph**, **LangChain**, and **FAISS**

---

## 📂 Project Structure

```

mental\_health\_bot/
│
├── data/
│   └── MentalHealthSummary.pdf       # Your reference document
│
├── faiss\_index/                      # Auto-generated vector store
│
├── prompts/
│   └── phq\_gad\_template.py          # Contains PHQ-9 & GAD-7 question lists
│
├── embeddings.py                    # Loads & embeds the PDF into FAISS
├── agent\_logic.py                   # Chat agent logic with LangGraph
├── main.py                          # Entry point: runs the chatbot
├── .env                             # Stores your Gemini API key
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone and navigate into the project

```bash
git clone https://github.com/your-username/mental_health_bot.git
cd mental_health_bot
````

### 2. Create a virtual environment and activate it

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file in the root folder:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🧠 How to Run

### Step 1: Embed the reference PDF

Make sure your `MentalHealthSummary.pdf` is in the `data/` folder, then run:

```bash
python embeddings.py
```

### Step 2: Run the chatbot

```bash
python main.py
```

You will be asked PHQ-9 and GAD-7 questions. Answer using **natural language** like:

> a little
> yes
> not at all
> nearly every day

The bot will then analyze your responses using Gemini AI and report whether you likely have depression, anxiety, both, or neither.

---

## ✅ Example Responses

```
[PHQ-9] Feeling down, depressed, or hopeless?
> a little

[GAD-7] Feeling nervous, anxious, or on edge?
> nearly every day
```

---

## 🛡️ Disclaimer

This tool is for **educational and research purposes only**. It does **not replace professional medical advice**. Always consult a mental health professional for clinical evaluation and support.

---




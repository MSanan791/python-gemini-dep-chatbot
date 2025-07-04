
# 🧠 Mental Health Screening Chatbot (PHQ-9 & GAD-7)

A terminal-based chatbot built with **LangChain**, **Gemini API**, and **FAISS** that screens users for signs of **depression** and **anxiety** using clinically validated tools (**PHQ-9**, **GAD-7**) and **DSM-5 criteria** as reference.

---

## 📌 Features

- Prompts user with PHQ-9 and GAD-7 clinical questions
- Uses Gemini LLM to analyze responses kindly and intelligently
- References official criteria from DSM-5 to assess severity
- Runs locally with no frontend required
- Easily extendable to add GUI, logging, scoring, or web interface

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mental-health-chatbot.git
cd mental-health-chatbot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

<details>
<summary>📦 If no <code>requirements.txt</code>, manually install:</summary>

```bash
pip install langchain langchain-community langchain-google-genai \
             google-generativeai faiss-cpu sentence-transformers \
             pypdf
```

</details>

---

### 3. Set your API keys

#### 🌐 Gemini (Chat + Embeddings)

Option 1: Use **Google Cloud service account JSON** (recommended for embeddings):

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
```

Option 2: If using only chat (not embeddings):

```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

---

### 4. Add Reference Document

Put this file (already included or generate it yourself) in the `documents/` folder:

```
documents/dsm5_excerpt.pdf
```

This should include summaries of:

* PHQ-9
* GAD-7
* DSM-5 Diagnostic Criteria

---

### 5. Run the chatbot

```bash
python mental_health_chatbot.py
```

You'll be prompted with 16 clinical questions and receive a kind, supportive assessment.

---

## 📁 File Structure

```
mental-health-chatbot/
│
├── documents/
│   └── dsm5_excerpt.pdf         # Reference doc for PHQ-9, GAD-7, DSM-5
│
├── mental_health_chatbot.py    # Main chatbot logic
├── README.md                   # This file
└── requirements.txt            # (optional) pip install deps
```

---

## 🧠 Screening Tools Used

| Tool  | Purpose                   |
| ----- | ------------------------- |
| PHQ-9 | Depression Screening      |
| GAD-7 | Anxiety Screening         |
| DSM-5 | Clinical Diagnostic Guide |

---

## 📄 Disclaimer

This tool is **for educational and informational purposes only**.
It is **not a replacement for clinical diagnosis**.
Please consult a licensed mental health professional for personalized support.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve this chatbot, enhance UX, or add model support.

---




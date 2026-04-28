# 🧠 SEMANTIC RESEARCH INTERFACE

Lightweight research tool that generates structured summaries from a given topic using Wikipedia data and keyword-based semantic mapping.

---

## 🚀 OVERVIEW

This project allows users to input a topic and receive:

- A structured summary
- Related contextual insights
- Relevant references
- An emoji associated with the topic based on semantic matching

The goal is to provide fast and simplified research support.

---

## 🌐 Live Demo

👉 https://bea3gomes.github.io/semantic-research-interface/

---

## ⚙️ HOW IT WORKS

1. The user enters a topic
2. The system queries the Wikipedia API
3. Relevant content is extracted and cleaned
4. The system selects the best matching content
5. A structured summary is generated
6. An emoji is assigned based on keyword mapping

---

## 🧩 TECH STACK

- **Frontend:** HTML, CSS  
- **Backend:** Python (Flask)  
- **Data Source:** Wikipedia API  
- **Logic:**
  - Keyword matching
  - Heuristic ranking
  - Rule-based summarization

---

## 🎯 FEATURES

- 🔍 Topic-based search
- 🧠 Automatic summary generation
- 🎯 Emoji semantic mapping
- 📊 Structured output (summary + references)
- ⚡ Fast response with caching

---

## ⚠️ LIMITATIONS

- Does not use real AI models (rule-based logic)
- Emoji system is static (predefined dictionary)
- Depends on Wikipedia content quality

---

## 🔮 FUTURE IMPROVEMENTS

- Integrate AI for smarter summarization
- Improve semantic matching (NLP / embeddings)
- Add multiple data sources (not only Wikipedia)
- Improve ranking algorithm

---

## ▶️ HOW TO RUN

### Backend

```bash
pip install -r requirements.txt
python app.py

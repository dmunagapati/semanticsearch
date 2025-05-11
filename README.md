# Semantic Search Notes App 

An AI-powered web app that lets you upload notes or paste text, then ask natural language questions to retrieve the most relevant parts — using Cohere embeddings and semantic similarity.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)
![Cohere](https://img.shields.io/badge/Cohere-NLP-purple)
![Deployed on Render](https://img.shields.io/badge/Deployed-Render-blue)

---

## Features

- Upload text files or paste notes directly
- Ask questions in natural language
- Uses Cohere to embed your notes and compute semantic similarity
- Supports `.txt` and `.pdf` file upload (limited to 2MB)
- Simple UI with Flask + HTML/CSS

---

## Demo

Deployed on [Render](https://render.com/) (link coming soon)

---

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (static)
- **AI API**: [Cohere](https://cohere.ai/)
- **PDF Parsing**: PyPDF2
- **Similarity Calculation**: scikit-learn (`cosine_similarity`)

---

## Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/semanticsearch.git
cd semanticsearch

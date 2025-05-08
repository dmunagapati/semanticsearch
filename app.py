import os
import cohere
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader

co = cohere.Client("O0h3LoeEwiNJZZ323zLzikGHxZl7iGaphEf2ladz")

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2 MB

notes_text = ""
chunks = []
embeds = []

@app.route("/", methods=["GET", "POST"])
def index():
    global notes_text, chunks, embeds
    result = []

    if request.method == "POST":
        # Uploading Notes
        if request.form.get("action") == "upload":
            # 1. Textarea
            if request.form.get("notes").strip():
                notes_text = request.form["notes"]
            # 2. File upload
            elif "file" in request.files:
                uploaded_file = request.files["file"]
                if uploaded_file and uploaded_file.filename.endswith(".txt"):
                    notes_text = uploaded_file.read().decode(errors="ignore")
                elif uploaded_file and uploaded_file.filename.endswith(".pdf"):
                    reader = PdfReader(uploaded_file)
                    notes_text = "\n".join(page.extract_text() or "" for page in reader.pages)

            # Embed if we have valid notes
            if notes_text.strip():
                chunks, embeds = embed_chunks(notes_text)

        # Question asking
        elif "question" in request.form and chunks:
            question = request.form["question"]
            result = search_relevant_chunks(question, chunks, embeds)

    return render_template("index.html", results=result)


def embed_chunks(text):
    text_chunks = [chunk.strip() for chunk in text.split('\n') if chunk.strip()]
    if not text_chunks:
        return [], []
    response = co.embed(texts=text_chunks, model="embed-english-v3.0", input_type="clustering")
    return text_chunks, response.embeddings

def search_relevant_chunks(query, chunks, embeddings):
    query_embed = co.embed(texts=[query], model="embed-english-v3.0", input_type="search_query").embeddings[0]
    sims = cosine_similarity([query_embed], embeddings)[0]
    ranked = sorted(zip(sims, chunks), reverse=True)
    return [chunk for _, chunk in ranked[:3]]


if __name__ == "__main__":
    app.run(debug=True)

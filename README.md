Legal Document Summarizer

Summarizes PDFs into 3–4 bullet points using a local LLaMA model via llama-cpp-python.

Features

Extracts text from PDF legal documents

Summarizes into short, clear bullet points

Runs entirely offline using a local LLaMA model

Supports large documents by chunking text

Setup
 Clone or Download the Repository

If you are using Git:

git clone https://github.com/mahithamunjeti/legal-document-summarizer.git
cd legal-document-summarizer


Or simply download the project folder and open it.

Install Requirements

Make sure you have Python 3.9+ installed. Then run:

pip install -r requirements.txt

1. Download the LLaMA Model

Use Hugging Face CLI to download:

huggingface-cli download bartowski/Llama-3.2-3B-Instruct-GGUF \
   --include "Llama-3.2-3B-Instruct-Q4_K_M.gguf" --local-dir models/

4. Place Your PDF File

Put your target legal PDF document in the project folder.

5. Run the Script
python summarize_pdf.py

Requirements

pdfplumber

llama-cpp-python

Python 3.9 or later
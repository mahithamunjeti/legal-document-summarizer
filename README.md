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

Example Output

📃 Short Summary:

Confidential Information includes proprietary and confidential information with commercial value or utility.

The Receiving Party must keep confidential information confidential and restrict access to employees and third parties.

The Receiving Party must obtain prior written approval from the Disclosing Party before using, publishing, or disclosing confidential information.

The nondisclosure provisions survive beyond the end of the agreement and remain in effect until the confidential information is no longer a trade secret.

Requirements

pdfplumber

llama-cpp-python

Python 3.9 or later
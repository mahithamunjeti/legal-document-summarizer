import pdfplumber
from llama_cpp import Llama
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

sys.stdout.reconfigure(encoding='utf-8')

# Step 1: Load your LLM model
MODEL_PATH = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"  # Fixed path to match actual file

if not os.path.exists(MODEL_PATH):
    print(f"❌ Model file not found at {MODEL_PATH}")
    print("Please ensure the model file is in the same directory as this script.")
    sys.exit(1)

try:
    llm = Llama(
        model_path=MODEL_PATH,
        n_threads=4,  # Reduced for better stability
        n_batch=128,  # Reduced batch size
        n_ctx=2048,
        n_gpu_layers=0  # Disable GPU layers for CPU-only operation
    )
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    sys.exit(1)

# Step 2: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except Exception as e:
        print(f"❌ Error extracting text from PDF: {e}")
        return None

# Step 3: Summarize using LLM (chunking for large PDFs)
def summarize_text(text, chunk_size=1000):  # Reduced chunk size for better performance
    if not text:
        return "No text to summarize."
    
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    partial_summaries = []

    for i, chunk in enumerate(chunks, start=1):
        print(f"📄 Summarizing chunk {i}/{len(chunks)}...")
        try:
            prompt = f"""
You are a legal document summarizer.
Summarize the following text into exactly 3–4 clear bullet points.
Do not include the original text in your output.
Keep it concise and preserve all key meanings.

Text:
{chunk}

Summary:
"""
            output = llm(
                prompt,
                max_tokens=150,  # Reduced for faster processing
                temperature=0.1,  # Lower temperature for more consistent output
                stop=["Text:", "###"]
            )
            summary_text = output["choices"][0]["text"].strip()
            partial_summaries.append(summary_text)
        except Exception as e:
            print(f"⚠️  Warning: Error processing chunk {i}: {e}")
            continue

    if not partial_summaries:
        return "Failed to generate summary. Please try again."

    print("\n🔄 Combining partial summaries into final summary...")
    try:
        combined_text = " ".join(partial_summaries)
        final_prompt = f"""
Combine the following partial summaries into a single, clean set of 3–4 bullet points,
removing duplicates and keeping it short and clear:

{combined_text}

Final Summary:
"""
        final_output = llm(final_prompt, max_tokens=150, temperature=0.1, stop=["###"])
        return final_output["choices"][0]["text"].strip()
    except Exception as e:
        print(f"⚠️  Warning: Error generating final summary: {e}")
        return " ".join(partial_summaries)  # Return partial summaries if final combination fails

# Step 4: Run with file dialog
if __name__ == "__main__":
    # Open a file selection dialog
    Tk().withdraw()  # Hide the root window
    pdf_path = askopenfilename(
        title="Select a PDF file to summarize",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_path:
        print("No file selected. Exiting...")
        exit()

    print(f"📁 Processing: {pdf_path}")
    
    text = extract_text_from_pdf(pdf_path)
    if text is None:
        print("❌ Failed to extract text from PDF. Exiting...")
        sys.exit(1)
    
    if not text.strip():
        print("⚠️  No readable text found in the PDF.")
        sys.exit(1)
    
    print(f"📄 Extracted {len(text)} characters of text")
    
    summary = summarize_text(text)

    print("\n📃 Short Summary:\n")
    print(summary)

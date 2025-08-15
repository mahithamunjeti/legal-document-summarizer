import pdfplumber
from llama_cpp import Llama
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Step 1: Load your LLM model
llm = Llama(
    model_path="models/Llama-3.2-3B-Instruct-Q4_K_M.gguf",
    n_threads=8,
    n_batch=256,
    n_ctx=2048
)

# Step 2: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# Step 3: Summarize using LLM (chunking for large PDFs)
def summarize_text(text, chunk_size=1500):
    # Break text into smaller chunks for processing
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    partial_summaries = []

    for i, chunk in enumerate(chunks, start=1):
        print(f"📄 Summarizing chunk {i}/{len(chunks)}...")
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
            max_tokens=200,
            temperature=0.3,
            stop=["Text:", "###"]
        )
        summary_text = output["choices"][0]["text"].strip()
        partial_summaries.append(summary_text)

    # Step 4: Combine chunk summaries into one final summary
    print("\n🔄 Combining partial summaries into final summary...")
    combined_text = " ".join(partial_summaries)
    final_prompt = f"""
Combine the following partial summaries into a single, clean set of 3–4 bullet points,
removing duplicates and keeping it short and clear:

{combined_text}

Final Summary:
"""
    final_output = llm(final_prompt, max_tokens=200, temperature=0.3, stop=["###"])
    return final_output["choices"][0]["text"].strip()

# Step 5: Run
if __name__ == "__main__":
    pdf_path = "sample_legal_doc.pdf"  # Replace with your file path
    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text(text)
    print("\n📃 Short Summary:\n")
    print(summary)

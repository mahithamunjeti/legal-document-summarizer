import streamlit as st
import pdfplumber
from llama_cpp import Llama
import os

# -----------------------
# Config
# -----------------------
MODEL_PATH = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"  # Fixed path to match actual file

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found at {MODEL_PATH}. Please ensure the model file is in the same directory as this script.")
    st.stop()

st.set_page_config(page_title="Legal Document Summarizer", layout="wide")
st.title("📄 Legal Document Summarizer")
st.write("Upload a legal PDF document and get a concise summary in bullet points.")

# -----------------------
# Load LLaMA model (cache to avoid reloads)
# -----------------------
@st.cache_resource
def load_model():
    try:
        # Reduced context and threads for better performance
        return Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=4, n_gpu_layers=0)
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

# Load model with error handling
try:
    llm = load_model()
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -----------------------
# Summarize text in chunks
# -----------------------
def summarize_text(text, chunk_size=1000):  # Reduced chunk size for better performance
    # Split text into chunks
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    partial_summaries = []

    for i, chunk in enumerate(chunks, start=1):
        with st.spinner(f"Summarizing chunk {i}/{len(chunks)}..."):
            try:
                prompt = f"""You are a legal document summarizer. Summarize the following legal text into exactly 3-4 clear bullet points. Do not include the original text in your output. Keep it concise and preserve all key meanings.

Text:
{chunk}

Summary:"""
                output = llm(prompt, max_tokens=200, temperature=0.1, stop=["Text:", "###"])
                partial_summaries.append(output['choices'][0]['text'].strip())
            except Exception as e:
                st.warning(f"Error processing chunk {i}: {e}")
                continue

    if not partial_summaries:
        return "Failed to generate summary. Please try again."

    # Combine partial summaries into a final summary
    try:
        combined_text = " ".join(partial_summaries)
        final_prompt = f"""Combine the following partial summaries into a single, clean set of 3-4 bullet points, removing duplicates and keeping it short and clear:

{combined_text}

Final Summary:"""
        final_output = llm(final_prompt, max_tokens=200, temperature=0.1, stop=["###"])
        return final_output['choices'][0]['text'].strip()
    except Exception as e:
        st.warning(f"Error generating final summary: {e}")
        return " ".join(partial_summaries)  # Return partial summaries if final combination fails

# -----------------------
# File uploader
# -----------------------
uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

        if not text.strip():
            st.warning("No readable text found in the PDF. Please try another file.")
        else:
            st.subheader("📃 Summary")
            
            # Show extracted text length for debugging
            st.info(f"📄 Extracted {len(text)} characters of text")
            
            with st.spinner("Generating summary..."):
                summary = summarize_text(text)
            
            st.success("✅ Summary generated successfully!")
            
            # Display the summary in a more prominent way
            st.markdown("### Generated Summary:")
            st.markdown(summary)
            
            # Add debugging info
            with st.expander("🔍 Debug Information"):
                st.write("**Extracted Text Preview:**")
                st.text(text[:500] + "..." if len(text) > 500 else text)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
        st.info("Please ensure the file is a valid PDF and try again.")

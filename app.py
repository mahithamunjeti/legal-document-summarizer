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

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="Legal Document Translator",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# Custom CSS for better styling
# -----------------------
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .upload-section {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 2px dashed #dee2e6;
        text-align: center;
        margin-bottom: 2rem;
    }
    .summary-box {
        background: #e8f5e8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .info-box {
        background: #e7f3ff;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #007bff;
    }
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Model status
    st.markdown("### 🤖 Model Status")
    if os.path.exists(MODEL_PATH):
        st.success("✅ Model Available")
        st.info(f"**Model:** Mistral 7B Instruct")
        st.info(f"**Size:** 4.07 GB")
    else:
        st.error("❌ Model Not Found")
    
    # Processing options
    st.markdown("### ⚡ Processing Options")
    chunk_size = st.slider("Chunk Size", min_value=500, max_value=2000, value=1000, step=100, 
                           help="Larger chunks = fewer API calls but more memory usage")
    
    max_tokens = st.slider("Max Tokens", min_value=100, max_value=300, value=200, step=50,
                           help="Maximum length of generated summary")
    
    temperature = st.slider("Creativity", min_value=0.0, max_value=0.5, value=0.1, step=0.1,
                           help="Lower = more focused, Higher = more creative")
    
    st.markdown("---")
    st.markdown("### 📚 About")
    st.markdown("""
    This tool helps you understand legal documents by translating them into simple, everyday English.
    
    **Features:**
    - 📄 PDF text extraction
    - 🧠 AI-powered summarization
    - 💬 Simple language output
    - 🔍 Key point highlighting
    """)

# -----------------------
# Main Content
# -----------------------
# Header
st.markdown("""
<div class="main-header">
    <h1>📄 Legal Document Translator</h1>
    <p style="font-size: 1.2rem; margin: 0;">Transform complex legal documents into simple, understandable explanations</p>
</div>
""", unsafe_allow_html=True)

# -----------------------
# Load LLaMA model (cache to avoid reloads)
# -----------------------
@st.cache_resource
def load_model():
    try:
        # Use sidebar values for dynamic configuration
        return Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=4, n_gpu_layers=0)
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

# Load model with error handling
try:
    llm = load_model()
    # Move success message to sidebar
    with st.sidebar:
        st.success("✅ Model Loaded!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -----------------------
# Summarize text in chunks
# -----------------------
def summarize_text(text, chunk_size=1000, max_tokens=200, temperature=0.1):
    # Split text into chunks
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    partial_summaries = []

    # Progress bar for chunks
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, chunk in enumerate(chunks, start=1):
        status_text.text(f"📄 Processing chunk {i}/{len(chunks)}...")
        progress_bar.progress(i / len(chunks))
        
        try:
            prompt = f"""You are a helpful legal document translator. Your job is to explain legal documents in simple, everyday English that anyone can understand.

Read this legal text and explain the MOST IMPORTANT points in simple terms. Focus on:
- What this document is about
- Who it involves
- What they're agreeing to do
- Any important dates or deadlines
- Any money or consequences involved

Write your answer in 3-4 simple bullet points using everyday language. Avoid legal jargon.

Text:
{chunk}

Simple Summary:"""
            output = llm(prompt, max_tokens=max_tokens, temperature=temperature, stop=["Text:", "###"])
            partial_summaries.append(output['choices'][0]['text'].strip())
        except Exception as e:
            st.warning(f"⚠️ Error processing chunk {i}: {e}")
            continue

    progress_bar.empty()
    status_text.empty()

    if not partial_summaries:
        return "Failed to generate summary. Please try again."

    # Combine partial summaries into a final summary
    try:
        st.info("🔄 Combining summaries into final explanation...")
        combined_text = " ".join(partial_summaries)
        final_prompt = f"""Take these partial summaries and create ONE clear, simple summary in everyday English. 

Focus on the MOST IMPORTANT information that someone needs to know. Use simple language and avoid legal terms.

Combine everything into 3-4 clear bullet points that explain:
- What this document is about
- Who it involves  
- What they're agreeing to
- Any important details (dates, money, consequences)

{combined_text}

Final Simple Summary:"""
        final_output = llm(final_prompt, max_tokens=max_tokens, temperature=temperature, stop=["###"])
        return final_output['choices'][0]['text'].strip()
    except Exception as e:
        st.warning(f"⚠️ Error generating final summary: {e}")
        return " ".join(partial_summaries)  # Return partial summaries if final combination fails

# -----------------------
# File uploader
# -----------------------
st.markdown("""
<div class="upload-section">
    <h3>📂 Upload Your Legal Document</h3>
    <p>Drag and drop or click to upload a PDF file</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

if uploaded_file is not None:
    # File info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("File Name", uploaded_file.name)
    with col2:
        st.metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")
    with col3:
        st.metric("File Type", "PDF")
    
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

        if not text.strip():
            st.warning("⚠️ No readable text found in the PDF. Please try another file.")
        else:
            st.markdown("## 📝 Document Analysis")
            
            # Show extracted text info
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("""
                <div class="info-box">
                    <strong>📄 Text Extracted Successfully</strong><br>
                    Ready to generate simple explanation
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.metric("Characters", len(text))
                st.metric("Pages", len(pdf.pages))
            
            # Generate summary button
            if st.button("🚀 Generate Simple Explanation", use_container_width=True):
                with st.spinner("🤖 AI is analyzing your document..."):
                    summary = summarize_text(text, chunk_size, max_tokens, temperature)
                
                st.markdown("## ✨ What This Document Means")
                st.markdown(f"""
                <div class="summary-box">
                    {summary}
                </div>
                """, unsafe_allow_html=True)
                
                # Download summary option
                st.download_button(
                    label="💾 Download Summary",
                    data=summary,
                    file_name=f"{uploaded_file.name.replace('.pdf', '')}_summary.txt",
                    mime="text/plain"
                )
            
            # Debug information in expandable section
            with st.expander("🔍 Technical Details"):
                st.write("**Extracted Text Preview:**")
                st.text_area("", text[:1000] + "..." if len(text) > 1000 else text, height=200, disabled=True)

    except Exception as e:
        st.error(f"❌ An error occurred while processing the file: {e}")
        st.info("💡 Please ensure the file is a valid PDF and try again.")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>Built with ❤️ using Streamlit and Mistral AI | Legal Document Translator v2.0</p>
</div>
""", unsafe_allow_html=True)

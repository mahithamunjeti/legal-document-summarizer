• Legal Document Translator

Transform complex legal documents into simple, understandable explanations using AI

A powerful tool that uses local AI models to translate complex legal documents into clear, everyday English. Perfect for lawyers, business professionals, students, or anyone who needs to quickly understand legal documents without the jargon.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)
![AI](https://img.shields.io/badge/AI-Mistral%207B-green.svg)
![Offline](https://img.shields.io/badge/Offline-Local%20Model-orange.svg)

• Features

- AI-Powered: Local Mistral 7B model for offline processing
- PDF Support: Extract and process any legal PDF document
- Simple Language: Convert legal jargon to everyday English
- Key Points: Focus on the most important information
- Web Interface: Beautiful Streamlit app with interactive controls
- CLI Tool: Command-line interface for quick processing
- Customizable: Adjustable processing parameters

• Quick Start

• Prerequisites
- Python 3.9+
- 4GB+ RAM
- Legal PDF document

• Installation

1. Clone & Install
   ```bash
   git clone https://github.com/mahithamunjeti/legal-document-summarizer.git
   cd legal-document-summarizer
   pip install -r requirements.txt
   ```

2. Add AI Model
   - Place `mistral-7b-instruct-v0.1.Q4_K_M.gguf` in project root

3. Run the App
   ```bash
   # Web Interface (Recommended)
   streamlit run app.py
   
   # Command Line
   python summarize_pdf.py
   ```

• Usage

• Web Interface
1. Upload your PDF document
2. Adjust settings in the sidebar (optional)
3. Click "Generate Simple Explanation"
4. Get your results in simple English
5. Download the summary as text file

• Command Line
```bash
python summarize_pdf.py
# Select PDF when prompted
```

• Example Output

Instead of:
"The Parties hereto agree that in the event of any such invalidity or unenforceability..."

You get:
• This is an agreement between two people or companies
• They're agreeing to work together on a specific project
• The project starts on July 1st and ends on August 1st
• Each person puts in $500, so the total budget is $1000

• Configuration

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| Chunk Size | 500-2000 | 1000 | Text processing chunks |
| Max Tokens | 100-300 | 200 | Summary length |
| Creativity | 0.0-0.5 | 0.1 | AI response focus |

• Requirements

- streamlit - Web framework
- pdfplumber - PDF processing
- llama-cpp-python - AI inference
- Python 3.9+ - Runtime
- 4GB+ RAM - For AI model

• Project Structure

```
├── app.py                 # Streamlit web app
├── summarize_pdf.py       # CLI tool
├── requirements.txt       # Dependencies
├── README.md             # This file
└── mistral-7b-instruct-v0.1.Q4_K_M.gguf  # AI model
```

• Contributing

- Report bugs
- Suggest features
- Improve docs
- Submit code

---

Made with Streamlit and Mistral AI

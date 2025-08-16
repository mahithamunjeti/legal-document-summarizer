# 📄 Legal Document Translator

> **Transform complex legal documents into simple, understandable explanations using AI**

A powerful tool that uses local AI models to translate complex legal documents into clear, everyday English. Perfect for lawyers, business professionals, students, or anyone who needs to quickly understand legal documents without the jargon.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)
![AI](https://img.shields.io/badge/AI-Mistral%207B-green.svg)
![Offline](https://img.shields.io/badge/Offline-Local%20Model-orange.svg)

## ✨ Features

### 🧠 **AI-Powered Translation**
- **Local AI Model**: Runs entirely offline using Mistral 7B Instruct
- **Smart Summarization**: Breaks down complex legal language into simple explanations
- **Key Point Highlighting**: Focuses on the most important information
- **Everyday Language**: Translates legal jargon into simple English

### 📄 **Document Processing**
- **PDF Support**: Extract text from any legal PDF document
- **Large Document Handling**: Processes documents of any size through intelligent chunking
- **Text Extraction**: High-quality text extraction using pdfplumber
- **Multi-page Support**: Handles documents with multiple pages

### 🎨 **User Experience**
- **Web Interface**: Beautiful Streamlit web application
- **Command Line Tool**: Simple CLI for quick processing
- **Interactive Controls**: Adjustable processing parameters
- **Progress Tracking**: Real-time progress indicators
- **Download Results**: Save summaries as text files

### ⚙️ **Customization**
- **Adjustable Chunk Size**: Control memory usage vs. processing speed
- **Token Limits**: Customize summary length
- **Creativity Control**: Adjust AI response creativity
- **Model Parameters**: Fine-tune performance settings

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+** installed on your system
- **4GB+ RAM** for the AI model
- **Legal PDF document** to process

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mahithamunjeti/legal-document-summarizer.git
   cd legal-document-summarizer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download AI Model**
   ```bash
   # The model file should be: mistral-7b-instruct-v0.1.Q4_K_M.gguf
   # Place it in the project root directory
   ```

4. **Run the Application**
   ```bash
   # Web Interface (Recommended)
   streamlit run app.py
   
   # Command Line Tool
   python summarize_pdf.py
   ```

## 📱 Usage

### Web Interface (Recommended)

1. **Launch the App**
   ```bash
   streamlit run app.py
   ```

2. **Upload Document**
   - Drag and drop your PDF file
   - Or click to browse and select

3. **Configure Settings** (Optional)
   - Adjust chunk size, token limits, and creativity
   - Use the sidebar controls

4. **Generate Summary**
   - Click "Generate Simple Explanation"
   - Watch the progress bar
   - Get your results in simple English

5. **Download Results**
   - Save the summary as a text file
   - Share or store for later reference

### Command Line Tool

```bash
python summarize_pdf.py
```

- A file dialog will open automatically
- Select your PDF document
- Get instant summary in the terminal

## 🎯 What You'll Get

Instead of complex legal language like:
> "The Parties hereto agree that in the event of any such invalidity or unenforceability, the Parties shall attempt in good faith to replace the invalid or unenforceable provision with a provision that is valid and enforceable..."

You'll get simple explanations like:
> • **This is an agreement** between two people or companies
> • **They're agreeing to work together** on a specific project or goal  
> • **The project starts on July 1st** and ends on August 1st
> • **Each person puts in $500**, so the total budget is $1000

## ⚙️ Configuration

### Processing Options

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| **Chunk Size** | 500-2000 | 1000 | Text processing chunks (larger = fewer calls, more memory) |
| **Max Tokens** | 100-300 | 200 | Maximum summary length |
| **Creativity** | 0.0-0.5 | 0.1 | AI response creativity (lower = more focused) |

### Model Settings

- **Model**: Mistral 7B Instruct (Q4_K_M quantized)
- **Context Window**: 2048 tokens
- **Threads**: 4 CPU threads
- **Memory**: ~3.2 GB model buffer + 256 MB cache

## 🔧 Technical Details

### Architecture
- **Frontend**: Streamlit web framework
- **AI Engine**: llama-cpp-python with Mistral 7B
- **PDF Processing**: pdfplumber for text extraction
- **Text Processing**: Intelligent chunking and summarization

### Performance
- **Processing Speed**: ~4-5 tokens per second (CPU)
- **Memory Usage**: ~3.5 GB total
- **Document Size**: Unlimited (chunked processing)
- **Response Time**: 30-60 seconds for typical documents

## 📁 Project Structure

```
legal-document-summarizer/
├── app.py                 # Streamlit web application
├── summarize_pdf.py       # Command line tool
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── mistral-7b-instruct-v0.1.Q4_K_M.gguf  # AI model
└── sample_legal_doc.pdf  # Example document
```

## 🛠️ Requirements

### Core Dependencies
- **streamlit** - Web application framework
- **pdfplumber** - PDF text extraction
- **llama-cpp-python** - Local AI model inference

### System Requirements
- **Python**: 3.9 or later
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 5GB for model and dependencies
- **OS**: Windows, macOS, or Linux

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 **Report bugs** or issues
- 💡 **Suggest new features**
- 📝 **Improve documentation**
- 🔧 **Submit code improvements**

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Mistral AI** for the powerful language model
- **Streamlit** for the excellent web framework
- **llama-cpp-python** for efficient local inference
- **pdfplumber** for reliable PDF processing

## 📞 Support

If you need help or have questions:

- 📧 **Create an issue** on GitHub
- 🔍 **Check existing issues** for solutions
- 📚 **Review the documentation** above

---

**Made with ❤️ using Streamlit and Mistral AI**

*Transform your legal documents from complex jargon to simple understanding in seconds!*
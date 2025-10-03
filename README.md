 
# AI Q&A Bot Project

## Overview
A simple command-line AI-powered question-answering bot built with Hugging Face Transformers. This project demonstrates how to create a basic conversational AI system that can answer questions based on provided context.

## Features
- ✅ Command-line interface for easy interaction
- 🤖 Uses Hugging Face's free pre-trained models
- 📚 Context-based question answering
- 💡 Confidence scoring for answers
- 🚀 No API key required for basic functionality
- 📊 User-friendly output with emojis and formatting

## Requirements
- Python 3.7+
- Internet connection (for downloading models on first run)

## Installation

### Step 1: Clone or Download
```bash
git clone <your-repository-url>
cd ai-qa-bot
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Environment File (Optional)
Create a `.env` file in the project root:
```
HUGGING_FACE_TOKEN=your_token_here
```
*Note: Token is optional for free models*

## Usage

### Running the Bot
```bash
python main.py
```

### How It Works
1. **Initialization**: The bot loads a pre-trained question-answering model
2. **Context Input**: Provide context text or use the default Python context
3. **Ask Questions**: Type questions about the context
4. **Get Answers**: Receive AI-generated answers with confidence scores

### Example Interaction
```
🚀 AI Q&A Bot - Powered by Hugging Face
===============================================
🤖 Initializing AI Q&A Bot...
📚 Loading Hugging Face model (this may take a moment)...
✅ Bot initialized successfully!

📖 Please provide some context...
📝 Using default context about Python programming.

🎯 You can now ask questions about the provided context!
💡 Type 'quit', 'exit', or 'bye' to stop the bot.

❓ Your question: What is Python?
🤔 Thinking...

🤖 Answer: a high-level, interpreted programming language with dynamic semantics
📊 Confidence: 89.45%
✅ High confidence answer!
```

### Commands
- Ask any question about the provided context
- Type `context` to view the current context
- Type `quit`, `exit`, or `bye` to stop the bot

## Project Structure
```
ai-qa-bot/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (optional)
├── README.md           # This file
├── .gitignore          # Git ignore rules
└── app.py              # Streamlit UI (stretch goal)
```

## Stretch Goals (Optional Enhancements)

### 1. Web Interface with Streamlit
Create `app.py` for a web-based interface:
```python
import streamlit as st
from transformers import pipeline

# Initialize the model
@st.cache_resource
def load_qa_model():
    return pipeline("question-answering")

# Your Streamlit app code here
```

Run with: `streamlit run app.py`

### 2. Deployment Options
- **Streamlit Cloud**: Deploy directly from GitHub
- **Hugging Face Spaces**: Free hosting for ML apps
- **Render**: Simple web app deployment

## Troubleshooting

### Common Issues
1. **Model Download Slow**: First run downloads ~250MB model
2. **Memory Issues**: Model requires ~1GB RAM
3. **Import Errors**: Ensure all dependencies are installed

### Solutions
```bash
# If transformers installation fails:
pip install --upgrade pip
pip install transformers torch --no-cache-dir

# For PyTorch CPU-only version:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## Technical Details

### Model Used
- **Name**: `distilbert-base-cased-distilled-squad`
- **Type**: Question Answering
- **Size**: ~250MB
- **Language**: English
- **Training**: SQuAD dataset (Stanford Question Answering Dataset)

### Dependencies
- `transformers`: Hugging Face transformers library
- `torch`: PyTorch for model inference
- `python-dotenv`: Environment variable management
- `streamlit`: Web interface (optional)

## Learning Outcomes
By building this project, you will learn:
- How to use Hugging Face Transformers
- Command-line application development
- AI model integration in Python
- Git version control basics
- Project documentation with README

## Next Steps
1. ✅ Basic command-line bot (completed)
2. 🔄 Add web interface with Streamlit
3. 🚀 Deploy to Hugging Face Spaces
4. 📊 Add conversation history
5. 🎨 Improve UI/UX design
6. 📈 Add different AI models for comparison

## Resources
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [SQuAD Dataset](https://rajpurkar.github.io/SQuAD-explorer/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is for educational purposes. Model licenses apply to their respective models.
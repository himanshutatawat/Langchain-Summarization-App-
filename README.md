# Langchain Summarization App  

## Overview  
This project is a **Streamlit-based web application** that summarizes text content from **YouTube videos** and **web pages**. It leverages **LangChain**, **GROQ API**, and **LLMs** to generate concise summaries.  

## Features  
- 📌 **Summarizes YouTube video transcripts**  
- 🌐 **Extracts and summarizes web page content**  
- 🚀 **Uses LangChain's LLMs (Gemma2-9B-IT via GROQ API)**  
- 🎯 **Validates and processes URLs before summarization**  
- ⚡ **Easy-to-use Streamlit UI**  

## Installation  

### Prerequisites  
Ensure you have Python 3.8+ installed.  

### Install Dependencies  
Run the following command to install the required libraries:  

```sh
pip install streamlit langchain langchain_groq validators langchain_community
```

## Usage  

### 1️⃣ Run the Streamlit App  
Execute the following command:  

```sh
streamlit run app.py
```

### 2️⃣ Enter Details  
- **Groq API Key:** Enter your GROQ API Key in the sidebar.  
- **YouTube or Website URL:** Provide a valid YouTube video or webpage URL.  
- Click **"Summarize"** to generate a summary.  

## Environment Variables  
You must provide a **Groq API Key** to access the LLM:  

```sh
export GROQ_API_KEY="your_groq_api_key"
```

Alternatively, enter it in the Streamlit sidebar during runtime.  

## Project Structure  

```
📂 langchain-summarization
│── app.py              # Main Streamlit application
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
```

## Future Enhancements  
- ✅ Improve LLM response quality with **better prompting**  
- ✅ Support **multiple language summarization**  
- ✅ Allow **file-based** summarization (PDFs, Docs)  

## License  
This project is open-source and available under the **MIT License**.  


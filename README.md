
# Prompt Engineering with Python & Gemini

## Overview

This project demonstrates basic to advanced **Prompt Engineering concepts using Python** and a **Google Gemini + Streamlit application**.

## Topics Covered

* Basic prompt creation
* User-input based prompts
* Dynamic prompts using loops
* Prompt templates
* Dynamic prompts using lists
* Step-by-step prompting
* Flexible f-string prompts
* Gemini API integration
* Streamlit interface
* Basic RAG workflow

## Project Structure

```text
Prompt-Engineering/
├── 1.py
├── 2.py
├── 3.py
├── 4.py
├── 5.py
├── 6.py
├── 7.py
├── gemini_prompt.py
├── requirements.txt
└── README.md
```

## Technologies

* Python
* Google Gemini API
* Streamlit
* Prompt Engineering
* Generative AI
* RAG Concepts

## Gemini Application

The Streamlit application accepts a user query, adds retrieved information to the prompt, and sends it to Gemini to generate a response.

## ▶️ Run the Application
python -m streamlit run gemini_prompt.py
## OR
streamlit run gemini_prompt.py

**Workflow:**

```text
User Query
   ↓
Information Retrieval
   ↓
Prompt Augmentation
   ↓
Gemini API
   ↓
Generated Response
```

The retriever in this project is a **demo implementation** and can later be replaced with a vector database, PDF retriever, or knowledge base.

## Conclusion

This project helped me understand how prompts can be created, modified, combined, and used with Generative AI models through Python and Gemini.

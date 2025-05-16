#  Coinbase Learn Chatbot

A lightweight, LLM-powered chatbot that uses Coinbase's Learn content to answer crypto questions in real time — with multilingual support and source links.

---

##  Live Demo
Try it live: **[https://coinbaselearnbot-ivan.streamlit.app/] (https://coinbaselearnbot-ivan.streamlit.app/)**

> *(Deployed on Streamlit Cloud — no setup required)*

---

##  Features
-  Vector search over real Coinbase Learn articles
-  OpenAI-powered Q&A with citations
-  Multilingual output (English, Spanish, French, Bulgarian)
-  Coinbase branding and clean UI
-  Returns sources with clickable links

---

##  How to Run Locally

1. **Clone the repo**:
    ```bash
    git clone https://github.com/your-username/coinbase-chatbot.git
    cd coinbase-chatbot
    ```

2. **Set up the environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\\Scripts\\activate on Windows
    pip install -r requirements.txt
    ```

3. **Add your OpenAI API key**:
    Create a `.env` file in the root:
    ```
    OPENAI_API_KEY=your-openai-api-key
    ```

4. **Run the chatbot**:
    ```bash
    streamlit run app.py
    ```

---

##  Powered By
- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [OpenAI API](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)

---

##  Disclaimer

This tool is for demonstration purposes only. It is **not affiliated with Coinbase**.

---

##  Author

**Ivan Stoyanchev**  
[LinkedIn](https://www.linkedin.com/in/ivanstoyanchev)

© 2025

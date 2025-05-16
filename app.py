'''The user-facing Streamlit app'''
import streamlit as st
from chatbot import ask_question
from langchain_community.chat_models import ChatOpenAI
import os

def translate_output(text, target_lang):
    if target_lang == "en":
        return text
    translator = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
    return translator.invoke(f"Translate this to {target_lang}: {text}").content
st.title("Coinbase Learn Chatbot")

# Language selector
with st.sidebar:
    st.markdown("## 🌐 Language")
    lang = st.selectbox("", ["English", "Spanish", "French", "Bulgarian"])

lang_code_map = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Bulgarian": "bg"
}

user_input = st.text_input("Ask me anything about crypto...")

if user_input:
    with st.spinner("Thinking..."):
        answer, sources = ask_question(user_input)
        translated = translate_output(answer, lang_code_map[lang])
        st.success(translated)

        if sources:
            st.markdown("### 📚 Sources:")
            seen = set()
            for doc in sources:
                url = doc.metadata.get("url")
                if url and url not in seen:
                    seen.add(url)
                    st.markdown(f"- [{url}]({url})")

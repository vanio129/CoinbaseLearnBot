'''Loads the vector DB + defines the Q&A logic'''
import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI


# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = FAISS.load_local("coinbase_index", embedding, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})


qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
    retriever=retriever,
    return_source_documents=True  
)


llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

def ask_question(query):
    retrieved_docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    examples = """Example:
Q: Who created Bitcoin?
A: Coinbase says that Bitcoin was created by an anonymous individual or group known as Satoshi Nakamoto.

Q: What is staking?
A: Coinbase says staking is a way to earn rewards for helping to secure a blockchain network.
"""

    prompt = f"""{examples}
    Context:
    {context}

    Question: {query}
    Answer:"""

    llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)  
    response = llm.invoke(prompt)  
    return response.content, retrieved_docs

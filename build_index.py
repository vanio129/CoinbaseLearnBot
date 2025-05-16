''': Reads JSON, splits it, embeds it, and stores a FAISS index in faiss_index/'''
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import json

with open("data/coinbase_articles.json") as f:
    raw_data = json.load(f)

docs = []
for item in raw_data:
    if item["text"].strip():
        docs.append(Document(page_content=item["text"], metadata={"url": item["url"]}))

# Split into chunks
splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embed & index
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embedding)
vectorstore.save_local("coinbase_index")

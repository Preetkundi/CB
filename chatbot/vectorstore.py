# vectorstore_builder.py
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Load blogs
blogs_folder = "blog_articles"
docs = []

for filename in os.listdir(blogs_folder):
    with open(os.path.join(blogs_folder, filename), "r", encoding="utf-8") as f:
        text = f.read()
        docs.append(Document(page_content=text))

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Create vectorstore
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = FAISS.from_documents(split_docs, embedding=embeddings)

# Save it
vectordb.save_local("faiss_index")
print("✅ Vectorstore saved at faiss_index/")

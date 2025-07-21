import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

# 👇 Dummy content from Jas's videos (replace this with actual blog texts)
docs = [
    Document(page_content="In today's video, we talk about setting healthy boundaries in relationships."),
    Document(page_content="Understanding your inner child can lead to emotional healing."),
    Document(page_content="How to deal with anxiety and stress during exams."),
]

# 👇 Use a specific model (MiniLM is fast + good quality)
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 👇 Create and save the FAISS index
vectordb = FAISS.from_documents(docs, embedding)
vectordb.save_local("faiss_index")

print("✅ FAISS index built and saved to 'faiss_index/'")

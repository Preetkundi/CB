from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_groq import ChatGroq
import os

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
from dotenv import load_dotenv
load_dotenv()


vectordb = FAISS.load_local("faiss_index", embeddings=embedding, allow_dangerous_deserialization=True)

# Load Groq LLM
groq_llm = ChatGroq(model="llama3-8b-8192", temperature=0.4)

def ask_jas_bot(query: str) -> str:
    print("🟣 Received user query:", query)

    # Retrieve top 3 relevant docs with score
    docs_and_scores = vectordb.similarity_search_with_score(query, k=3)
    print("🔍 Retrieved docs with scores:", docs_and_scores)

    if not docs_and_scores or docs_and_scores[0][1] < 0.7:
        return "⚠️ Sorry, I can only assist with queries related to JasThinks videos or philosophy."

    # Only pass if relevance is high enough
    context = "\n".join([doc.page_content for doc, _ in docs_and_scores])
    prompt = f"You are JasThinks AI. Use the context below to answer professionally.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = groq_llm.invoke(prompt)
    return response

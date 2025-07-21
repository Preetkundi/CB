from langchain_groq import ChatGroq
from chatbot.vectorstore import add_document

# Initialize the Groq LLM (adjust model/temperature if needed)
groq_llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)

# Prompt to convert transcript to blog-style content
BLOG_PROMPT_TEMPLATE = """
Convert the following transcript from a therapist's YouTube video into a helpful, professional, and empathetic blog article.

Transcript:
{transcript}

Blog:
"""

def transcript_to_blog(transcript: str) -> str:
    prompt = BLOG_PROMPT_TEMPLATE.format(transcript=transcript)
    response = groq_llm.invoke(prompt)
    return response.content.strip()

def process_and_store_transcript(transcript: str, video_title: str):
    blog_article = transcript_to_blog(transcript)
    metadata = {"source": "YouTube", "title": video_title}
    add_document(blog_article, metadata)
    return blog_article

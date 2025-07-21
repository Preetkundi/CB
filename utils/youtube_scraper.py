from pytube import Channel, YouTube
from utils.transcriber import get_transcript
from chatbot.summarizer import process_and_store_transcript

# Replace this with Jas's actual YouTube channel URL
JAS_CHANNEL_URL = "https://www.youtube.com/@jas_example"

def scrape_and_process_youtube():
    channel = Channel(JAS_CHANNEL_URL)
    print(f"Found {len(channel.video_urls)} videos on Jas's channel.")

    for url in channel.video_urls:
        try:
            yt = YouTube(url)
            title = yt.title
            print(f"Processing video: {title}")
            
            transcript = get_transcript(url)
            if transcript:
                blog = process_and_store_transcript(transcript, title)
                print(f"✅ Processed and stored: {title}")
            else:
                print(f"❌ No transcript found for: {title}")
        except Exception as e:
            print(f"⚠️ Error processing {url}: {e}")

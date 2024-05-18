import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

def get_notes(api_key,video_id):
    try:
        genai.configure(api_key=api_key)
        video_id = video_id.split("=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Extract text from the transcript
        input_text =""
        for i in transcript:
            input_text += i['text'] + " "
        
        # Generate notes from the text
        model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  system_instruction="You are a note generator. You need to convert the given text into some couple of notes and wrap that notes into some HTML tags. Generate only the tags and notes and nothing else.",
)
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        print(e)
        return None
    
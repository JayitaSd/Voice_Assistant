import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
E_API_KEY = os.getenv("ELEVENLABS_API_KEY")
G_API_KEY = os.getenv("GEMINI_API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig
from google import genai
from google.genai import types

gemini_client = genai.Client(api_key=G_API_KEY)

user_name = "Jayita"
schedule = "MPR discussion on Monday at 10:00 AM"
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)

client = ElevenLabs(api_key=E_API_KEY)

def gemini_response(text):
    response = gemini_client.models.generate_content(
        model="gemini-1.5-flash",  # or gemini-1.5-flash
        contents=text
    )
    return response.text.strip()

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")


def print_user_transcript(transcript):
    print(f"User: {transcript}")
    gemini_reply = gemini_response(transcript)
    print(f"Gemini: {gemini_reply}")
    # Speak Gemini's reply
    audio = client.generate(
        text=gemini_reply,
        voice="Rachel",
        model="eleven_multilingual_v2"
    )
    DefaultAudioInterface().play(audio)


conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()
# 🎙️ Voice Assistant with ElevenLabs Conversational AI API

This project demonstrates how to create a **real-time voice assistant** using the [ElevenLabs Conversational AI API](https://elevenlabs.io/).  

The assistant:
- 🎤 Records your voice through the microphone  
- 🖨️ Detects when you finish speaking or interrupt the assistant  
- 🤖 Uses an LLM to generate responses  
- 📈 Synthesizes speech from the response  
- 🔊 Plays the generated speech back through your speakers  

---

## 📦 Features
- Real-time speech recognition  
- Smart voice activity detection (VAD)  
- AI-powered conversational responses  
- Natural, high-quality voice synthesis  
- Instant playback  

---

## 🛠 Architecture

```text
 🎤 Microphone Input
        ↓
 [Voice Activity Detection] --- detects when you finish speaking
        ↓
 [Speech-to-Text] --- converts voice to text
        ↓
 [LLM API Call] --- generates AI response
        ↓
 [Text-to-Speech] --- synthesizes natural voice
        ↓
 🔊 Speaker Output

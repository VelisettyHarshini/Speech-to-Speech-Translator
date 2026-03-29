## 🎤 Real-Time Speech-to-Speech Translation System

This project implements an end-to-end real-time Speech-to-Speech Machine Translation (S2ST) system that enables seamless communication across different languages by converting spoken input into a target language and generating a natural speech response.

The system captures live audio input, processes it through multiple stages including noise reduction, speech recognition, language identification, translation, and speech synthesis, and delivers an intelligible audio output with minimal latency.

---

## 🧠 System Pipeline

Microphone Input → Noise Suppression → Speech Recognition + Language Identification → Translation → Text-to-Speech → Audio Output

---

## ⚙️ Tools and Technologies

- **Audio Capture**: `sounddevice`, `soundfile`  
- **Noise Suppression**: `noisereduce`  
- **Speech Recognition & Language Identification**: `OpenAI Whisper`  
- **Translation Engine**: `deep-translator (Google Translate)`  
- **Text-to-Speech**: `gTTS`  
- **Programming Language**: Python  

---

## 🚀 Key Features

- Supports multilingual speech input  
- Automatic language detection  
- End-to-end speech-to-speech translation  
- Modular and scalable pipeline design  
- Handles real-world noisy environments  

---

## 🎯 Use Cases

- Real-time cross-lingual communication  
- Voice-based translation systems  
- Accessibility tools for regional language users  
- Human-computer interaction in multilingual settings  

---

## 📌 Implementation Note

The current implementation translates speech from multiple languages into a single target language (Telugu), focusing on performance, simplicity, and real-world applicability.

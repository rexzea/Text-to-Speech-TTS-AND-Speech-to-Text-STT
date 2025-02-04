# 🗣️ Python Speech Processing Toolkit

## 📝 Project Description
This tools speech processing toolkit is a solution for converting text to speech and speech to text using Python. The project demonstrates the versatility of speech related libraries by implementing two distinct approaches to text to speech conversion and a robust speech recognition system.

## 🎯 Project Objectives
- Develop a flexible speech processing tool
- Explore multiple text to speech conversion techniques
- Create a user friendly speech recognition system
- Demonstrate practical application of speech processing libraries

## 🚀 Core Features

### Text-to-Speech (TTS) Modules

#### 1. Google Text to Speech (gTTS)
**Advantages:**
- Natural and clear pronunciation
- Supports multiple languages
- High quality voice synthesis
- Easy to use with minimal configuration

**Limitations:**
- Requires active internet connection
- Limited customization options
- Potential usage restrictions
- Dependent on Google service availability

#### 2. PYTTSX3 
**Advantages:**
- Offline functionality
- Works across multiple platforms (Windows, macOS, Linux)
- Uses system installed voices
- No internet connection required
- Lower latency compared to online services

**Limitations:**
- Less natural voice quality
- Limited voice variety
- Platform-dependent voice support
- Potential licensing restrictions for commercial use

### Speech-to-Text (STT) Module
**Library:** `speech_recognition`

**Features:**
- Multiple speech recognition engines support
- Handles various audio input formats
- Robust noise reduction capabilities
- Supports multiple languages

## 📂 Project Structure
```
SpeechTools/
│
├── STT/ (Speech To Text)
│   ├── save/
│   │   ├── audio/     # Stored audio recordings
│   │   └── text/      # Transcribed text history
│   └── STT.py         # Speech-to-text processing script
│
└── TTS/ (Text To Speech)
    ├── Google Speech/
    │   └── gtts_converter.py     # Google TTS converter
    ├── Robotik PYTTSX3/
    │   └── pyttsx3_converter.py  # PYTTSX3 TTS converter
    └── saved_audio/              # Generated audio files storage
```

## 🛠️ Technical Specifications

### Software Requirements
- Python 3.7+
- Operating System: Cross-platform (Windows, macOS, Linux)

### Library Dependencies
- `gtts`: Google Text to Speech conversion
- `pyttsx3`: Offline Text to Speech conversion
- `SpeechRecognition`: Speech to text transcription
- `pyaudio`: Audio input/output handling

### Performance Metrics
- **gTTS**
  - Latency: 1-3 seconds per conversion
  - Language Support: 30+ languages
  - Voice Quality: High

- **PYTTSX3**
  - Latency: <0.5 seconds per conversion
  - Language Support: Depends on system voices
  - Voice Quality: Medium

## 🔧 Installation & Setup
1. Clone the repository
   ```bash
   git clone https://github.com/rexzea/Text-to-Speech-TTS-AND-Speech-to-Text-STT.git
   ```

2. Install dependencies
   ```bash
   pip install gtts pyttsx3 SpeechRecognition pyaudio
   ```

## 📦 Usage Examples

### Text-to-Speech Conversion
This is a simple version of the code!
```python
# Google TTS Example
from gtts import gTTS
tts = gTTS(text='Hello, world!', lang='en')
tts.save('output.mp3')

# PYTTSX3 Example
import pyttsx3
engine = pyttsx3.init()
engine.say('Hello, world!')
engine.runAndWait()
```

### Speech-to-Text Conversion
This is a simple version of the code!
```python
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
```

## 🔮 Future Improvements
- Add more TTS engines
- Implement noise cancellation
- Create a unified interface for TTS and STT
- Enhance language support
- Develop a GUI application

## 🤝 Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License
MIT License

## 📞 Contact
-
```

# AI_CHATBOT--v1

I built this in pycharm.
There are a few error in this code and i will definitely work on them. At present I just started it, in future you might get to see a fully working chatbot with awesome visuals.
Current issues are regarding main.py and the usage of the api keys (they are getting exhasted).

# Snow - AI Voice Assistant

Snow is a Python-based voice assistant that listens to your commands, responds using AI, and can perform quick actions like opening websites or telling the time.  
It uses **OpenAI GPT** or **Google Gemini** for AI responses, along with **speech recognition** and **text-to-speech** capabilities.

---

## ✨ Features
- 🎤 **Voice Input** – Uses your microphone to capture commands.
- 🗣 **Voice Output** – Responds using text-to-speech.
- 🤖 **AI Integration** – Uses OpenAI GPT-3.5 (fallback to Google Gemini if GPT fails).
- 🌐 **Quick Web Access** – Open popular websites like YouTube, Google, Netflix, etc.
- ⏰ **Time Check** – Tells you the current time on request.
- 🔄 **Multi-API Fallback** – Automatically switches to Gemini if OpenAI is unavailable.

---

## 📂 Project Structure
```
.
├── main.py          # Main voice assistant logic
├── ai_handler.py    # Handles AI API requests and fallbacks
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## 🛠 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Krishna-721/snow-ai-assistant.git
cd snow-ai-assistant
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

If `pyaudio` fails to install:
- **Windows**
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```
- **Linux/macOS**
  ```bash
  sudo apt install portaudio19-dev   # Linux
  brew install portaudio             # macOS (with Homebrew)
  ```

---

## 🔑 Environment Variables

Create a `.env` file in the project root with:
```env
OPENAI_API_KEY=your_openai_key1,your_openai_key2
GEMINI_KEY=your_gemini_api_key
```
- You can add multiple OpenAI keys separated by commas (used in case one hits the limit).
- Gemini is optional; used only if OpenAI is unavailable.

---

## 🚀 Usage
Run the assistant:
```bash
python main.py
```

Example commands:
- **"Open YouTube"** → Opens YouTube in browser.
- **"What’s the time?"** → Tells you the current time.
- **"Tell me a joke"** → Gets a funny response from AI.

---

## 📜 requirements.txt
```
openai
google-generativeai
SpeechRecognition
pyttsx3
pyaudio
```

---

## ⚠️ Notes
- Requires an active internet connection for AI responses.
- Microphone access is necessary.
- Works on Windows, macOS, and Linux (with proper audio drivers).

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- [OpenAI](https://openai.com/)
- [Google Generative AI](https://ai.google.dev/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- 

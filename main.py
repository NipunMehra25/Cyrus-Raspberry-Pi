import os
import random
import tempfile
import platform
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from langdetect import detect
import google.generativeai as genai
import winsound

# ───────────────────────────────
# 🔹 Gemini API setup
# ───────────────────────────────
api_keys = [
]

def configure_api():
    genai.configure(api_key=random.choice(api_keys))

# ───────────────────────────────
# 🔹 Initialize
# ───────────────────────────────
recognizer = sr.Recognizer()
convo_history = []

# ───────────────────────────────
# 🔹 Wake words
# ───────────────────────────────
WAKE_WORDS = ["hey cyrus", "hi cyrus", "hey sirus", "hey cyris", "cryus", "hi cry","SRS"]

def is_wake_word(text):
    text = text.lower().strip()
    return any(word in text for word in WAKE_WORDS)

def play_beep():
    if platform.system() == "Windows":
        winsound.Beep(1200, 150)
    else:
        os.system('play -nq -t alsa synth 0.2 sine 1200')

# ───────────────────────────────
# 🔹 Gemini Chat Logic
# ───────────────────────────────
def chat_with_gemini(prompt, lang_hint="en"):
    """Send message to Gemini and get response prefixed with language code."""
    configure_api()
    model = genai.GenerativeModel("gemini-2.0-flash")

    system_prompt = f"""
    You are Cyrus, an intelligent IoT-based AI assistant developed for Raspberry Pi Zero 2 W
    using Google's Gemini API.

    Background:
    - Created by Mr. Nipun, Mr. Naveen, and Mrs. Neha at Chitkara University under Dr. Jyoti.
    - You respect Mr. Nipun Mehra greatly and always stay polite.

    Guidelines:
    - Detect the user’s language from context or the given hint.
    - Always reply in the same language.
    - Prefix response with:
        'en:' for English
        'hi:' for Hindi
        'pa:' for Punjabi
    - Example:
        User: What is AI?
        Cyrus: en: Artificial Intelligence is the ability of machines to think.

        User: भारत की राजधानी क्या है?
        Cyrus: hi: भारत की राजधानी नई दिल्ली है।

        User: ਪੰਜਾਬ ਦੀ ਰਾਜਧਾਨੀ ਕੀ ਹੈ?
        Cyrus: pa: ਪੰਜਾਬ ਦੀ ਰਾਜਧਾਨੀ ਚੰਡੀਗੜ੍ਹ ਹੈ।

    - Be concise, clear, and respectful.
    - Avoid extra prefixes or greetings.
    - Maintain professionalism.

    Language hint: {lang_hint}
    Recent conversation:
    {chr(10).join(convo_history[-5:])}

    User: {prompt}
    """

    response = model.generate_content(system_prompt, generation_config={"temperature": 0.3})
    answer = response.text.strip()
    convo_history.append(f"User: {prompt}")
    convo_history.append(f"Cyrus: {answer}")
    return answer

# ───────────────────────────────
# 🔹 Text-to-speech
# ───────────────────────────────
def speak(response):
    """Speak response in correct language (en, hi, pa)."""
    try:
        response = response.replace("Cyrus:", "").strip()

        # Extract language code
        if ":" in response:
            lang_code, text = response.split(":", 1)
            lang_code, text = lang_code.strip().lower(), text.strip()
        else:
            lang_code, text = "en", response

        if lang_code not in ["en", "hi", "pa"]:
            lang_code = "en"

        print(f"Cyrus says ({lang_code}): {text}")

        # Faster voice by saving once
        tts = gTTS(text=text, lang=lang_code, slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            path = fp.name
        tts.save(path)

        if platform.system() == "Windows":
            playsound(path)
        else:
            os.system(f"mpg123 {path} >/dev/null 2>&1")

        os.remove(path)
    except Exception as e:
        print(f"Speech error: {e}")

# ───────────────────────────────
# 🔹 Language detection helper
# ───────────────────────────────
def detect_language(text):
    try:
        lang = detect(text)
        if lang.startswith("hi"):
            return "hi"
        elif lang.startswith("pa"):
            return "pa"
        else:
            return "en"
    except:
        return "en"

# ───────────────────────────────
# 🔹 Main Loop
# ───────────────────────────────
startup_message = (
    "en: Cyrus has woken up. "
    "To talk to me, say 'Hey Cyrus' and wait for the beep. "
    "Then ask your question in English, Hindi, or Punjabi."
)
speak(startup_message)
print("🎧 Cyrus is listening... Say 'Hey Cyrus' to trigger.")

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("Listening for wake word...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", text)

        if is_wake_word(text):
            print("🔔 Wake word detected!")
            play_beep()

            print("🎤 Listening for your command...")
            with sr.Microphone() as source2:
                recognizer.adjust_for_ambient_noise(source2, duration=0.3)
                command_audio = recognizer.listen(source2)

            try:
                command_text = recognizer.recognize_google(command_audio, language="en-IN")
                print("Command:", command_text)

                # Detect spoken language
                detected_lang = detect_language(command_text)
                print(f"🌐 Detected language: {detected_lang}")

                response = chat_with_gemini(command_text, lang_hint=detected_lang)
                speak(response)

            except sr.UnknownValueError:
                print("❌ Could not understand the command.")
    except sr.UnknownValueError:
        pass

# 🎙️ Cyrus - Your Personal Voice Assistant

**Talk to your computer in English, Hindi, or Punjabi!**

Created by **Nipun Mehra**

---

## 🌟 What is Cyrus?

Cyrus is a voice assistant that you can talk to. Just say "Hey Cyrus" and ask any question. It will reply back to you in your language!

**Works on:**
- 💻 Windows computers
- 🥧 Raspberry Pi

---

## 📦 Installation Guide

Choose your device and follow the steps carefully:

- [🪟 Windows Installation](#-windows-installation-step-by-step)
- [🥧 Raspberry Pi Installation](#-raspberry-pi-installation-step-by-step)

---

# 🪟 Windows Installation (Step by Step)

## Step 1: Install Python

**What is Python?** It's a programming language that Cyrus needs to run.

### 1.1 Download Python

1. Open your web browser (Chrome, Edge, Firefox, etc.)
2. Go to: **https://www.python.org/downloads/**
3. You'll see a big yellow button that says **"Download Python 3.x.x"**
4. Click that button
5. Wait for the file to download (it's about 25 MB)

### 1.2 Install Python

1. Find the downloaded file (usually in your "Downloads" folder)
2. The file name will be like `python-3.12.0-amd64.exe`
3. **Double-click** on it
4. **IMPORTANT:** Check the box that says **"Add Python to PATH"** ✅ (This is very important!)
5. Click **"Install Now"**
6. Wait 2-3 minutes for installation
7. When done, click **"Close"**

### 1.3 Verify Python Installation

1. Press **Windows Key + R** on your keyboard
2. Type `cmd` and press **Enter**
3. A black window will open (this is called Command Prompt)
4. Type: `python --version`
5. Press **Enter**
6. You should see something like: `Python 3.12.0`
7. ✅ If you see this, Python is installed correctly!
8. ❌ If you see an error, restart your computer and try again

---

## Step 2: Install Git (To Download Cyrus)

**What is Git?** It's a tool to download code from the internet.

### 2.1 Download Git

1. Go to: **https://git-scm.com/download/win**
2. Click **"Click here to download"**
3. Wait for download (about 50 MB)

### 2.2 Install Git

1. Find the downloaded file `Git-x.xx.x-64-bit.exe`
2. Double-click it
3. Keep clicking **"Next"** until installation starts
4. Wait 2-3 minutes
5. Click **"Finish"**

---

## Step 3: Install PyAudio (For Microphone)

**What is PyAudio?** It lets Python use your microphone.

### 3.1 Open Command Prompt

1. Press **Windows Key + R**
2. Type `cmd`
3. Press **Enter**

### 3.2 Install pipwin (Helper tool)

In the black window (Command Prompt), type exactly:

```
pip install pipwin
```

Press **Enter** and wait 30 seconds.

### 3.3 Install PyAudio

Now type:

```
pipwin install pyaudio
```

Press **Enter** and wait 1 minute.

✅ When it finishes, you should see "Successfully installed pyaudio"

---

## Step 4: Get Google Gemini API Key

**What is an API Key?** It's like a password that lets Cyrus talk to Google's AI.

### 4.1 Create Google Account (Skip if you have one)

1. Go to **https://accounts.google.com**
2. Click **"Create account"**
3. Follow the steps
4. ✅ Remember your email and password!

### 4.2 Get Your FREE API Key

1. Go to: **https://makersuite.google.com/app/apikey**
2. Sign in with your Google account
3. Click the blue button **"Create API Key"**
4. Click **"Create API key in new project"**
5. Wait 5-10 seconds
6. You'll see a long text like: `AIzaSyDxxxxxxxxxxxxxxxxxxxxx`
7. Click the **"Copy"** button 📋
8. **IMPORTANT:** Paste this somewhere safe (Notepad, your phone, etc.)
9. ✅ This is your API key! Don't share it with anyone!

---

## Step 5: Download Cyrus

### 5.1 Create a Folder

1. Open **File Explorer** (folder icon on taskbar)
2. Go to your **Desktop** (or anywhere you want)
3. Right-click on empty space
4. Choose **New → Folder**
5. Name it: `Cyrus`
6. Double-click to open it

### 5.2 Open Command Prompt in This Folder

1. Inside the Cyrus folder, click on the **address bar** at the top
2. Type `cmd` and press **Enter**
3. A black window will open

### 5.3 Download Cyrus Code

In the Command Prompt, type:

```
git clone https://github.com/yourusername/cyrus-voice-assistant.git
```

Press **Enter** and wait 10-20 seconds.

### 5.4 Go Into Cyrus Folder

Type:

```
cd cyrus-voice-assistant
```

Press **Enter**.

---

## Step 6: Install Cyrus Dependencies

**What are dependencies?** Other small programs that Cyrus needs.

### 6.1 Create requirements.txt File

1. In the Cyrus folder, right-click
2. Choose **New → Text Document**
3. Name it: `requirements.txt` (delete the .txt at the end if you see it)
4. Double-click to open it
5. Copy and paste this EXACTLY:

```
SpeechRecognition==3.10.0
gTTS==2.4.0
playsound==1.3.0
langdetect==1.0.9
google-generativeai==0.3.0
```

6. Press **Ctrl + S** to save
7. Close Notepad

### 6.2 Install Everything

In Command Prompt (black window), type:

```
pip install -r requirements.txt
```

Press **Enter** and wait 2-3 minutes. You'll see lots of text scrolling.

✅ When done, you'll see "Successfully installed..."

---

## Step 7: Add Your API Key to Cyrus

### 7.1 Open cyrus.py File

1. In your Cyrus folder, find `cyrus.py`
2. Right-click on it
3. Choose **"Edit with Notepad"** or **"Open with → Notepad"**

### 7.2 Replace API Keys

1. Look for **lines 14-17** (they look like this):

```python
api_keys = [
]
```

2. **Delete** those two long text strings starting with "AIza..."
3. Paste **YOUR** API key (the one you copied in Step 4)
4. It should look like:

```python
api_keys = [
    "AIzaSyD-YOUR-ACTUAL-KEY-HERE"
]
```

5. Press **Ctrl + S** to save
6. Close Notepad

---

## Step 8: Setup Microphone

### 8.1 Check Microphone

1. Click **Start Menu** (Windows icon)
2. Type: `sound settings`
3. Press **Enter**
4. Click **"Sound Control Panel"** on the right
5. Go to **"Recording"** tab
6. You should see **"Microphone"**
7. Right-click on it → **"Set as Default Device"**
8. Click **"OK"**

### 8.2 Test Microphone

1. Click **Start Menu**
2. Type: `voice recorder`
3. Open the **Voice Recorder** app
4. Click the microphone button
5. Say: "Testing one two three"
6. Click stop
7. Play it back
8. ✅ If you hear yourself, microphone works!

---

## Step 9: RUN CYRUS! 🎉

### 9.1 Open Command Prompt in Cyrus Folder

1. Go to your Cyrus folder
2. Click the address bar at top
3. Type `cmd`
4. Press **Enter**

### 9.2 Start Cyrus

Type:

```
python cyrus.py
```

Press **Enter**.

### 9.3 Talk to Cyrus!

1. Wait 5-10 seconds
2. You'll hear: "Cyrus has woken up..."
3. Say clearly: **"Hey Cyrus"**
4. Wait for the **BEEP** sound 🔔
5. Now ask your question! For example:
   - "What is artificial intelligence?"
   - "Tell me a joke"
   - "क्या तुम हिंदी बोल सकते हो?" (Hindi)
   - "ਪੰਜਾਬੀ ਬੋਲੋ" (Punjabi)

6. Cyrus will answer you! 🎉

### 9.4 Stop Cyrus

Press **Ctrl + C** in the Command Prompt window.

---

# 🥧 Raspberry Pi Installation (Step by Step)

## Before You Start

**You need:**
- 🥧 Raspberry Pi (Zero 2 W, 3, or 4)
- 🎤 USB Microphone
- 🔊 Speaker or headphones (3.5mm or USB)
- 💻 Monitor, keyboard, and mouse connected to Pi
- 🌐 Internet connection (WiFi or Ethernet)

---

## Step 1: Setup Your Raspberry Pi

### 1.1 Install Raspberry Pi OS (If not already installed)

1. Download **Raspberry Pi Imager** on another computer: https://www.raspberrypi.com/software/
2. Insert SD card (at least 16GB)
3. Open Raspberry Pi Imager
4. Click **"Choose OS"** → **"Raspberry Pi OS (32-bit)"**
5. Click **"Choose Storage"** → Select your SD card
6. Click **"Write"**
7. Wait 10-15 minutes
8. Insert SD card into Raspberry Pi
9. Connect power, monitor, keyboard, mouse
10. Turn on Raspberry Pi
11. Follow on-screen setup (country, WiFi, password)

### 1.2 Update Raspberry Pi

1. Click the **terminal** icon (black box at top)
2. A window will open
3. Type exactly:

```bash
sudo apt-get update
```

4. Press **Enter**
5. Enter your password if asked
6. Wait 2-3 minutes (you'll see lots of text)

7. Now type:

```bash
sudo apt-get upgrade -y
```

8. Press **Enter**
9. Wait 5-10 minutes (it's updating everything)
10. ✅ When done, you'll see the command prompt again

---

## Step 2: Install Required Software

### 2.1 Install Audio Tools

In terminal, type:

```bash
sudo apt-get install -y python3-pip portaudio19-dev mpg123 alsa-utils
```

Press **Enter** and wait 2-3 minutes.

### 2.2 Install PyAudio

Type:

```bash
pip3 install pyaudio
```

Press **Enter** and wait 1-2 minutes.

---

## Step 3: Setup Audio Devices

### 3.1 Connect Your Microphone and Speaker

1. Plug USB microphone into Raspberry Pi
2. Plug speaker into 3.5mm jack (or USB)

### 3.2 Find Your Audio Devices

Type:

```bash
arecord -l
```

Press **Enter**.

You'll see something like:

```
card 1: Device [USB Audio Device], device 0: USB Audio [USB Audio]
```

**Remember the card number** (in this example, it's **1**)

Type:

```bash
aplay -l
```

Press **Enter**.

Again, **remember the card number** for your speaker.

### 3.3 Set Default Audio Device

Type:

```bash
nano ~/.asoundrc
```

Press **Enter**.

An editor will open. Type exactly (replace **1** with your card number):

```
pcm.!default {
    type hw
    card 1
}

ctl.!default {
    type hw
    card 1
}
```

Press **Ctrl + X**, then **Y**, then **Enter** to save.

### 3.4 Test Microphone

Type:

```bash
arecord -d 3 test.wav
```

Press **Enter** and speak for 3 seconds.

Now play it back:

```bash
aplay test.wav
```

✅ If you hear yourself, it works!

❌ If not, check connections and try different card numbers.

---

## Step 4: Install Git

Type:

```bash
sudo apt-get install -y git
```

Press **Enter** and wait 1 minute.

---

## Step 5: Get Google Gemini API Key

### 5.1 Open Web Browser on Raspberry Pi

1. Click the **globe icon** at top (Chromium browser)
2. Go to: **https://makersuite.google.com/app/apikey**
3. Sign in with Google account
4. Click **"Create API Key"**
5. Click **"Create API key in new project"**
6. **Copy** the long text (starts with AIza...)
7. **Write it down** or save it somewhere

---

## Step 6: Download Cyrus

### 6.1 Create Folder

In terminal, type:

```bash
cd ~
```

Press **Enter**.

Type:

```bash
mkdir cyrus-assistant
```

Press **Enter**.

Type:

```bash
cd cyrus-assistant
```

Press **Enter**.

### 6.2 Download Cyrus Code

Type:

```bash
git clone https://github.com/yourusername/cyrus-voice-assistant.git
```

Press **Enter** and wait 10-20 seconds.

Type:

```bash
cd cyrus-voice-assistant
```

Press **Enter**.

---

## Step 7: Install Dependencies

### 7.1 Create requirements.txt

Type:

```bash
nano requirements.txt
```

Press **Enter**.

Copy and paste this:

```
SpeechRecognition==3.10.0
gTTS==2.4.0
playsound==1.3.0
langdetect==1.0.9
google-generativeai==0.3.0
```

Press **Ctrl + X**, then **Y**, then **Enter**.

### 7.2 Install Everything

Type:

```bash
pip3 install -r requirements.txt
```

Press **Enter** and wait 3-5 minutes.

---

## Step 8: Add Your API Key

### 8.1 Open cyrus.py

Type:

```bash
nano cyrus.py
```

Press **Enter**.

### 8.2 Find the API Keys Section

Use **arrow keys** to go to lines 14-17.

You'll see:

```python
api_keys = [

]
```

### 8.3 Replace with Your Key

1. Delete those two long strings
2. Type your API key (the one from Step 5)
3. Should look like:

```python
api_keys = [
    "AIzaSyD-YOUR-KEY-HERE"
]
```

Press **Ctrl + X**, then **Y**, then **Enter** to save.

---

## Step 9: RUN CYRUS! 🎉

### 9.1 Start Cyrus

Type:

```bash
python3 cyrus.py
```

Press **Enter**.

### 9.2 Talk to Cyrus!

1. Wait 5-10 seconds
2. You'll hear: "Cyrus has woken up..."
3. Say clearly: **"Hey Cyrus"**
4. Wait for **BEEP** 🔔
5. Ask your question!

Example:
- "What is the weather?"
- "Tell me about Raspberry Pi"
- "भारत की राजधानी क्या है?"

6. Cyrus will reply! 🎉

### 9.3 Stop Cyrus

Press **Ctrl + C**.

---

## 🎯 Make Cyrus Start Automatically (Advanced)

If you want Cyrus to start when Raspberry Pi boots:

### Step 1: Create Service File

Type:

```bash
sudo nano /etc/systemd/system/cyrus.service
```

### Step 2: Add This Content

```
[Unit]
Description=Cyrus Voice Assistant
After=network.target sound.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/cyrus-assistant/cyrus-voice-assistant
ExecStart=/usr/bin/python3 /home/pi/cyrus-assistant/cyrus-voice-assistant/cyrus.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Press **Ctrl + X**, **Y**, **Enter**.

### Step 3: Enable Service

Type:

```bash
sudo systemctl enable cyrus.service
sudo systemctl start cyrus.service
```

Now Cyrus starts automatically! ✅

---

## ❓ Common Problems and Solutions

### Problem 1: "python not found" or "python3 not found"

**Solution:**
- Make sure you completed Step 1
- Restart your computer/Pi
- Try: `python3 --version` instead of `python --version`

### Problem 2: Microphone not working

**Windows:**
- Go to Settings → Privacy → Microphone
- Turn ON microphone access
- Make sure your app can use microphone

**Raspberry Pi:**
```bash
amixer set Mic 100%
```

### Problem 3: "No module named 'speech_recognition'"

**Solution:**
```bash
pip install SpeechRecognition
```
or
```bash
pip3 install SpeechRecognition
```

### Problem 4: API Error

**Solution:**
- Check your internet connection
- Make sure API key is correct
- Go to https://makersuite.google.com and check if API is enabled

### Problem 5: Cyrus doesn't hear wake word

**Solution:**
- Speak louder
- Get closer to microphone (6-12 inches)
- Check if microphone is working (test in Step 8 for Windows, Step 3.4 for Pi)

### Problem 6: No sound output

**Windows:**
- Check volume is not muted
- Right-click speaker icon → Open Sound settings

**Raspberry Pi:**
```bash
amixer set PCM 100%
```

---

## 📞 Need More Help?

1. Read error messages carefully
2. Google the exact error message
3. Check if all steps were followed
4. Make sure microphone and speakers are connected
5. Restart computer/Raspberry Pi

---

## 📝 Quick Checklist

Before running Cyrus, make sure:

- ✅ Python is installed
- ✅ Git is installed
- ✅ All requirements installed (requirements.txt)
- ✅ API key is added to cyrus.py
- ✅ Microphone is connected and working
- ✅ Speakers are connected
- ✅ Internet is connected

---

## 🎉 Success!

If Cyrus is responding to you, congratulations! You did it! 🎊

Now you can:
- Ask questions in English, Hindi, or Punjabi
- Learn about anything
- Have conversations with AI
- Show off to your friends!

---

**Created with ❤️ by Nipun Mehra**

⭐ If this helped you, star the repository on GitHub!

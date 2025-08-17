import sys
import webbrowser

# Try to import speech + TTS libraries, but allow fallback if not available
try:
    import speech_recognition as sr
    import pyttsx3
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    VOICE_MODE = True
except Exception as e:
    print("Voice features not available on this platform:", e)
    VOICE_MODE = False

def speak(text):
    if VOICE_MODE:
        engine.say(text)
        engine.runAndWait()
    else:
        print("Jarvis says:", text)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "exit" in c.lower() or "stop" in c.lower():
        speak("Goodbye!")
        sys.exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    if VOICE_MODE:
        # Local mode (Windows, with microphone + TTS)
        while True:
            print("Listening for wake word 'Jarvis'...")
            try:
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

                if "jarvis" in word.lower():
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Jarvis is active. Listening for command...")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

            except Exception as e:
                print("Error:", e)
                speak("Sorry, I didn't catch that.")
    else:
        # Netlify-safe fallback (no microphone/audio)
        # Simple command loop via text input
        while True:
            command = input("Type a command for Jarvis: ")
            processCommand(command)


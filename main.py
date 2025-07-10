import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
        exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
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

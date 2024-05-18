"""Task 2:- Build a simple chatbot that responds to user inputs based on
predefined rules. Use if-else statements or pattern matching
techniques to identify user queries and provide appropriate
responses. This will give you a basic understanding of natural
language processing and conversation flow --- Kirti Murge"""
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

def listen_to_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get you.")
    except sr.RequestError as e:
        print(f"Error occurred during speech recognition: {e}")
    return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wikipedia():
    wiki_wiki = wikipedia.wikipedia('en')
    page = wiki_wiki.page()

    if not page.exists():
        return None

    summary = page.summary[:500]  # Limit summary to 500 characters
    return summary

def page_details():
    wiki_wiki = wikipedia().Wikipedia('en')
    page = wiki_wiki.page()

    if not page.exists():
        return None

    return page.text


def jarvis():
    speak("Hello Kirti I am Jarvis. How can I assist you?")

    while True:
        user_input = listen_to_microphone()

        if user_input is not None:
            if "hello" in user_input:
                speak("Hello! How can I help you?")
            elif "what is your name" in user_input:
                speak("I am Jarvis, your personal AI assistant.")
            elif "what's your name" in user_input:
                speak("I am Jarvis, your personal AI assistant.")
            elif "wikipedia" in user_input:
                query = user_input.replace("wikipedia", "").strip()
                result = wikipedia(query)

                if result is not None:
                    speak(f"Here is the summary from Wikipedia: {result}")
                else:
                    speak("I'm sorry, I couldn't find information on that topic.")
            elif "who is your owner " in user_input:
                speak("I am created by Kirti Murge")

            elif "time" in user_input:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}.")

                pass
            elif "weather" in user_input:
                speak("It is raining today")
                # Implement code to fetch and speak the current weather.
                # You can use weather APIs like OpenWeatherMap for this purpose.
                pass
            elif "bye" in user_input:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't have a response for that.")

if __name__ == "__main__":
    jarvis()





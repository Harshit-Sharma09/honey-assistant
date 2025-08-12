#program to listen 

import speech_recognition as sr                                                           #for listning 

try:
    recognizer = sr.Recognizer()

    def listening():   
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio=recognizer.listen(source,timeout=10,phrase_time_limit=10)
            text_detected=recognizer.recognize_google(audio, language="en-IN")
            text=text_detected.upper()
            print(text)
        return text
    
except Exception as e:
    print(e)
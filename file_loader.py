from edza_req import *
import os


def chat_mode():
    kernel = aiml.Kernel()
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles="brnld.xml", commands="load edza brain")
        kernel.saveBrain("bot_brain.brn")

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 10.0)

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Tell me something:")
            audio = r.listen(source)
            try:
                print("You said:- " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
                chat_mode()
        rep = kernel.respond(r.recognize_google(audio))
        print(rep)

        engine.say(rep)
        engine.runAndWait()
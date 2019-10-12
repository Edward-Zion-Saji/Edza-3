#@title Apache 2.0 License
#
# Copyright (c) 2019 Edward Zion Saji
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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

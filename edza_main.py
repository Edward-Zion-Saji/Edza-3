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

import wx.adv
from edza_web import *
from edza_req import *


class MyPanel(wx.Panel):

    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")

        gif_fname = wx.adv.Animation("imgs/edza_face.gif")
        global gif
        gif = wx.adv.AnimationCtrl(self, id, gif_fname, pos=(1, 1))
        gif.GetAnimation()
        self.gif = gif
        self.Show()
        self.conwin = wx.TextCtrl(self, id=wx.ID_ANY, value="Hi, How May I Help You.", pos=(500, 130),
                                  size=(400, 200),
                                  style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CENTER | wx.BORDER_NONE)
        f1 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Lucida Sans')
        self.conwin.SetFont(f1)
        self.hinwin = wx.TextCtrl(self, id=wx.ID_ANY, value="   ", pos=(500, 330),
                                  size=(400, 20), style=wx.TE_READONLY | wx.BORDER_NONE | wx.TE_CENTER)
        self.hinwin.SetFont(f1)
        bmp = wx.Bitmap("imgs/microphone (1).png", wx.BITMAP_TYPE_ANY)
        self.button = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                                      size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10), pos=(500, 400))
        self.button.Bind(wx.EVT_BUTTON, self.on_button)
        bmp2 = wx.Bitmap("imgs/git.png", wx.BITMAP_TYPE_ANY)
        self.button2 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp2,
                                       size=(32, 32), pos=(950, 527))
        self.button2.Bind(wx.EVT_BUTTON, self.on_button)
        self.lbl = wx.StaticText(self, label="   Chat", pos=(500, 445),
                                 size=(40, 32))
        bmp3 = wx.Bitmap("imgs/search.png", wx.BITMAP_TYPE_ANY)
        self.but_fact = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp3,
                                        size=(42, 42), pos=(625, 400))
        self.but_fact.Bind(wx.EVT_BUTTON, self.on_fact)
        self.lbl2 = wx.StaticText(self, label="Fact Search", pos=(615, 445),
                                  size=(70, 32))
        bmp6 = wx.Bitmap("imgs/google.png", wx.BITMAP_TYPE_ANY)
        self.button6 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp6,
                                       size=(42, 42), pos=(745, 400))
        self.button6.Bind(wx.EVT_BUTTON, self.on_google)
        self.lbl3 = wx.StaticText(self, label="Google Search", pos=(725, 445),
                                  size=(80, 32))
        bmp7 = wx.Bitmap("imgs/wikipedia.png", wx.BITMAP_TYPE_ANY)
        self.button7 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp7,
                                       size=(42, 42), pos=(855, 400))
        self.button7.Bind(wx.EVT_BUTTON, self.on_wiki)
        self.lbl4 = wx.StaticText(self, label="Wikipedia", pos=(850, 445),
                                  size=(70, 32))
        bmp4 = wx.Bitmap("imgs/twitter.png", wx.BITMAP_TYPE_ANY)
        self.button4 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp4,
                                       size=(32, 32), pos=(918, 527))
        self.button4.Bind(wx.EVT_BUTTON, self.on_button)
        bmp5 = wx.Bitmap("imgs/facebook.png", wx.BITMAP_TYPE_ANY)
        self.button5 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp5,
                                       size=(32, 32), pos=(886, 527))
        self.button5.Bind(wx.EVT_BUTTON, self.on_button)
        bmp8 = wx.Bitmap("imgs/icons8-mind-map-96.png", wx.BITMAP_TYPE_ANY)
        wx.StaticBitmap(self, -1, bmp8, (880, 0), (bmp8.GetWidth(), bmp8.GetHeight()))
        bmp9 = wx.Bitmap("imgs/logotext.png", wx.BITMAP_TYPE_ANY)
        wx.StaticBitmap(self, -1, bmp9, (790, 30), (bmp9.GetWidth(), bmp9.GetHeight()))

        global engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 10.0)
        global kernel
        kernel = aiml.Kernel()
        if os.path.isfile("bot_brain.brn"):
            kernel.bootstrap(brainFile="bot_brain.brn")
        else:
            kernel.bootstrap(learnFiles="brnld.xml", commands="load edza brain")
            kernel.saveBrain("bot_brain.brn")

    def on_button(self, event):

        def chat_class():

            while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    winsound.Beep(500, 500)
                    r.adjust_for_ambient_noise(source)
                    self.hinwin.SetValue("   ")
                    self.hinwin.AppendText("Listening...")
                    audio = r.listen(source)
                    winsound.Beep(500, 250)
                    winsound.Beep(700, 250)
                    try:
                        self.hinwin.SetValue("  ")
                        self.conwin.AppendText("\n\nYou:    " + r.recognize_google(audio))
                    except sr.UnknownValueError:
                        self.hinwin.AppendText("Sorry, I didn't get you.")
                        chat_class()
                rep = kernel.respond(r.recognize_google(audio))
                self.conwin.AppendText("\n\n" + rep)
                self.gif.Play()
                engine.say(rep)
                engine.runAndWait()
                self.gif.Play()

        chat_class()

    def on_wiki(self, event):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            winsound.Beep(500, 500)
            r.adjust_for_ambient_noise(source)
            self.hinwin.SetValue("   ")
            self.hinwin.AppendText("Listening...")
            audio = r.listen(source)
            winsound.Beep(500, 250)
            winsound.Beep(700, 250)
            try:
                self.hinwin.SetValue("  ")
                self.conwin.AppendText("\n\nYou:    " + r.recognize_google(audio))
            except sr.UnknownValueError:
                self.hinwin.AppendText("Sorry, I didn't get you. Please try again")
        wiki_dat = wikipedia.summary(r.recognize_google(audio))
        self.conwin.AppendText("\n\n" + wiki_dat)
        self.gif.Play()
        engine.say(wiki_dat)
        engine.runAndWait()
        self.gif.Stop()

    def on_fact(self, event):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            winsound.Beep(500, 500)
            r.adjust_for_ambient_noise(source)
            self.hinwin.SetValue("   ")
            self.hinwin.AppendText("Listening...")
            audio = r.listen(source)
            winsound.Beep(500, 250)
            winsound.Beep(700, 250)
            try:
                self.hinwin.SetValue("  ")
                self.conwin.AppendText("\n\nYou:    " + r.recognize_google(audio))
            except sr.UnknownValueError:
                self.hinwin.AppendText("Sorry, I didn't get you. Please repeat that again")
                pass
        app_id = "GJRQVK-GY36XW7K8H"
        client = wolframalpha.Client(app_id)
        res = client.query(r.recognize_google(audio))
        answer = next(res.results).text
        self.conwin.AppendText("\n\n" + answer)
        self.gif.Play()
        engine.say(answer)
        engine.runAndWait()
        self.gif.Stop()

    def on_google(self, event):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            winsound.Beep(500, 500)
            r.adjust_for_ambient_noise(source)
            self.hinwin.SetValue("   ")
            self.hinwin.AppendText("Listening...")
            audio = r.listen(source)
            winsound.Beep(500, 250)
            winsound.Beep(700, 250)
            try:
                self.hinwin.SetValue("  ")
                self.conwin.AppendText("\n\nYou:    " + r.recognize_google(audio))
            except sr.UnknownValueError:
                self.hinwin.AppendText("Sorry, I didn't get you. Please repeat that again")
                pass
        if __name__ == '__main__':
            app = wx.App()
            dialog = MyBrowser(None, -1)
            req = "https://google.co.in/search?q=" + r.recognize_google(audio)
            dialog.browser.LoadURL(req)
            dialog.Show()
            app.MainLoop()


def splash_scr():
    bitmap = wx.Bitmap('imgs/splash_screen.png')
    splash = wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTER_ON_SCREEN | wx.adv.SPLASH_NO_TIMEOUT, 0, None, -1)
    splash.Show()
    return splash


if __name__ == "__main__":
    app = wx.App()
    splashsc = splash_scr()
    frame = wx.Frame(None,
                     pos=wx.DefaultPosition, size=wx.Size(1000, 600),
                     style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.HELP |
                     wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                     title="Edza 3.0")
    frame.SetIcon(wx.Icon("imgs/icons8-mind-map-48.ico"))
    MyPanel(frame, -1)
    frame.Show(True)
    splashsc.Destroy()
    app.MainLoop()

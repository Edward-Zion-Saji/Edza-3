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

import wx
import wx.html2
import wx.html


class MyBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle('Edza-Web')
        self.SetIcon(wx.Icon("imgs/icons8-mind-map-48.ico"))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        # Element Variables
        self.browser = wx.html2.WebView.New(self)
        self.address = wx.TextCtrl(self, value="", size=(500, 26))
        self.go = wx.Button(self, label="Go", id=wx.ID_OK)
        self.back = wx.Button(self, label="Back")
        self.forward = wx.Button(self, label="Forward")
        self.reload = wx.Button(self, label="Refresh")
        self.result = None
        # Nav area
        addressarea = wx.BoxSizer()
        addressarea.Add(self.address, proportion=1, border=0)
        addressarea.Add(self.go, proportion=0, border=0)
        addressarea.Add(self.back, proportion=0, border=0)
        addressarea.Add(self.forward, proportion=0, border=0)
        addressarea.Add(self.reload, proportion=0, border=0)
        # adding elements
        sizer.Add(addressarea, proportion=0, flag=wx.EXPAND, border=0)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        # button binding
        self.Bind(wx.EVT_BUTTON, self.OnGo, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.OnBack, self.back)
        self.Bind(wx.EVT_BUTTON, self.OnForward, self.forward)
        self.Bind(wx.EVT_BUTTON, self.OnReload, self.reload)
        # menu bar stuff
        # File Menu
        self.fileMenu = wx.Menu()
        self.New = self.fileMenu.Append(wx.ID_ANY, 'New Window')
        self.Exit = self.fileMenu.Append(wx.ID_ANY, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnNew, self.New)
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, self.Exit)
        # Help Menu
        self.helpMenu = wx.Menu()
        self.Help = self.helpMenu.Append(wx.ID_ANY, 'Help')
        self.About = self.helpMenu.Append(wx.ID_ANY, 'About')
        self.Bind(wx.EVT_MENU, self.OnHelp, self.Help)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.About)
        # Adding the actual Menu Bar
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, 'File')
        self.menuBar.Append(self.helpMenu, 'Help')
        self.SetMenuBar(self.menuBar)

        self.SetSizer(sizer)
        self.SetSize((1000, 700))

    def OnBack(self, event):
        self.browser.GoBack()

    def OnForward(self, event):
        self.browser.GoForward()

    def OnGo(self, event):
        self.result = self.address.GetValue()
        self.browser.LoadURL(self.result)

    def OnReload(self, event):
        self.browser.Reload()

    def OnNew(self, event):
        if __name__ == '__main__':
            app = wx.App()
            dialog = MyBrowser(None, -1)
            dialog.browser.LoadURL("http://www.google.com")
            dialog.Show()
            app.MainLoop()

    def OnHelp(self, event):
        helpDlg = HelpDlg(None)
        helpDlg.Show()

    def OnAbout(self, event):
        aboutDlg = AboutDlg(None)
        aboutDlg.Show()

    def OnCloseWindow(self, e):
        self.Destroy()


# About Menu Dialog HTMl Style
class AboutDlg(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400, 400))

        html = wxHTML(self)

        html.SetPage(

            "<h2>Edza-Web</h2>"

            '<p>WxPython is the GUI back end that runs this program</p>'

            '<p>Python is the programing language of this program and browser is the functions of this program.</p>'
            '<p>Created by Edward Zion Saji</p>'
            '<p>This software is free to use, but please give credit when credit is due(simply mention the parts you used and my name and your good)</p>'
        )


class HelpDlg(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400, 400))

        html = wxHTML(self)

        html.SetPage(
            ''

            "<h2>Edza-Web Help</h2>"

            "<p>Thanks for trying out this web browser, It's nothing big yet, but we can dream right?"

            "<p>Not much to be said about usage as it pretty self explanatory if you ever use a computer.</p>"

            "<p>Go to any site by typing in the address and pressing go.</p>"

            '<p>Thank\'s for using my program!</p>'
        )


class wxHTML(wx.html.HtmlWindow):
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())


if __name__ == '__main__':
    app = wx.App()
    dialog = MyBrowser(None, -1)
    dialog.browser.LoadURL("http://www.google.com")
    dialog.Show()
    app.MainLoop()

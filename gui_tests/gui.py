# version 0.1
import tkinter as tk
import webbrowser
# Globals
appName = "cleaningTest"
repository = "http://www.github.com/Wauro21/cleaningTest"
class Welcomewindow:
    window = None
    frm_top = None
    #mid = None
    #bot = None
    def openRepo(self):
        #global repository
        webbrowser.open_new_tab(repository)

    def __init__(self):
        global appName
        self.window = tk.Tk()
        self.window.title(appName)
        # top:
        #   Just the app logo in a button, that has the url for the repository
        self.frm_top = tk.Frame(self.window, width = 500)
        self.frm_top.pack()
        logo_img = tk.PhotoImage(file = "logo/test.png")
        btn_logo = tk.Button(self.frm_top, text = "Logo", command=self.openRepo,  image = logo_img)
        btn_logo.pack()
        self.window.mainloop() # Must be moved to another method

test = Welcomewindow()

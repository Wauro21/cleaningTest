# version 0.1
import tkinter as tk
import webbrowser
# Globals
appName = "cleaningTest"
repository = "http://www.github.com/Wauro21/cleaningTest"
instructions = " Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


class Welcomewindow:
    window = None
    frm_top = None
    frm_mid = None
    #bot = None
    # list for files
    files = []
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
        self.frm_top.grid(row = 1, column = 1)
        logo_img = tk.PhotoImage(file = "logo/test.png")
        btn_logo = tk.Button(self.frm_top, text = "Logo", command=self.openRepo,  image = logo_img)
        btn_logo.pack()
        # mid:
        # Instructions: Must be brief, how this app works
        self.frm_mid = tk.Frame(self.window, width = 500)
        self.frm_mid.grid(row = 2, column = 1)
        lbl_instruc = tk.Label(self.frm_mid, cursor = "xterm", justify="left" , text = instructions, wraplength = 500)
        lbl_instruc.pack()
        # # Listbox con los archivos a cargar
        frm_mLeft = tk.Frame(self.frm_mid, width = 250)
        frm_mLeft.grid(row = 3, column = 0)
        # lstbx_left = tk.Listbox()
        # lstbx_left.pack()

        # frm_mRight = tk.Frame(self.frm_mid, width = 250)
        # lstbx_right = tk.Listbox()
        # lstbx_right.pack()
        # frm_mRight.pack(side=tk.RIGHT)
        self.window.mainloop() # Must be moved to another method

test = Welcomewindow()

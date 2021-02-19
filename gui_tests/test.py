import tkinter as tk
#Remember frames
window = tk.Tk()
frame = tk.Frame()
# insertar al frame aca
label = tk.Label(master=frame, text="This is a test!")
label.pack()
frame.pack()
window.mainloop()

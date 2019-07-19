import tkinter as tk
import gui_creation




win = tk.Tk()

win.title("Process Word Pairs")
win.geometry("760x420") 
win.resizable(0, 0) 


myGUI = gui_creation.LexGUI(win)

myGUI.createGUI()


win.mainloop()
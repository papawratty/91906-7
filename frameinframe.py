import Tkinter
tk = Tkinter.Tk()
frame1 = Tkinter.Frame(tk, height = 100, width = 100, bg = "WHITE", borderwidth=2)
frame2 = Tkinter.Frame(frame1, height = 100, width = 100, bg = "RED", borderwidth=2)
frame1.pack()
frame2.pack()
label = Tkinter.Label(frame2, text = "Label") #Receive a callback from button here
label.pack()
button = Tkinter.Button(frame1,text="Button") #Send some action to Label here
button.pack()
tk.mainloop()   

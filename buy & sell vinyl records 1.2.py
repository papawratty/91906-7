from tkinter import *
import random


class buy:
    def __init__(self, parent):

        #formatting variables....
        background_color = "#eda112"

        # converter Main Screen GUI...
        self.buy_frame = Frame(width=600, height=600, bg=background_color)
        self.buy_frame.grid()

        # buy heading (row 0)
        self.buy_label = Label(text="Buy page",
                               font=("Arial", "16", "bold"),
                               padx=10, pady=10)
        self.buy_label.grid(row=0)
        


#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Buy & Sell Vinyl Records")
    something = buy(root)
    root.mainloop()

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
        self.buy_label = Label(self.buy_frame, text="Buy page",
                               font=("Arial", "16", "bold"),
                               bg=background_color,
                               padx=10, pady=10)
        self.buy_label.grid(row=0)

        # Sell Button (row 1)
        self.sell_button = Button(self.buy_frame, text="sell",
                                  padx=10, pady=10,)
        self.sell_button.grid(row=1)
        


#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Buy & Sell Vinyl Records")
    something = buy(root)
    root.mainloop()

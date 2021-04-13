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
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.sell)
        self.sell_button.grid(row=1)


    def sell(self):
        print("going to sell page")
        sell_page = sell(self)
        sell_page.sell_text.configure(text="sell text goes here")
        
class Sell:
    def __init__(self, partner):
        
        background = "#19b8e6"
        
        # disable help button
        partner.sell_button.config(state=DISABLED)
        
        #sets up child window (ie: sell box)
        self.sell_box = Toplevel()
        
        # set up GUI Frame 
        self.sell_frame = Frame(self.sell_box, bg=background)
        self.sell_frame.grid()
        
        # set up sell heading (row 0)
        self.sell_heading = Label(self.sell_frame, text="Sell page",
                                 font="arial 10 bold", bg=background )
        
        # sell text (label, row 1)
        
        
        # dismiss button (row 2)


        

        

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Buy & Sell Vinyl Records")
    something = buy(root)
    root.mainloop()

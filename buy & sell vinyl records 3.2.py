from functools import partial
from tkinter import *
import random

stock_list = ["Igor - Tyler The Creator"
         "Good Kid Maad City - Kendrick Lamar"
         "Demon Days - Gorillaz"]
class stock:
    def __init__(self, name, amount):
        self.name = name
        self.amount
        stock_list.append(self)

#formatting variables....
background_color = "orange"

# converter Main Screen GUI...
buy_frame = Frame(width=3600, bg=background_color) 
buy_frame.grid()

    
# buy title (row 0)
buy_label = Label(buy_frame, text="Buy page",
                       font=("Arial", "16", "bold"),
                       bg=background_color,
                       padx=10, pady=5)
buy_label.grid(row=0, column=0)

# buy heading (label, row 1)
buy_heading = Label(buy_frame, text="Buy heading goes here",
                       font=("Arial", "12"),
                       bg=background_color,
                       padx=10, pady=5)
buy_heading.grid(row=1, column=0)

# buy heading (label, row 2)
buy_text = Label(buy_frame, text="this is where you buy vinyls",
                       font="Arial 9 italic", wrap=250, justify=LEFT,
                       bg=background_color,
                       padx=10, pady=10)
buy_text.grid(row=2, column=0)



def help(self):
        print("going to help page")
        get_help = help(self)
        get_help.help_text.configure(text="help text goes here")


class help:
    def __init__(self, partner):
        
        background = "#19b8e6"
        
        # disable help button
        partner.help_button.config(state=DISABLED)
        
        #sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        
        # set up GUI Frame 
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
        
        # set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)
        
        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="Help text go's here",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)
        
        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command= partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        #put help button back to noraml...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()
        
#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Buy & Sell Vinyl Records")
    root = buy()
    root.mainloop()

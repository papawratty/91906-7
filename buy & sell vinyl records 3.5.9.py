from functools import partial
from tkinter import *
import random
root = Tk()

blonde = 3
nectar = 6
flower_boy =12

class stock:
    def __init__(self, name, amount):
        self.name = name
        self.amount
        stock_list.append(self)

##########################################calution######################################################

    
##########################################buy frame######################################################
#formatting variables....
background_color = "orange"

#buy frame 
buy_frame = Frame(root, width=360, height=180, bg="orange")
buy_frame.grid(row = 0, column = 0)

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

#entry for amount of vinyls the user wants to buy
e = Entry(buy_frame, width=25)
e.insert(0,"")
e.grid(row=4, column=1)

myButton = Button(buy_frame, text="Enter", font=("Arial", "14"),
                          padx=10, pady=10, command=buy_confirm)
myButton.grid(row=5, column=1)

#Creating the Dropdown Menu

chosen_option = StringVar()
stock_list = "blonde", "nectar", "flower boy"
option_menu = OptionMenu(buy_frame, chosen_option, *stock_list)
option_menu.grid(row=1, column=1)

##########################################sell frame######################################################
#formatting variables....
sell_background_color = "blue"

#sell frame
sell_frame = Frame(root, width=360, height=180, bg="blue")
sell_frame.grid(row = 2, column = 0)

# sell title (row 0)
sell_label = Label(sell_frame, text="Sell page",
                       font=("Arial", "16", "bold"),
                       bg=sell_background_color,
                       padx=10, pady=5)
sell_label.grid(row=0, column=0)

# sell heading (label, row 1)
sell_heading = Label(sell_frame, text="sell heading goes here",
                       font=("Arial", "12"),
                       bg=sell_background_color,
                       padx=10, pady=5)
sell_heading.grid(row=1, column=0)

# buy heading (label, row 2)
sell_text = Label(sell_frame, text="this is where you buy vinyls",
                       font="Arial 9 italic", wrap=250, justify=LEFT,
                       bg=sell_background_color,
                       padx=10, pady=10)
sell_text.grid(row=2, column=0)

#entry for amount of vinyls the user wants to buy
sell_e = Entry(sell_frame, width=25)
sell_e.insert(0,"")
sell_e.grid(row=4, column=1)

sell_Button = Button(sell_frame, text="Enter", font=("Arial", "14"),
                          padx=10, pady=10, command=help)
sell_Button.grid(row=5, column=1)

#Creating the Dropdown Menu
sell_chosen_option = StringVar()
sell_option_menu = OptionMenu(sell_frame, sell_chosen_option, stock_list[0], *stock_list)
sell_option_menu.grid(row=1, column=1)
##########################################stock frame############################
#formatting variables....
stock_background_color = "green"

# stock frame
stock_frame = Frame(root, width=180, height=360, bg="green")
stock_frame.grid(row = 0, column = 2, sticky = NE,)

# stock title (row 0)
stock_label = Label(stock_frame, text="Stock page",
                       font=("Arial", "16", "bold"),
                       bg=stock_background_color,
                       padx=10, pady=5)
stock_label.grid(row=0, column=0)

# stock heading (label, row 1)
stock_heading = Label(stock_frame, text="stock heading goes here",
                       font=("Arial", "12"),
                       bg=stock_background_color,
                       padx=10, pady=5)
stock_heading.grid(row=1, column=0)

#stock items (label, row 2)
stock_text = Label(stock_frame, text="this is where the stock will go",
                       font="Arial 9 italic", wrap=250, justify=LEFT,
                       bg="white",
                       padx=10, pady=10)
stock_text.grid(row=2, column=0)


        
#main routine
if __name__ == "__main__":
    root.title("Buy & Sell Vinyl Records")
    root.mainloop()

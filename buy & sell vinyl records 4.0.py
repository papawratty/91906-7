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
def buy_stock():
  global blonde, nectar, flower_boy
  vinyl = chosen_vinyl.get()
  mode = chosen_action.get()

  if vinyl == "blonde":
      if mode == "sell":
        blonde += amount.get()
      else:
          blonde -= amount.get()
    
  elif vinyl == "nectar":
      if mode == "sell":
        nectar += amount.get()
      else:
          nectar -= amount.get()

  elif vinyl == "flower boy":
      if mode == "sell":
        flower_boy += amount.get()
      else:
          flower_boy -= amount.get()

  
  vinyl_string = "blonde: ${:.2f}\nnectar: ${:.2f}\nflower boy: ${:.2f}".format(blonde, nectar, flower_boy)
  vinyl_details.set(vinyl_string)
  amount.set("")
##########################################buy/sell frame######################################################
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
                          padx=10, pady=10, command=buy_stock)
myButton.grid(row=5, column=1)

#Creating the Dropdown Menu

chosen_option = StringVar()
stock_list = "blonde", "nectar", "flower boy"
option_menu = OptionMenu(buy_frame, chosen_option, *stock_list, textvariable=amount)
option_menu.grid(row=1, column=1)


       
#main routine
if __name__ == "__main__":
    root.title("Buy & Sell Vinyl Records")
    root.mainloop()

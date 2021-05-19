from functools import partial
from tkinter import *
import random
root = Tk()

blonde = 3
nectar = 6
flower_boy =12

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

# Create a label for the account combobox
vinyl_label = Label(buy_frame, text="Vinyl: ")
vinyl_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
vinyl_names = ["blonde", "nectar", "flower boy"]
chosen_vinyl = StringVar()
chosen_vinyl.set(vinyl_names[0])

# Create a Combobox to select the account
vinyl_box = ttk.Combobox(buy_frame, textvariable=chosen_vinyl, state="readonly")
vinyl_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")




##########################################sell frame######################################################
#formatting variables....
sell_background_color = "blue"

#sell frame
sell_frame = Frame(root, width=360, height=180, bg="blue")
sell_frame.grid(row = 2, column = 0)

# sell title (row 0)
sell_label = Label(sell_frame, text="Stock page",
                       font=("Arial", "16", "bold"),
                       bg=sell_background_color,
                       padx=10, pady=5)
sell_label.grid(row=0, column=0)

# Create and set the account details variable
vinyl_details = StringVar()
vinyl_details.set("Blonde: 0 \nNectar: 0\nFlower boy: 0")

# Create the details label and pack it into the GUI
vinyl_label = Label(sell_frame, textvariable=Vinyl_details)
Vinyl_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)






        
#main routine
if __name__ == "__main__":
    root.title("Buy & Sell Vinyl Records")
    root.mainloop()

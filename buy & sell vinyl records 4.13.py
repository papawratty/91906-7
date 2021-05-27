from functools import partial
from tkinter import *
from tkinter import ttk
import random
root = Tk()

blonde = 3
nectar = 6
flower_boy = 12

sold_blonde = 0
sold_nectar = 0
sold_flower_boy = 0



##########################################calution######################################################
def buy_stock():
  global blonde, nectar, flower_boy
  vinyl = chosen_vinyl.get()
  mode = chosen_action.get()

  if vinyl == "blonde":
      if mode == "sell":
        blonde += amount.get()
      else:
        if blonde > 1:
          blonde -= amount.get()
          sold_blonde += amount.get()
        else:
          print("nah")
    
  elif vinyl == "nectar":
      if mode == "sell":
        nectar += amount.get()
      else:
          nectar -= amount.get()
          sold_nectar += amount.get()

  elif vinyl == "flower boy":
      if mode == "sell":
        flower_boy += amount.get()
      else:
          flower_boy -= amount.get()
          sold_flower_boy += amount.get()

  
  vinyl_string = "Blonde:{}\nNectar:{}\nFlower boy:{}".format(blonde, nectar, flower_boy)
  sold_vinyl_string = "Blonde:{}\nNectar:{}\nFlower boy:{}".format(sold_blonde, sold_nectar,
                                                                   sold_flower_boy)
  vinyl_details.set(vinyl_string)
  sold_vinyl_details.set(sold_vinyl_string)
  
  amount.set("")

  

##########################################buy frame######################################################
# buy/sell frame 
buy_frame = ttk.LabelFrame(root, width=360, height=180, text="Buy & Sell")
buy_frame.grid(row = 0, column = 1)

# Create a label for the account combobox
vinyl_label = ttk.Label(buy_frame, text="Vinyl: ")
vinyl_label.grid(row=1, column=0, padx=10, pady=3 )

# Set up a variable and option list for the account Combobox
vinyl_names = ["blonde", "nectar", "flower boy"]
chosen_vinyl = StringVar()
chosen_vinyl.set(vinyl_names[0])

# Create a Combobox to select the account
vinyl_box = ttk.Combobox(buy_frame, textvariable=chosen_vinyl, state="readonly")
vinyl_box['values'] = vinyl_names
vinyl_box.grid(row=1, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(buy_frame, text="Action:")
action_label.grid(row=3, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["buy", "sell"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(buy_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(buy_frame, text="Amount:")
amount_label.grid(row=4, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = IntVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(buy_frame, textvariable=amount)
amount_entry.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(buy_frame, text="Submit", command=buy_stock)
submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
##########################################stock frame###################################################### 
# stock frame
stock_frame = ttk.LabelFrame(root, width=360, height=180, text="Stock")
stock_frame.grid(row = 0, column = 0, sticky="NSWE", padx=10, pady=10)

# Create and set the account details variable
vinyl_details = StringVar()
vinyl_details.set("Blonde: 3 \nNectar: 6\nFlower boy: 12")

# Create the details label and pack it into the GUI
vinyl_label = Label(stock_frame, textvariable=vinyl_details)
vinyl_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# stock frame
sold_stock_frame = ttk.LabelFrame(root, width=360, height=180, text="Sold Stock")
sold_stock_frame.grid(row = 2, column = 0, sticky="SW", padx=10, pady=5)

# Create and set the account details variable
sold_vinyl_details = StringVar()
sold_vinyl_details.set("Blonde: 0 \nNectar: 0\nFlower boy: 0")

# Create the details label and pack it into the GUI
sold_vinyl_label = Label(sold_stock_frame, textvariable=sold_vinyl_details)
sold_vinyl_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)




       
#main routine
if __name__ == "__main__":
    root.title("Buy & Sell Vinyl Records")
    root.mainloop()

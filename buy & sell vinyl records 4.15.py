from functools import partial
from tkinter import *
from tkinter import ttk
import random
root = Tk()
##########################################calution######################################################
def buy_stock():
  global super_dude, lizard_man, water_woman
  comic = chosen_comic.get()
  mode = chosen_action.get()
  
  super_dude = 8
  lizard_man = 12
  water_woman = 3
  
  sold_super_dude = 0
  sold_lizard_man = 0
  sold_water_woman = 0

  if comic == "Super dude":
     if mode == "buy":
        if super_dude > amount.get():
          super_dude -= amount.get()
          sold_super_dude += amount.get()
     else:
        super_dude += amount.get()
        
    
  elif comic == "Lizard man":
      if mode == "buy":
        lizard_man -= amount.get()
        sold_lizard_man += amount.get()
      else:
        lizard_man += amount.get()
        

  elif comic == "Water woman":
      if mode == "buy":
        water_woman -= amount.get()
        sold_water_woman += amount.get()
      else:
        water_woman += amount.get()
        

  
  comic_string = "Super dude:{}\nLizard man:{}\nWater woman:{}".format(super_dude, lizard_man, water_woman)
  sold_comic_string = "Super dude:{}\nLizard man:{}\nWater woman:{}".format(sold_super_dude, sold_lizard_man,
                                                                   sold_water_woman)
  comic_details.set(comic_string)
  sold_comic_details.set(sold_comic_string)
  
  amount.set("")

  

##########################################buy frame######################################################
# buy/sell frame 
buy_frame = ttk.LabelFrame(root, width=360, height=180, text="Buy & Sell")
buy_frame.grid(row = 0, column = 1)

# Create a label for the account combobox
comic_label = ttk.Label(buy_frame, text="Vinyl: ")
comic_label.grid(row=1, column=0, padx=10, pady=3 )

# Set up a variable and option list for the account Combobox
comic_names = ["Super dude", "Lizard man", "Water woman"]
chosen_comic = StringVar()
chosen_comic.set(comic_names[0])

# Create a Combobox to select the account
comic_box = ttk.Combobox(buy_frame, textvariable=chosen_comic, state="readonly")
comic_box['values'] = comic_names
comic_box.grid(row=1, column=1, padx=10, pady=3, sticky="WE")

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
comic_details = StringVar()
comic_details.set("Super dude: 8 \nLizard man: 12\nWater woman: 3")

# Create the details label and pack it into the GUI
comic_label = Label(stock_frame, textvariable=comic_details)
comic_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
##########################################sold stock frame###################################################### 
# sold stock frame
sold_stock_frame = ttk.LabelFrame(root, width=360, height=180, text="Sold Stock")
sold_stock_frame.grid(row = 0, column = 3, sticky="NSWE", padx=10, pady=5)

# Create and set the account details variable
sold_comic_details = StringVar()
sold_comic_details.set("Super dude: 0 \nLizard man: 0\nWater woman: 0")

# Create the details label and pack it into the GUI
sold_comic_label = Label(sold_stock_frame, textvariable=sold_comic_details)
sold_comic_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)




       
#main routine
if __name__ == "__main__":
    root.title("Buy & Sell Vinyl Records")
    root.mainloop()

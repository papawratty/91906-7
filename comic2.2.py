####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk
import random


##################  CLASS CODE  ######################
# Create the item class
class item:
  """The item class stores the details of each item and has methods to restock, buy and calculate progress towards the super_dude sold"""
  def __init__(self, name, amount, sold):
    self.name = name
    self.amount = amount
    self.sold = sold
    item_list.append(self)

  # restock method adds comics to amount
  def restock(self, amount):
    if amount > 0:
      self.amount += amount
      return True
    else:
      return False

  # buy method subtracts comics from amount
  def buy(self, amount, sold):
    if amount > 0 and amount <= self.amount:
      self.amount -= amount
      item.sold += amount
      return True
    else:
      return False


##############  FUNCTIONS AND SETUP ###############
# Create a function to read data from the file
def get_data():
  item_file = open("items.txt","r")
  line_list = item_file.readlines()
  
  for line in line_list:
    item_data = line.strip().split(",")


# Create a function to get item names list
def create_name_list():
  name_list = []
  for item in item_list:
    name_list.append(item.name)
  return name_list

# Create a function that will update the amount.
def update_amount():
  total_amount = 0
  amount_string = ""

  # Append each items amount, progress and sold to the label
  for item in item_list:
    amount_string += "{}: {}  and {} were sold today\n".format(item.name, item.amount, item.sold)
    total_amount += item.amount

  amount_string += "\nTotal amount: {}".format(total_amount)
  item_details.set(amount_string)

# Create the restock function
def restock_comics(item):
  if item.restock(amount.get()):
    message = random.choice(restock_messages)
    message_text.set(message)
    action_feedback.set("Success! Total of {} restocked into {}".format(amount.get(), item.name))
  else:
    action_feedback.set("Please enter a positive number")

# Create the buyfunction
def buy_comics(item):
  if item.buy(amount.get()):
    message = random.choice(buy_messages)
    message_text.set(message)
    action_feedback.set("Success! you brought {} {} comics".format(amount.get(), item.name))
  else:
    action_feedback.set("Not enough {} comics or not a valid amount".format(item.name))

# Create the manage action function
def manage_action():
  try:
    for item in item_list:
      if chosen_item.get() == item.name:
        if chosen_action.get() == "Buy":
         buy_comics(item)
        else:
          restock_comics(item)

    # Update the GUI
    update_amount()
    amount.set("")

  # Add an exception for text input
  except ValueError:
    action_feedback.set("Please enter a valid number")


# Set up Lists
item_list = []
restock_messages = ["have a good day", "thank you"]
buy_messages = ["enjoy","buy ","buy"]


# Create instances of the class
super_dude = item("Super dude", 8, 0)
lizard_dude = item("Lizard dude", 12, 0)
water_woman = item("Water woman", 3, 0)
item_names = create_name_list()

##################  GUI CODE  ######################
root = Tk()
root.title("Comic store")

# Create the left frame
left_frame = ttk.LabelFrame(root, text="Comics Details")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can restock or buy comics.")

# Create and pack the message label
message_label = ttk.Label(left_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and set the item details variable
item_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(left_frame, textvariable=item_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the right frame
right_frame = ttk.LabelFrame(root,text='Buy and Restock')
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

# Create a label for the item combobox
item_label = ttk.Label(right_frame, text="Comic: ")
item_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the item Combobox
chosen_item = StringVar()
chosen_item.set(item_names[0])

# Create a Combobox to select the item
item_box = ttk.Combobox(right_frame, textvariable=chosen_item, state="readonly")
item_box['values'] = item_names
item_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(right_frame, text="Action:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Restock", "Buy"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(right_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(right_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = IntVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(right_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(right_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(right_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_amount()
root.mainloop()






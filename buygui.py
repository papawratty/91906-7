# Create the sell frame
sell_frame = ttk.LabelFrame(root, text="sell")
sell_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

#create and set the message text variable
message_text = StringVar()
message_text.set("my name jeff")

# Create and pack the message label
message_label = ttk.Label(sell_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="hoe'r;lt.PNG")
happy_image = PhotoImage(file="Capture.PNG")
sad_image = PhotoImage(file="ali-a no brow.PNG")

image_label = ttk.Label(sell_frame, image=neutral_image)
image_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Create and set the account details variable
account_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(sell_frame, textvariable=account_details)
details_label.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# Create the bottom frame
sell_bottom_frame = ttk.LabelFrame(root)
sell_bottom_frame.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

# Create a label for the account combobox
account_label = ttk.Label(sell_bottom_frame, text="Account: ")
account_label.grid(row=3, column=1, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(sell_bottom_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=2, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(sell_bottom_frame, text="Action:")
action_label.grid(row=4, column=1)

# Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(sell_bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=2, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(sell_bottom_frame, text="Amount:")
amount_label.grid(row=5, column=1, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(sell_bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=2, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(sell_bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(sell_bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=1, columnspan=2)
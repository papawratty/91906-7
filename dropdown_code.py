# dropdown menu (row 2)
        items_list = ["Igor - Tyler The Creator"
             "Good Kid Maad City - Kendrick Lamar"
             "Demon Days - Gorillaz"]
        
        popupMenu = OptionMenu(buy_frame, tkvar, *items_label)
        Label(buy_frame, text="Choose a Vinyl").grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)

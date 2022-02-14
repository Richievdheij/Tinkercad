from tkinter import *
from tkinter.messagebox import showinfo
from random import randrange

# Makes the window
window = Tk() 
window.title("Grabbelton")

items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] # Items the user can win
total_items = len(items) # Total amount of items
item_information = f"items: {total_items}" # Label text


# Shows what the user won
def item_won(): 
    total_items = len(items) # Total items
    number = randrange(0, total_items) # Pick a random number 
    item = items[number] # Pick the item

    items.pop(number) # Delete the item from the array

    showinfo("Gefeliciteerd", f"Gefeliciteerd, je hebt een {item} gegrabbeld!") # Shows what the user won


def update_label():
    total_items = len(items) # Total items

    label.configure(text = f"items: {total_items}") # Change the label text


def game_status():
    total_items = len(items)

    if total_items == 0:
        window.destroy()


# Makes the label
label = Label(window)

label = Label(
    window, 
    font=("arial", 50, 'bold'), 
    bg="lightblue",
    fg="black"
)

label.configure(text=item_information)
label.pack()


# Makes the button
button = Button(
    window,
    bg="lightgray",
    fg="black"
) 

button.configure(
    text="Grabbelen", 
    command= lambda: [item_won(), update_label(), game_status()]
) 

button.pack(
    fill = "both",
    expand=True
)


# If the code starts
if __name__ == "__main__":
    window.mainloop() 
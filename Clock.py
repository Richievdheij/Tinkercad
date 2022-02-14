import tkinter as tk
import time


window = tk.Tk() # Makes the window
window.title("Clock") # Title of the window
timeText = tk.StringVar() 
label = tk.Label(bg="lightblue", fg="black", font=("Comic sans MS", 125), textvariable=timeText) # Information about the window / text
label.pack() # Add the time label to the window


# Count every 1 second
def count():
    localTime = time.localtime() # Get the local time
    timeText.set(time.strftime("%H:%H:%S", localTime)) # Set the text to the time
    window.after(1000, count) # Go every 1 second to this function


# If the code starts
if __name__ == "__main__":
    count() # Show the time
    window.mainloop() # Starts the window
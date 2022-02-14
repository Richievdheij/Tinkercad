import tkinter
import time

window = tkinter.Tk()
kleuren = ["black", "purple", "red", "orange", "yellow", "white"]
sizeRatio = 50
sizeRatioStr = str(sizeRatio)
number = 6

def windowChange():
    global number
    if number == 0:
        print("BOOM!")
        window.destroy()
    else:
        global sizeRatio
        global sizeRatioStr
        window.configure(height=sizeRatioStr, width=sizeRatioStr, bg=kleuren[number - 1])
        print(number)
        number -=1
        sizeRatio += 50
        sizeRatioStr = str(sizeRatio)
        window.after(2000, windowChange)

window.after(2000, windowChange)

window.mainloop()
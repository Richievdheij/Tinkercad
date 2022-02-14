import tkinter

window = tkinter.Tk()
window.title('Hello')
window.configure(bg='black')
window.geometry("150x100")

# box 1
box1 = tkinter.Label(
    window,
    text="Hello \n Tkinter!",
    bg="red",
    fg="white"
)

box1.pack(
    ipadx=20,
    ipady=10,
    expand=True
)

window.mainloop()
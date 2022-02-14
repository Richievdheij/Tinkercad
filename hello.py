import tkinter

window = tkinter.Tk()
window.title('Hello')
window.configure(bg='black')
window.geometry("200x200")

# box 1
box1 = tkinter.Label(
    window,
    text="Hello Tkinter!",
    bg="red",
    fg="white"
)

box1.pack(
    ipadx=20,
    ipady=40,
    expand=True
)

window.mainloop()
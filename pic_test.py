from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

canvas = Canvas(
    ws,
    width = 500,
    height = 500
    )
canvas.pack()
img = PhotoImage(file='pictures/1.png')
canvas.create_image(
    10,
    10,
    anchor=NW,
    image=img
    )
ws.mainloop()
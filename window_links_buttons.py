from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
from PIL import ImageTk, Image
from io import BytesIO

root = Tk()
root.configure(borderwidth=2)
root.title("Военная экипировка и снаряга!")
w, h, x, y = 1360, 850, 500, 100
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

background_image = PhotoImage(file="pictures/com_2.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

list_pic = [
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg"
]


def exit_new_form():
    root.destroy()
    text_exit_1 = 'Работа приложения'
    text_exit_2 = 'Форма с кнопками, фото и ссылками закрыта!'
    messagebox.showinfo(text_exit_1, text_exit_2)


list_photos = []
num_col = 0
for i in list_pic:
    with urlopen(i) as u:
        raw_data = u.read()
    img = Image.open(BytesIO(raw_data))
    list_photos.append(ImageTk.PhotoImage(img.resize((70, 90), Image.LANCZOS)))
for photo in list_photos:
    Button(root, image=photo, width=70, height=80).grid(row=0, column=num_col)
    num_col += 1

Button(root, text="ВЫХОД", command=exit_new_form, bg="red", fg="white").grid(row=5, column=14, padx=2,
                                                                             pady=2)

root.mainloop()

## IT WORKS!
# from tkinter import *
# # from tkinter.ttk import *
# from tkinter import messagebox
#
# from urllib.request import urlopen
# from PIL import ImageTk, Image
# import urllib
# from io import BytesIO
#
# root = Tk()
# root.configure(borderwidth=2)
# root.title("Военная экипировка и снаряга!")
# w, h, x, y = 1360, 850, 500, 100
# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#
# background_image = PhotoImage(file="pictures/com_2.png")
# background_label = Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# list_pic = [
#     "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
#     "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
#     "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg"
# ]
#
#
# def exit_new_form():
#     root.destroy()
#     text_exit_1 = 'Работа приложения'
#     text_exit_2 = 'Форма с кнопками, фото и ссылками закрыта!'
#     messagebox.showinfo(text_exit_1, text_exit_2)
#
#
# buttons = []
#
#
# with urlopen(list_pic[0]) as u:
#     raw_data = u.read()
# img = Image.open(BytesIO(raw_data))
# photo_1 = ImageTk.PhotoImage(img.resize((70, 90), Image.LANCZOS))
# buttons.append(Button(root, image=photo_1, width=70, height=80))
# buttons[0].grid(row=0, column=0)
#
# with urlopen(list_pic[1]) as u:
#     raw_data = u.read()
# img = Image.open(BytesIO(raw_data))
# photo_2 = ImageTk.PhotoImage(img.resize((70, 90), Image.LANCZOS))
# buttons.append(Button(root, image=photo_2, width=70, height=80))
# buttons[1].grid(row=0, column=1)
#
# Button(root, text="ВЫХОД", command=exit_new_form, bg="red", fg="white").grid(row=5, column=14, padx=2,
#                                                                              pady=2)
#
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
#
# # Create the window
# root = tk.Tk()
#
# # Create the buttons
# button1 = tk.Button(root)
# button2 = tk.Button(root)
# button3 = tk.Button(root)
#
# # Get the images
# image1 = Image.open('https://docs.google.com/drawings/d/1ZA8wrkgBRHtYBxFsh-TF6qCuXZd8me_X2ALFBJVuXc4/edit?usp=share_link')
# image2 = Image.open('https://docs.google.com/drawings/d/1ZA8wrkgBRHtYBxFsh-TF6qCuXZd8me_X2ALFBJVuXc4/edit?usp=share_link')
# image3 = Image.open('https://docs.google.com/drawings/d/1ZA8wrkgBRHtYBxFsh-TF6qCuXZd8me_X2ALFBJVuXc4/edit?usp=share_link')
#
# # Create the images for the buttons
# photoimage1 = ImageTk.PhotoImage(image1)
# photoimage2 = ImageTk.PhotoImage(image2)
# photoimage3 = ImageTk.PhotoImage(image3)
#
# # Set the images for the buttons
# button1.config(image=photoimage1)
# button2.config(image=photoimage2)
# button3.config(image=photoimage3)
#
# # Pack the buttons
# button1.pack()
# button2.pack()
# button3.pack()
#
# # Start the window
# root.mainloop()

# import tkinter as tk
# from PIL import ImageTk, Image
#
# # Create window
# root = tk.Tk()
#
# # Create list of web links
# links = [
#     "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
#     "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
#     "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg"
# ]
#
# # Create a list of images from the web links
# images = [Image.open(link) for link in links]
#
# # Create the three buttons
# buttons = []
# for image in images:
#     buttons.append(tk.Button(root, image=ImageTk.PhotoImage(image)))
#
# # Add buttons to the window
# for button in buttons:
#     button.pack()

root.mainloop()

# import tkinter as tk
#
# # Create window
# root = tk.Tk()
#
# # Create image list
# image_list = []
#
# # Load images
# for i in range(2):
#     # Get URL of image
#     img_url = '<YOUR_IMAGE_URL>'
#     # Load the image
#     image = tk.PhotoImage(file=img_url)
#     # Add image to list
#     image_list.append(image)
#
# # Create buttons
# for i in range(2):
#     # Create button
#     btn = tk.Button(root, image=image_list[i])
#     # Place button
#     btn.grid(row=i, column=0)
#
# # Start main loop
# root.mainloop()

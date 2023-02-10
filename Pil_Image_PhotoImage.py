from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
import urllib
from io import BytesIO

root = Tk()
url = "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg"
jpg_name = "1.jpg"

root.geometry("800x600")
root.title("Test image")

# photo = urlopen(url)
# photoimage = ImageTk.PhotoImage(data=photo.read())
# Label(root, image=photoimage).grid(row=1, column=0, padx=2, pady=2)
# Button(root, image=photoimage, width=150, height=200).grid(row=0, column=0, padx=2, pady=2)

# fd = urllib.urlretrieve(url, jpg_name)
# im1 = Image.open(jpg_name)
# im_small = im1.resize((200, 200), Image.ANTIALIAS)
# im = ImageTk.PhotoImage(im_small)
# image = Label(root, image=im, bd=2)
# image.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

with urllib.request.urlopen(url) as u:
    raw_data = u.read()
img = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(img.resize((70, 90), Image.LANCZOS))
Button(root, image=photo, width=70, height=90).grid(row=0, column=0, padx=2, pady=2)
label = Label(root, image=photo).grid(row=1, column=0, padx=2, pady=2)

root.mainloop()

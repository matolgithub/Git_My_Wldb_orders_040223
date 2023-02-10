import tkinter as tk
from PIL import ImageTk, Image

# Create window
root = tk.Tk()

# Create list of web links
links = [
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg",
    "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg"
]

# Create a list of images from the web links
images = [Image.open(link) for link in links]

# Create the three buttons
buttons = []
for image in images:
    buttons.append(tk.Button(root, image=ImageTk.PhotoImage(image)))

# Add buttons to the window
for button in buttons:
    button.pack()

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
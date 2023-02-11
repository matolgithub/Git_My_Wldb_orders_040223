from tkinter import *
from tkinter.ttk import Progressbar
import time

ws = Tk()
ws.title('Идёт выполнение...')
ws.geometry("300x120")
ws.config(bg='black')

pb = Progressbar(ws, orient=HORIZONTAL, length=150, mode='determinate')

pb.place(x=60, y=40)

txt = Label(ws, text='0%', bg='black', fg='white')

txt.place(x=220, y=40)

for i in range(6):
    ws.update_idletasks()
    pb['value'] += 20
    time.sleep(0.5)
    txt['text'] = pb['value'], '%'

time.sleep(3)
ws.destroy()

ws.mainloop()

# from tkinter import *
# from tkinter import ttk
# import time
#
# root = Tk()
# root.title("Идёт выполнение...")
# root.geometry("250x100")
# progr_value = 10
#
# while progr_value <= 100:
#     label = ttk.Label(text="Выполнено:")
#     label.pack(anchor=NW, padx=6, pady=6)
#
#     value_var = IntVar(value=progr_value)
#
#     progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
#     progressbar.pack(fill=X, padx=6, pady=6)
#     progr_value += 10
#
#     label = ttk.Label(textvariable=value_var, text="%")
#     label.pack(anchor=NW, padx=6, pady=6)
#
#     time.sleep(1)
#
# root.mainloop()

import tkinter as tk
import sys

sys.path.append('.')
from database_connection.database_connection import update_rgb_values, get_rgb_values

rgb = get_rgb_values()
def update_values(color, adjustment):
    rgb[color] = 100 if (rgb[color] + adjustment > 100) else 0 if (rgb[color] + adjustment < 0) else rgb[color] + adjustment
    print(update_rgb_values(rgb[0], rgb[1], rgb[2]))

def create_red_frame(root):
    red_frame = tk.Frame(root, bg='#ff0000', width=213, height=400)
    red_frame.grid(row=1, column=0)

    red_frame.grid_propagate(False)

    increase_red_btn = tk.Button(red_frame, text='+10', width=15, bg='#ff2626', command=lambda: [update_values(0, 10)])
    increase_red_btn.grid(row=0, column=0, pady=70, padx=50)

    current_red = tk.Label(red_frame, text='current value: 70', bg='#ff0000', height=4)
    current_red.grid(row=1, column=0)

    decrease_red_btn = tk.Button(red_frame, text='-10', width=15, bg='#ff2626', command=lambda: [update_values(0, -10)])
    decrease_red_btn.grid(row=2, column=0, pady=70, padx=50)

def create_green_frame(root):
    green_frame = tk.Frame(root, bg='green', width=213, height=400)
    green_frame.grid(row=1, column=1)

    green_frame.grid_propagate(False)

    increase_green_btn = tk.Button(green_frame, text='+10', width=15, bg='#008c25', command=lambda: [update_values(1, 10)])
    increase_green_btn.grid(row=0, column=0, pady=70, padx=50)

    current_green = tk.Label(green_frame, text='current value: 70', bg='green', height=4)
    current_green.grid(row=1, column=0)

    decrease_green_btn = tk.Button(green_frame, text='-10', width=15, bg='#008c25', command=lambda: [update_values(1, -10)])
    decrease_green_btn.grid(row=2, column=0, pady=70, padx=50)



def create_blue_frame(root):
    blue_frame = tk.Frame(root, bg='blue', width=213, height=400)
    blue_frame.grid(row=1, column=2)

    blue_frame.grid_propagate(False)

    increase_blue_btn = tk.Button(blue_frame, text='+10', width=15, bg='#0083c9', command=lambda: [update_values(2, 10)])
    increase_blue_btn.grid(row=0, column=0, pady=70, padx=50)

    current_blue = tk.Label(blue_frame, text='current value: 70', bg='blue', height=4)
    current_blue.grid(row=1, column=0)

    decrease_blue_btn = tk.Button(blue_frame, text='-10', width=15, bg='#0083c9', command=lambda: [update_values(2, -10)])
    decrease_blue_btn.grid(row=2, column=0, pady=70, padx=50)

root = tk.Tk()
root.geometry("639x480")



text_frame = tk.Frame(root, bg='#ffffff', width=639, height=80)
text_frame.pack_propagate(False)
text_frame.grid(row=0, column=0, columnspan=3)

text_label = tk.Label(text_frame, text='Set color values', bg='#ffffff', pady=20)
text_label.pack()

create_red_frame(root)
create_green_frame(root)
create_blue_frame(root)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)





root.mainloop()
import tkinter as tk
from time import strftime
from datetime import date


def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)


def display_clock():
    name = name_entry.get()
    name_label.config(text=f'Bienvenido, {name}!')

    name_entry.destroy()
    name_button.destroy()

    date_label = tk.Label(root, text=date.today().strftime(
        "%d-%m-%Y"), font=('Arial', 14))
    date_label.pack(pady=10)

    global time_label
    time_label = tk.Label(root, font=('Arial', 48))
    time_label.pack()

    update_time()


root = tk.Tk()
root.title('Reloj Digital')
root.geometry('400x200')

name_label = tk.Label(root, text='Ingrese su nombre:', font=('Arial', 14))
name_label.pack(pady=10)

name_entry = tk.Entry(root, font=('Arial', 14))
name_entry.pack()

name_button = tk.Button(root, text='Mostrar reloj',
                        command=display_clock, font=('Arial', 14))
name_button.pack(pady=20)

root.mainloop()

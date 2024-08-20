from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = int(miles) * 1.609
    rounded = round(km)
    km_result.config(text=f'{rounded}')

window = Tk()
window.minsize(width=200, height=20)
window.title('Miles to Kilometers')

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=4, row=0)

is_equal = Label(text='is equal to')
is_equal.grid(column=0, row=1)

km_result = Label(text='0')
km_result.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=4, row=1)

calc_button = Button(text='calculate', command=miles_to_km)
calc_button.grid(column=1, row=2)

T0D0


window.mainloop()
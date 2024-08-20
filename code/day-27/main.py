from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)
label = Label(text='HI', font=('Arial', 15, 'bold'))
label.grid(column=0,row=0)

def button_clicked():
    print('Yeah')
    new_text = input.get()
    label.config(text=new_text)

button = Button(text='hi man', command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text='No man')
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3,row=2)




window.mainloop()
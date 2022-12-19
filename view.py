from tkinter import *


def myclick(data):
    entry.insert(data)


window = Tk()
entry = Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
Button(window, text='1', command=lambda: myclick(1)).grid(row=1, column=1)

# Button(window, text='2').grid(row=1, column=2)
# Button(window, text='3').grid(row=1, column=3)
# Button(window, text='+').grid(row=1, column=4)
# Button(window, text='4').grid(row=2, column=1)
# Button(window, text='5').grid(row=2, column=2)
# Button(window, text='6').grid(row=2, column=3)
# Button(window, text='-').grid(row=2, column=4)
# Button(window, text='7').grid(row=3, column=1)
# Button(window, text='8').grid(row=3, column=2)
# Button(window, text='9').grid(row=3, column=3)
# Button(window, text='*').grid(row=3, column=4)
# Button(window, text='  0  ').grid(row=4, column=1, columnspan=2)
# Button(window, text='=').grid(row=4, column=3)
# Button(window, text='/').grid(row=4, column=4)
window.mainloop()


def get_data():
    expression = input('Введите выражение: ')
    return expression


def view_data(result):
    print(result)

from tkinter import *


def click_button(data):
    display.insert(100, data)


def click_count():
    display.insert(100, f' = {eval(display.get())}')


window = Tk()
display = Entry(fg="white", bg="black", width=50)
display.grid(row=0, column=0, columnspan=4)

button_1 = Button(window, text='1', command=lambda: click_button(1))
button_1.grid(row=1, column=0)
button_2 = Button(window, text='2', command=lambda: click_button(2))
button_2.grid(row=1, column=1)
button_3 = Button(window, text='3', command=lambda: click_button(3))
button_3.grid(row=1, column=2)
button_4 = Button(window, text='4', command=lambda: click_button(4))
button_4.grid(row=2, column=0)
button_5 = Button(window, text='5', command=lambda: click_button(5))
button_5.grid(row=2, column=1)
button_6 = Button(window, text='6', command=lambda: click_button(6))
button_6.grid(row=2, column=2)
button_7 = Button(window, text='7', command=lambda: click_button(7))
button_7.grid(row=3, column=0)
button_8 = Button(window, text='8', command=lambda: click_button(8))
button_8.grid(row=3, column=1)
button_9 = Button(window, text='9', command=lambda: click_button(9))
button_9.grid(row=3, column=2)
button_0 = Button(window, text='0', command=lambda: click_button(0))
button_0.grid(row=4, column=1)

button_dot = Button(window, text='.', command=lambda: click_button('.'))
button_dot.grid(row=4, column=0)
button_sum = Button(window, text='+', command=lambda: click_button('+'))
button_sum.grid(row=1, column=3)
button_sub = Button(window, text='-', command=lambda: click_button('-'))
button_sub.grid(row=2, column=3)
button_mul = Button(window, text='*', command=lambda: click_button('*'))
button_mul.grid(row=3, column=3)
button_div = Button(window, text='/', command=lambda: click_button('/'))
button_div.grid(row=4, column=3)

button_equal = Button(window, text='=', command=lambda: click_count())
button_equal.grid(row=4, column=2)

window.mainloop()

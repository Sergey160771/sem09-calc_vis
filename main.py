from tkinter import *


def click_button(data):
    display.insert(100, data)


def click_count():
    display.insert(100, f' = {eval(display.get())}')


def clear():
    display.delete(0, END)


window = Tk()
window.title('Calculator')
display = Entry(fg="white", bg="black",width=30, borderwidth=10)
display.grid(row=0, column=0, columnspan= 4)

button_1 = Button(text="1", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(1))
button_1.grid(row=3, column=0)
button_2 = Button(text="2", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(2))
button_2.grid(row=3, column=1)
button_3 = Button(text="3", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(3))
button_3.grid(row=3, column=2)
button_4 = Button(text="4", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(4))
button_4.grid(row=2, column=0)
button_5 = Button(text="5", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(5))
button_5.grid(row=2, column=1)
button_6 = Button(text="6", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(6))
button_6.grid(row=2, column=2)
button_7 = Button(text="7", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(7))
button_7.grid(row=1, column=0)
button_8 = Button(text="8", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(8))
button_8.grid(row=1, column=1)
button_9 = Button(text="9", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(9))
button_9.grid(row=1, column=2)
button_0 = Button(text="0", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button(0))
button_0.grid(row=4, column=0)

button_dot = Button(text=".", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button('.'))
button_dot.grid(row=4, column=1)
button_sum = Button(text="+", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button('+'))
button_sum.grid(row=4, column=3)
button_sub = Button(text="-", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button('-'))
button_sub.grid(row=3, column=3)
button_mul = Button(text="*", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button('*'))
button_mul.grid(row=2, column=3)
button_div = Button(text="/", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_button('/'))
button_div.grid(row=1, column=3)
button_equal = Button(text="=", width=3, height=2, bg="blue", fg="yellow", command=lambda: click_count())
button_equal.grid(row=4, column=2)
button_clear = Button(text="clear", width=3, height=2, bg="blue", fg="yellow", command=clear)
button_clear.grid(row=5, column=3)

window.mainloop()
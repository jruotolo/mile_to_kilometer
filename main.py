from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")

window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

miles_input = Entry(width=10)
miles_input.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=1, row=2)

result_label = Label(text='0')
result_label.grid(column=2, row=2)

km_label = Label(text="Kilometers")
km_label.grid(column=3, row=2)


def button_clicked():
    user_input_float = float(miles_input.get())
    result = user_input_float * 1.60934
    result_label.config(text=f'{result:.2f}')


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=3)

quit_button = Button(text="Quit", command=exit)
quit_button.grid(column=2, row=4)


window.mainloop()

from tkinter import *
window = Tk()
window.title("Miles to Km converter")
window.minsize(width=100, height=50)


def button_clicked():
    miles = entry_miles.get()
    km = float(miles)*1.6
    output.config(text=f"{round(km,2)}")


entry_miles = Entry()
entry_miles.grid(column=2, row=1)

entry_label = Label(text="Miles")
entry_label.grid(column=3, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

output = Label(width=20, height=1)
output.grid(column=2, row=2)

output_label = Label(text="Km")
output_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=3)


window.mainloop()

from tkinter import *
import ogfile


def perform():
    source_path = source_in.get()
    destination_path = destination_in.get()
    ogfile.of(source_path, destination_path)
    output.grid(row=3, column=1)



window = Tk()

window.geometry("1280x720")
window.title("File Organiser ~ Krish Suthar")

source = Label(window, text='Enter address of folder which needs to be organised')
destination = Label(window, text='Enter address of where to store organised folders?')
output = Label(window, text="Files Organised Successfully!")

source.config(font=("Courier", 16))
destination.config(font=("Courier", 16))

source_in = Entry(window, width=100)
destination_in = Entry(window, width=100)

btn = Button(window, text="Organise Now", width=20, height=2, bg='blue', fg='white')
btn.config(font=("Courier", 16))
btn.config(command=perform)                             # When I add parenthese after function name, it ~gives~ Throws errorS.

source.grid(row=0, column=0)
source_in.grid(row=0, column=1)
destination.grid(row=1, column=0)
destination_in.grid(row=1, column=1)
btn.grid(row=2, column=1)


mainloop()
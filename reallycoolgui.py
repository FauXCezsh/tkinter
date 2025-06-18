from tkinter import *


count = 0

def click():
    global count
    count += 1
    label.config(text=(count))
    print(f"Button clicked {count} times")



coolwindow = Tk()
coolwindow.title("Really Cool GUI")


#label = Label(coolwindow, text="Welcome to the Really Cool GUI!")
#label.pack()


button= Button(coolwindow, text='Click this button lol!', width=20, height=5)

button.config(command=click)

button.config(bg='blue', fg='white', font=('Arial', 14, 'bold'))
button.config(activebackground='lightblue', activeforeground='black')

button.config(state=ACTIVE)

label = Label(coolwindow, text = count)
label.config(font=(25))
label.pack()

button.pack()

coolwindow.mainloop()
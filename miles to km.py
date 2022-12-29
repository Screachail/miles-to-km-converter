from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)



#Labels
label1 = Label(text="This is old text")
label1.config(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="This is old text")
label2.config(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="This is old text")
label3.config(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="This is old text")
label4.config(text="Km")
label4.grid(row=1, column=2)

#Buttons
def action():
    kilometers = round(1.609344*int(entry.get()))
    label3['text'] = f'{kilometers}'

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2,column=1)


#Entries
entry = Entry(width=7)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
entry.grid(row=0, column=1)





window.mainloop()
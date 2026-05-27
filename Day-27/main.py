from tkinter import *

# window=Tk()

# window.title("First GUI Program")
# window.minsize(500,300)

# first_label = Label(text="My First Label",font=("Arial" , 14,"bold"))
# first_label.grid(column=0,row=0)

# first_label.config(text="NEW TEXT")

# def printName():
#   newText=input.get()
#   first_label["text"] = newText

# #Button

# button = Button(text="Play" , command=printName)
# button.grid(column=1,row=1)

# new_button = Button(text="New Button")
# new_button.grid(column=2,row=0)
# new_button.config(padx=200,pady=200)

# #Entry
# input = Entry(width=10)
# input.grid(column=3,row=3)

def miles_to_km():
  miles = float(miles_input.get())
  km=miles*1.609
  kilometer_result_label.config(text=km)

window=Tk()
window.title("Miles To Km")
window.minsize(500,300)
window.config(padx=20,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text= "is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculateButton=Button(text="Calculate",command=miles_to_km)
calculateButton.grid(column=1,row=2)








window.mainloop()
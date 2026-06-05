# from tkinter import *

# def save():
#   website=website_entry.get()
#   email=email_entry.get()
#   password = password_entry.get()
#   with open("E:/CODE/100 days of Code-Python/Day-29/data.txt","a") as data_file:
#     data_file.write(f"{website} | {email} | {password}")

# window=Tk()
# window.title("Password Manager")
# window.config(padx=50,pady=50)

# canvas = Canvas(height=200,width=200)
# logo_img=PhotoImage(file="E:/CODE/100 days of Code-Python/Day-29/logo.png")
# canvas.create_image(100,100,image=logo_img)
# canvas.grid(row=0,column=1)

# website_label = Label(text="Website:", width=15, anchor="e")
# website_label.grid(row=1, column=0)

# email_label = Label(text="Email/Username:", width=15, anchor="e")
# email_label.grid(row=2, column=0)

# password_label = Label(text="Password:", width=15, anchor="e")
# password_label.grid(row=3, column=0)

# website_entry  = Entry(width=35)
# website_entry.grid(row=1,column=1,columnspan=2)
# website_entry.focus()
# email_entry=Entry(width=35)
# email_entry.grid(row=2,column=1,columnspan=2)
# email_entry.insert(0 , "xyz@gmail.com")
# password_entry=Entry(width=21)
# password_entry.grid(row=3,column=1)

# generate_password_button = Button(text="Generate Password")
# generate_password_button.grid(row=3,column=2)
# add_button = Button(text="Add",width=36,command=save)
# add_button.grid(row=4,column=1,columnspan=2)


# window.mainloop()

import tkinter as tk


def click():
  print("You Clicked The Button")

window = tk.Tk()
window.geometry("420x420")
window.title("My First GUI")


icon=tk.PhotoImage(file="E:/CODE/100 days of Code-Python/Day-29/logo.png")
window.iconphoto(True,icon)
window.config(background="#323ea8")

#label
label = tk.Label(window,text="Hello World",font = ("Arial",10,"bold"),fg="green" ,bg = "yellow" , relief=tk.RAISED,bd=10,padx=10,pady=10)
label.pack()
#button

button=tk.Button(window,text="Click Me",command=click , font=("Comic Sans",10),fg="#00ff00" ,bg="Black",activeforeground="#00ff00" ,activebackground="black")
button.pack()


#entry

def submit():
  username=entry.get()
  print(f"Hello {username}")
  entry.config(state=tk.DISABLED)

def delete():
  entry.delete(0,tk.END)

def backspace():
  entry.delete(len(entry.get())-1,tk.END)

entry=tk.Entry(window,font=("Arial",20),show="*")
entry.insert(0,"Name")
entry.pack()
submitButton=tk.Button(window,text="Submit",font=("Comic sans",10),command=submit)
submitButton.pack(side=tk.RIGHT)
endButton=tk.Button(window,text="Delete",font=("Comic sans",10),command=delete)
endButton.pack(side=tk.RIGHT)
backspace=tk.Button(window,text="Backspace",font=("Comic sans",10),command=backspace)
backspace.pack(side=tk.RIGHT)



window.mainloop()
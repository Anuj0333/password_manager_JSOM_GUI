from tkinter import *
from tkinter import messagebox
import random
import pyperclip  
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def genterate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letter+password_symbols+password_numbers

    random.shuffle(password_list)

    password ="".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0,password )
    pyperclip.copy(password)
#----------------------------FIND PASSWORD----------------------------------#

def find_password():
    website=website_entry.get()
    try:
        with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/password_manager_GUI/data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
                email= data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email:{email}\n Password:{password }")
        else:
                messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:    
         try:   
            with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/password_manager_GUI/data.json","r") as data_file:
                # f=data_file.write(f"{website} | {email} | {password}\n")
                # json.dump(new_data,data_file,indent=4)
                # Reading old data  
                data=json.load(data_file)
                
         except FileNotFoundError:
            with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/password_manager_GUI/data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
         else:
                # updating old data with new data
                data.update(new_data)
        
                with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/password_manager_GUI/data.json","w") as data_file:
                    # Saving updated data
                    json.dump(data,data_file,indent=4)
         finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

    
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("password Manager")
window.minsize(width=300,height=300)
window.config(padx=50,pady=50)

web_name=Label(text="Website:")
web_name.focus()
web_name.grid(row=1,column=0)


website_entry=Entry(width=32)
website_entry.grid(row=1,column=1)

search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)

Email_Username=Label(text="Email/Username:")
Email_Username.grid(row=2,column=0)


email_entry=Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"anujgutpa0333@gmail.com")


password_button=Button(text="Generate password",width=13,command=genterate_password)
password_button.grid(row=3,column=2)

password_label=Label(text="password:")
password_label.grid(row=3,column=0)


password_entry=Entry(width=32)
password_entry.grid(row=3,column=1)


add_button=Button(text="Add",width=43,command=save)
add_button.grid(row=4,column=1,columnspan=2)


canvas=Canvas(width=200,height=200)
lock_img=PhotoImage(file="C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/password_manager_GUI/password-manager-start/logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)


window.mainloop()
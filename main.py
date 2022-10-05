import email
from hashlib import new
from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json
window = Tk()



#------------------------------- PASSWORD GEN ----------------------------------------------------#
def gen():
    entry_pass.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [random.choice(letters) for item in range(nr_letters)]
    symbols_list = [random.choice(numbers) for item in range(nr_symbols)]
    numbers_list = [random.choice(symbols) for item in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)


    password = "".join(password_list)

    entry_pass.insert(END,string=password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


#------------------------------- SAVE DATA ----------------------------------------------------#
def save():
    website = entry_web.get()
    email = entry_email.get() 
    password = entry_pass.get()
    new_data = {

        website:{
            'email':email,
            'password':password
        }
    }

    if website != '' and email != '' and password != '':
        ensure = messagebox.askokcancel(title="waring", message=f"Please check your infomation\nwebsite:{website}  \nemail:{email} \npassword:{password}")
        if ensure == TRUE:
            
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    
                
            except FileNotFoundError:
                 
                with open("data.json","w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            
          
            else:
                with open("data.json", "w") as data_file:
                    data.update(new_data)
                    json.dump(data, data_file, indent=4)

            finally:

                messagebox.showinfo(title="Succeed", message="You password got saved ")

                entry_web.delete(0, END)
                entry_email.delete(0,END)
                entry_pass.delete(0, END)


    elif website == '' or email == '' or password == '':
        
        check_info = messagebox.showerror(title="Oops!", message="Please insert all infomation")


#------------------------------- SEARCH FUNCTION ----------------------------------------------------#
def search():
    
    key = entry_web.get()
    with open("data.json", "r") as data_file:
                    data = json.load(data_file)
    
    if key in data:
        messagebox.showinfo(title=key, message=f"email:{data[key]['email']}\npassword:{data[key]['password']}")
        messagebox.showinfo(title="Succeed", message= "the password has already been copied in clipboard")
        pyperclip.copy(data[key]['password'])

    if key not in data:
        messagebox.showerror(title='data not found', message="Sorry the information not match for any data")
    
    if len(key) == 0 :
        messagebox.showerror(title="Waring", message="Please insert the data")

    


#------------------------------- UI SETUP ----------------------------------------------------#
# note the columnspan don't work with any no idea

window.title("Password Maneger")
window.config(padx=20, pady=30)
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100, image = logo_img)
canvas.grid(column=2, row=1)


lable_web = Label(text="Website:", font=("Viva Beautiful", 12))
lable_web.grid(column=1, row=2)
entry_web = Entry(width=35)
entry_web.grid(column=2, row=2)

lable_email = Label(text="Email / Username:",font=("Viva Beautiful", 12))
lable_email.grid(column=1, row=3)
entry_email = Entry(width=35)
entry_email.grid(column=2, row=3)


lable_pass = Label(text="Password:",font=("Viva Beautiful", 12))
lable_pass.grid(column=1, row=4)
entry_pass = Entry(width=21)
entry_pass.grid(column=2,row=4)

button_gen = Button(text="Generate Password", command=gen)
button_gen.grid(column=3, row=4)

button_add = Button(text="Add", width=30, command=save)
button_add.grid(column=2, row=5, pady=5)

button_search = Button(text="Search", width=10, command=search)
button_search.grid(column=3, row=2)

lable_blank = Label(text='')
lable_blank.grid(column=4, row=1)




window.mainloop()
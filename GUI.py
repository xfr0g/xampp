import os
import webbrowser
from tkinter import *


# starts the services
def start():
    password = password_user.get()
    command = f"echo {password} | sudo -S /opt/lampp/lampp start"
    return os.system(command)


# stops the services
def stop():
    password = password_user.get()
    command = f"echo {password} | sudo -S /opt/lampp/lampp stop"
    return os.system(command)


# restarts the xampp server and mysql
def restart():
    password = password_user.get()
    command = f"echo {password} | sudo -S /opt/lampp/lampp restart"
    return os.system(command)


# opens the phpmyadmin on browser
def open_xampp():
    return webbrowser.open('https://127.0.0.1/phpmyadmin/')


# exit the program when clicked
def exit_program():
    return tk.destroy()


# initialization
tk = Tk()

# title
tk.title("XAMPP PANEL")

# label
label = Label(tk, text="XAMPP Control Panel", font=('Arial', 20, 'bold'))
label.pack()

# buttons
btn1 = Button(tk, text="Start Xampp", command=start)
btn1.place(x=50, y=80)

btn2 = Button(tk, text="Stop Xampp", command=stop)
btn2.place(x=50, y=120)

btn3 = Button(tk, text="Restart Xampp", command=restart)
btn3.place(x=50, y=160)

btn4 = Button(tk, text="Open Xampp", command=open_xampp)
btn4.place(x=50, y=200)

btn5 = Button(tk, text="Exit Xampp", command=exit_program)
btn5.place(x=50, y=240)

# password label
password_label = Label(tk, text="Enter Sudo Password")
password_label.place(x=50, y=290)

# password input field
password_user = Entry(tk)
password_user.place(x=50, y=310)
password_user.focus_set()

# geometry of frame
tk.geometry('380x450')

# runs the frame forever until closed
tk.mainloop()

# github

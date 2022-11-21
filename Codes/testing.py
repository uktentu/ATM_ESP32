import tkinter
import time
import serial

tkTop = tkinter.Tk()
tkTop.geometry("300x400")
tkTop.eval('tk::PlaceWindow . center')
tkTop.title("ESP Bank")


def check():
    ser.write(bytes("L", 'UTF-8'))
    time.sleep(2)
    for type in (["Username", "password"]):
        if type == "Username":
            ser.write(bytes(Username_Text.get(1.0, "end-1c"), 'UTF-8'))
            time.sleep(2)
        elif type == "password":
            ser.write(bytes(Password_Text.get(1.0, "end-1c"), 'UTF-8'))
            time.sleep(2)
    temp = ser.read().decode()
    if (temp != "n"):
        global account_no
        name=temp
        temp = ser.read().decode()
        while (temp != ":"):
            name += temp
            temp = ser.read().decode()
        temp = name.split(",acc=")
        account_no = temp[1]
        temp = "Succefully Loggedin\nWelcome "+temp[0]
        create_accinterface_button.place_forget()
    else:
        temp = "Invalid Credentials"
        Username_Text.delete(1.0, "end")
        Password_Text.delete(1.0, "end")
    status_variable.set(temp)
    if "Succefully Loggedin" in temp:
        removing_1st_page()
        Credit_button.pack()
        Debit_button.pack()
        Ministatement_button.pack()
        Available_balance_button.pack()


def create_accinterface():
    removing_1st_page()
    create_accinterface_button.place_forget()
    acc_hol_name_label.pack()
    acc_hol_name_Text.pack()
    Username_label.pack()
    Username_Text.pack()
    Password_label.pack()
    Password_Text.pack()
    tkLabel.pack_forget()
    RE_Password_label.pack()
    RE_Password_Text.pack()
    CreateAcc_button.pack()
    tkLabel.pack()
    back_button.place(x=20,y=350)


def creating_acc():
    hol_name = acc_hol_name_Text.get(1.0, "end-1c")
    new_username = Username_Text.get(1.0, "end-1c")
    new_pass = Password_Text.get(1.0, "end-1c")
    new_re_pass = RE_Password_Text.get(1.0, "end-1c")
    if (hol_name != "" and new_pass != "" and new_re_pass != "" and new_username != ""):
        if (new_pass == new_re_pass):
            ser.write(bytes("c", 'UTF-8'))
            time.sleep(2)
            ser.write(bytes(new_username, 'UTF-8'))
            time.sleep(2)
            ser.write(bytes(new_pass, 'UTF-8'))
            time.sleep(2)
            ser.write(bytes(hol_name, 'UTF-8'))
            time.sleep(3)
            temp = ser.read()
            if (temp.decode() == "y"):
                status_variable.set("Successfully Created!")
            elif (temp.decode() == "n"):
                status_variable.set("Username already exist , Try again!")
            else:
                status_variable.set("Try Again !!")

        else:
            status_variable.set("Password mismatched")
    else:
        status_variable.set("Some Feilds are empty check those.")


def Crediting():
    removing_2nd_page()
    Credit_label.pack()
    text_box.pack()
    Credit_enter.pack()
    status_variable.set("")
    tkLabel.pack()
    menu_button.place(x=20, y=350)


def Credit_amount():
    money = text_box.get(1.0, "end-1c")
    try:
        if (money != "" and str(int(money)) == money):
            if (account_no != -1):
                ser.write(bytes('r', 'UTF-8'))
                time.sleep(2)
                ser.write(bytes(account_no, 'UTF-8'))
                time.sleep(2)
                ser.write(bytes(str(money), 'UTF-8'))
                time.sleep(3)
                temp = ser.read()
                if (temp.decode() == "y"):
                    status_variable.set("Successfully Credited to account.")
            else:
                status_variable.set("Unable to find the Account.")
    except:
        status_variable.set("Enter Valid amount")


def Debit_amount():
    money = text_box.get(1.0, "end-1c")
    try:
        if (money != "" and str(int(money)) == money):
            if (account_no != -1):
                ser.write(bytes('d', 'UTF-8'))
                time.sleep(2)
                ser.write(bytes(account_no, 'UTF-8'))
                time.sleep(2)
                ser.write(bytes(str(money), 'UTF-8'))
                time.sleep(3)
                temp = ser.read()
                if (temp.decode() == "y"):
                    status_variable.set("Successfully Debited : "+money)
            else:
                status_variable.set("Unable to find the Account.")
    except:
        status_variable.set("Enter Valid amount")


def Debiting():
    removing_2nd_page()
    Debit_label.pack()
    text_box.pack()
    Debit_enter.pack()
    status_variable.set("")
    tkLabel.pack()
    menu_button.place(x=20, y=350)


def balance():
    removing_2nd_page()
    menu_button.place(x=20, y=350)
    tkLabel.pack_forget()
    Balance_label.pack()
    time.sleep(1)
    ser.write(bytes('b', 'UTF-8'))
    time.sleep(1)
    ser.write(bytes(account_no, 'UTF-8'))
    time.sleep(1)
    balance = ""
    i = ser.read().decode()
    while (i != ":"):
        balance += i
        i = ser.read().decode()
    status_variable.set(balance)
    tkLabel.pack()

def ministate_ment():
    removing_2nd_page()
    menu_button.place(x=20, y=350)
    tkLabel.pack_forget()
    Miinistate_label.pack()
    time.sleep(1)
    ser.write(bytes('m', 'UTF-8'))
    time.sleep(1)
    ser.write(bytes(account_no, 'UTF-8'))
    time.sleep(1)
    mini = ""
    i = ser.read().decode()
    while (i != ":"):
        mini += i
        i = ser.read().decode()
    status_variable.set(mini)
    tkLabel.pack()



def logouting():
    global account_no
    account_no = -1
    tkTop.destroy()


def removing_1st_page():
    Username_label.pack_forget()
    Username_Text.pack_forget()
    Password_label.pack_forget()
    Password_Text.pack_forget()
    Submit.pack_forget()


def removing_2nd_page():
    tkLabel.pack_forget()
    Credit_button.pack_forget()
    Debit_button.pack_forget()
    Ministatement_button.pack_forget()
    Available_balance_button.pack_forget()

def back_f():
    acc_hol_name_label.pack_forget()
    acc_hol_name_Text.pack_forget()
    RE_Password_label.pack_forget()
    RE_Password_Text.pack_forget()
    create_accinterface_button.place(x=20, y=350)
    CreateAcc_button.pack_forget()
    Submit.pack()
    status_variable.set("")
    try:
        Username_Text.delete(1.0, "end")
        Password_Text.delete(1.0, "end")
    except:
        None
    back_button.place_forget()

def menu():
    try:
        status_variable.set("")
        Debit_label.pack_forget()
        text_box.pack_forget()
        Debit_enter.pack_forget()
    except:
        None
    try:
        status_variable.set("")
        Credit_label.pack_forget()
        text_box.pack_forget()
        Credit_enter.pack_forget()
    except:
        None
    try:
        Miinistate_label.pack_forget()
    except:
        None
    try:
        Balance_label.pack_forget()
    except:
        None
    status_variable.set("")
    Credit_button.pack()
    Debit_button.pack()
    Ministatement_button.pack()
    Available_balance_button.pack()
    menu_button.place_forget()

ser = serial.Serial('/dev/cu.usbserial-0001', 9600)
acc_hol_name_label = tkinter.Label(tkTop, text="Account Holder name: ")
acc_hol_name_Text = tkinter.Text(tkTop,
                                 height=1,
                                 width=20)

Username_label = tkinter.Label(tkTop, text="Username: ")
Username_Text = tkinter.Text(tkTop,
                             height=1,
                             width=20)

Password_label = tkinter.Label(tkTop, text="Password: ")
Password_Text = tkinter.Text(tkTop,
                             height=1,
                             width=20)

RE_Password_label = tkinter.Label(tkTop, text="Re enter Password: ")
RE_Password_Text = tkinter.Text(tkTop,
                                height=1,
                                width=20)

Submit = tkinter.Button(tkTop,
                        text="Login",
                        command=check)

CreateAcc_button = tkinter.Button(tkTop,
                                  text="Create",
                                  command=creating_acc)

create_accinterface_button = tkinter.Button(tkTop,
                                            text="Create New Account",
                                            command=create_accinterface,
                                            height=1,
                                            width=12,
                                            bd=5
                                            )

back_button = tkinter.Button(tkTop,
                             text="Back",
                             height=1,
                             width=4,
                             bd=5,
                             command = back_f
                             )

menu_button = tkinter.Button(tkTop,
                             text="Menu",
                             command=menu,
                             height=1,
                             width=4,
                             bd=5
                             )

logout_button = tkinter.Button(tkTop,
                               text="Exit",
                               command=logouting,
                               height=1,
                               width=4,
                               bd=5
                               )

status_variable = tkinter.StringVar()
tkLabel = tkinter.Label(textvariable=status_variable, )

Credit_label = tkinter.Label(tkTop, text="Enter the Money of Credit")
Credit_button = tkinter.Button(tkTop,
                               text="Credit",
                               command=Crediting,
                               height=4,
                               fg="black",
                               width=9,
                               bd=5
                               )

Debit_label = tkinter.Label(tkTop, text="Enter the Money to Debit")
Debit_button = tkinter.Button(tkTop,
                              text="Debit",
                              command=Debiting,
                              height=4,
                              fg="black",
                              width=9,
                              bd=5
                              )
Credit_enter = tkinter.Button(tkTop,
                              text="Enter",
                              command=Credit_amount)
Debit_enter = tkinter.Button(tkTop,
                             text="Enter",
                             command=Debit_amount)
Miinistate_label = tkinter.Label(tkTop,
                                 text="Ministatement of last 5 transactions")
Ministatement_button = tkinter.Button(tkTop,
                                      text="MiniStatement",
                                      height=4,
                                      fg="black",
                                      width=9,
                                      bd=5,
                                      command=ministate_ment
                                      )

Balance_label = tkinter.Label(tkTop, text="Available balance")
Available_balance_button = tkinter.Button(tkTop,
                                          text="Available balance",
                                          height=4,
                                          fg="black",
                                          width=9,
                                          bd=5,
                                          command=balance
                                          )

text_box = tkinter.Text(tkTop,
                        height=1,
                        width=20)


# Username_label.grid(row=0,column=0)
# Username_Text.grid(row=0,column=1)
# Password_label.grid(row=1,column=0)
# Password_Text.grid(row=1,column=1)
# Submit.place(x=75,y=50)

# Placing the elements in order
account_no = -1
Username_label.pack()
Username_Text.pack()
Password_label.pack()
Password_Text.pack()
Submit.pack()
tkLabel.pack()
logout_button.place(x=220, y=350)
create_accinterface_button.place(x=20, y=350)

tkinter.mainloop()

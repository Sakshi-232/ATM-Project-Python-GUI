from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("600x588")
root.title("ATM MACHINE")
global pin

balance = 5000

global amt

def pin_submit():
    a = str(pin_value.get())
    if a == '1234':
        new_window(root)
    else:
        print("Entered Wrong Pin")

class new_window(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Successfully Logged In....")
        self.geometry("600x588")
        label = Label(self, text="Choose Any One From Given Options..", bg="grey", font="Hahmlet 15 bold", relief=SUNKEN)
        label.pack(fill=X,pady=20)

        one = Button(self, text="1.Balance", width="15", height="5", command=window3)
        one.pack(side="left",padx=20,pady=30)

        two = Button(self, text="2.Withdraw Balance", width="15", height="5", command=withdraw)
        two.pack(side="right")


        three = Button(self, text="3.Deposit Balance", width="15", height="5", command=deposit_amt)
        three.pack(side="left")

        four = Button(self, text="4.Exit", width="15", height="5", command=exit)
        four.pack(side="right")

class withdraw(Toplevel):
    def __init__(withdrawl, master=None):
        super().__init__(master=master)
        withdrawl.title("Successfully Logged In....")
        withdrawl.geometry("600x588")
        withdraw_amount = Label(withdrawl, text="Please Enter the amount to withdraw", font="lucida 13 bold")
        withdraw_amount.pack()

        withdrawl.withdraw_amount_value = IntVar()
        withdrawl.withdraw_amount_value.set(withdrawl.withdraw_amount_value.get())
        withdrawl.withdraw_amount_entry = Entry(withdrawl,textvariable=withdrawl.withdraw_amount_value)
        withdrawl.withdraw_amount_entry.pack()
        Button(withdrawl, text="Submit", command=withdrawl.amount_with).pack()


    def amount_with(withdrawl):
        Label(withdrawl,text=f"Your balance is {balance - withdrawl.withdraw_amount_value.get()}").pack()

        class withdraw(Toplevel):
            def __init__(withdrawl, master=None):
                super().__init__(master=master)
                withdrawl.title("Successfully Logged In....")
                withdrawl.geometry("600x588")
                withdraw_amount = Label(withdrawl, text="Please Enter the amount to withdraw", font="lucida 13 bold")
                withdraw_amount.pack()

                withdrawl.withdraw_amount_value = IntVar()
                withdrawl.withdraw_amount_value.set(withdrawl.withdraw_amount_value.get())
                withdrawl.withdraw_amount_entry = Entry(withdrawl, textvariable=withdrawl.withdraw_amount_value)
                withdrawl.withdraw_amount_entry.pack()
                Button(withdrawl, text="Submit", command=withdrawl.amount_with).pack()


            def amount_with(withdrawl):
                Label(withdrawl, text=f"Your balance is {balance - withdrawl.withdraw_amount_value.get()}").pack()


class deposit_amt(Toplevel):
    def __init__(depo, master=None):
        super().__init__(master=master)
        depo.title("Successfully Logged In....")
        depo.geometry("600x588")
        withdraw_amount = Label(depo, text="Please Enter the amount to withdraw", font="lucida 13 bold")
        withdraw_amount.pack()

        depo.deposit_amount_value = IntVar()
        depo.deposit_amount_value.set(depo.deposit_amount_value.get())
        depo.deposit_amount_entry = Entry(depo,textvariable=depo.deposit_amount_value)
        depo.deposit_amount_entry.pack()
        Button(depo, text="Submit", command=depo.amount_depo).pack()

    def amount_depo(depo):
        Label(depo,text=f"Your balance is {balance + depo.deposit_amount_value.get()}").pack()


class window3(Toplevel):
    def __init__(bal, master=None):
        super().__init__(master=master)
        bal.title("Successfully Logged In....")
        bal.geometry("600x588")
        s = str()
        Label(bal,text=f"Your Current Account Balance is {balance}").pack()

if __name__ == '__main__':
    Label(root,text="ATM MACHINE", bg = "red", font = "lucida 19 bold",padx=6,pady=9,relief=SUNKEN).grid(row=0,column=2)

    # time.sleep(3)
    Label(root,text="Please Insert Your Card", font = "licida 15 bold",padx=10,pady=10).grid(row=1,column=1)

    pin = Label(root,text="Kindly Enter Your Pin : ", font ="lucida 13 ",padx=5,pady=10).grid(row=2,column=1)

    pin_value = StringVar()
    pin_entry = Entry(root,textvariable=pin_value)
    pin_entry.grid(row=2,column=2)

    Button(text="Proceed", command=pin_submit).grid(row=3,column=2)

root.mainloop()

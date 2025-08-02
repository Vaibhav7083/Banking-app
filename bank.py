import tkinter as tk
from tkinter import messagebox

accounts = {}

#Function to create new accont
def create_account():
    account_holder = entry_name.get() 
    initial_deposite = entry_deposit.get() 

    if account_holder == "" or initial_deposite == "":
        messagebox.showwarning("inpute Error", "All fields must be filled!")
        return
    
    if not initial_deposite.isdigit():
        messagebox.showwarning("Input Error", "Deposit ammont must be a valid number")
        return
    
    initial_deposite = float(initial_deposite)

    if account_holder in accounts:
        messagebox.showwarning("Account exists ", "Account already exists")

    else:
        accounts[account_holder] = initial_deposite
        messagebox.showinfo("Success", f"Account for {account_holder} created with initial balance ${initial_deposite}!")

#Function to deposite
def deposit_money():
    account_holder = entry_name.get() 
    deposit_amount = entry_deposit.get()

    if account_holder == "" or deposit_amount == "":
        messagebox.showwarning("Input Error", "All fields must be filled")
        return
    
    if not deposit_amount.isdigit():
        messagebox.showwarning("Input Error", "Deposite amount must be valid number")
        return
    
    deposit_amount = float(deposit_amount)

    if account_holder not in accounts:
        messagebox.showwarning("Account Error", "Account does not exits!")

    else:
        accounts[account_holder] += deposit_amount
        messagebox.showinfo("Success", f"${deposit_amount} deposited to {account_holder}'s account. Current balence: ${accounts[account_holder]}")

#Function to withdraw money
def withdraw_money():
    account_holder = entry_name.get()
    withdraw_amount = entry_deposit.get()

    if account_holder == "" or withdraw_amount == "":
        messagebox.showwarning("Inpute Error", "All filed smus be filled")
        return
    
    if not withdraw_amount.isdigit():
        messagebox.showwarning("Input Error", "Withdraw amount must be a valid number!")
        return
    
    withdraw_amount = float(withdraw_amount)

    if account_holder not in accounts:
        messagebox.showwarning("Account Error", "Account does not exist!")
    elif accounts[account_holder] < withdraw_amount:
        messagebox.showwarning("Balance Error", "Insufficient funds!")
    else:
        accounts[account_holder] -= withdraw_amount
        messagebox.showinfo("Success", f"${withdraw_amount} withdraw from {account_holder}'s account. Current balance: ${accounts[account_holder]}")

#Function to check balance
def check_balance():
    account_holder = entry_name.get()
    
    if account_holder == "":
        messagebox.showwarning("Input Error", "Name field must be filled!")
        return
    
    if account_holder not in accounts:
        messagebox.showwarning("Input Error", "Account does not exits!")

    else:
        balance = accounts[account_holder]
        messagebox.showinfo("Account Balance", f"{account_holder}'s current balance is ${balance}")

#Create the main Window
root = tk.Tk()
root.title("Vp Bank")
root.configure(bg = "orange")
root.geometry("450x350")

#Labels
label_name = tk.Label(root, text="Account Holder Name")
label_name.pack(pady=10)

entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

label_deposit_withdraw = tk.Label(root, text="Amount")
label_deposit_withdraw.pack(pady=10)

entry_deposit = tk.Entry(root, width=40)
entry_deposit.pack(pady=5)

#Button for different actions 
button_create = tk.Button(root, text="Create Account", width=20, command=create_account)
button_create.pack(pady=10)

button_deposit = tk.Button(root, text="Deposit Money", width=20, command=deposit_money)
button_deposit.pack(pady=10)

button_Withdraw = tk.Button(root, text="Withdraw Money", width=20, command=withdraw_money)
button_Withdraw.pack(pady=10)

button_balance = tk.Button(root, text="Check Balance", width=20, command=check_balance)
button_balance.pack(pady=10)

#Start the main loop
root.mainloop()

import os
#print  (f"hello  {nametp}")



class budget:
    balance=0
    def __init__(self, _balance):
       self.balance = _balance


class food:
    balance=0
    def __init__(self, _balance):
        self.balance = _balance


class clothing:
    balance=0
    def __init__(self, _balance):
        self.balance = _balance


class entertainment:
    balance=0
    def __init__(self, _balance):
        self.balance = _balance


mainbudget=budget(100)
foodbudget=food(100)
clothingbudget=clothing(100)
entertainmentbudget=entertainment(100)




def deposit(category,amount):
    if category == "1":
        mainbudget.balance=mainbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    if category == "2":
            foodbudget.balance=foodbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    if category == "3":
            clothingbudget.balance=clothingbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    if category == "4":
            entertainmentbudget.balance=entertainmentbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    
def withdraw(category,amount):
    if category == "1":
        mainbudget.balance=mainbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    if category == "2":
            foodbudget.balance=foodbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    if category == "3":
            clothingbudget.balance=clothingbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    if category == "4":
            entertainmentbudget.balance=entertainmentbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    
def transfer(transferto,transferfrom,amount):
    if transferto == "1":
        mainbudget.balance=mainbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    if transferto == "2":
            foodbudget.balance=foodbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    if transferto == "3":
            clothingbudget.balance=clothingbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    if transferto == "4":
            entertainmentbudget.balance=entertainmentbudget.balance+int(amount)
    print("FUNDS DEPOSITED........")
    
    
    if transferfrom == "1":
            mainbudget.balance=mainbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    if transferfrom == "2":
            foodbudget.balance=foodbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    if transferfrom == "3":
            clothingbudget.balance=clothingbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
    if transferfrom == "4":
            entertainmentbudget.balance=entertainmentbudget.balance-int(amount)
    print("FUNDS DEPOSITED........")
    
   

def print_menu():
    os.system('cls')
    print()
    print("               Menu                   ")
    print("======================================")
    print("PRESS 1 FOR:  ----   Transfer Balance")
    print("PRESS 2 FOR:  ----   Deposit Balance ")
    print("PRESS 3 FOR:  ----   Withdraw Balance")
    print("PRESS 4 FOR:  ----   Exit")
    print("======================================")
    print("======================================")
    print(f"Main BUDGET: £  {mainbudget.balance}")
    print(f"       FOOD: £ {foodbudget.balance}  CLOTHING: £ {clothingbudget.balance}   Entertainment: £ {entertainmentbudget.balance}")
    print("======================================")
    print("======================================")
 

while True:
    print_menu()
    menu_entry=input()
    if menu_entry == "2":
        print("DEPOSIT===========WHICH CATEGORY DO YOU WANT TO DEPOSIT CHOOSE FROM BELOW")
        print("1 = MAIN BALANCE  2 = FOOD BALANCE  3 = CLOTHING BALANCE  4 = ENTERTAINMENT BALANCE")
        _category=input("ENTER YOUR CATERGORY:::")
        _amount=input("ENTER YOUR AMOUNT:::")
        deposit(_category,_amount)
        
    if menu_entry == "3":
        print("WITHDRAW===========WHICH CATEGORY DO YOU WANT TO WITHDRAW CHOOSE FROM BELOW")
        print("1 = MAIN BALANCE  2 = FOOD BALANCE  3 = CLOTHING BALANCE  4 = ENTERTAINMENT BALANCE")
        _category=input("ENTER YOUR CATERGORY:::")
        _amount=input("ENTER YOUR AMOUNT:::")
        withdraw(_category,_amount)
        
    if menu_entry == "1":
        print("TRANSFER =========== CHOOSE CATEGORIES FROM BELOW")
        print("1 = MAIN BALANCE  2 = FOOD BALANCE  3 = CLOTHING BALANCE  4 = ENTERTAINMENT BALANCE")
        _transferto=input("ENTER YOUR TRANSFER TO CATERGORY:::")
        _transferfrom=input("ENTER YOUR TRANSFER FROM CATERGORY:::")
        _amount=input("ENTER YOUR AMOUNT:::")
        transfer(_transferto,_transferfrom,_amount)
 
    if menu_entry == "4":
        print("GOOD BYE===========================")
        break
        



#name("Bruce")
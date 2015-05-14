# OOP ASSIGNMENT SHELL (Bank Account Manager)

#Your code here for 3 classes

class Accounts(object):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        amount = input("How much would you like to deposit?")
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self, amount):
        amount = input("How much would you like to withdraw?")
        if amount > self.balance:
            print("You do not have the money required for this transaction")
        else:
            self.balance = self.balance - amount
            print(self.balance)

    def Check_bal(self):
        print(self.balance)
       



class Checking(Accounts):
    def withdraw(self, amount, withdraw_amount):
        amount = int(input("How much would you like to withdraw?")
        if amount >= 100:
            new_bal = self.balance - amount
            print (new_bal)
        else:
            print ("You do not have enough money")



class Savings(Accounts):
  def interest(self):
    interest  = self.balance * 0.1
    print(interest)




print("Welcome to Ethan's ATM")
accountType = int(input("What type of account? 1:Savings; 2:Checking?"))
if accountType == 1:
    accountPicked = Savings(1500)
elif accountType == 2:
    accountPicked = Checking(1000)


#Your code here - loop asking the user what they want to do
while accountType == 1:
    option = input("What would you like to do? 1:Deposit; 2:Withdraw; 3:Check Balance 4:Calculate Interest; 5:Exit?")
    if option == 1:
        deposit = int(input("How much would you like to deposit?"))
        return accountPicked.deposit(deposit)


    elif option == 2:
        withdraw = int(input("How much would you like to withdraw?")
        return accountPicked.withdraw(withdraw)

    elif option == 3:
        return accountPicked.Check_bal()
    

    elif option == 4:
        return accountPicked.interest()

    elif option == 5:
        print ("Have a nice day!")
        break
while accountType == 2:
        option = input("What would you like to do? 1:Deposit; 2:Withdraw; 3:Check Balance; 4:Exit?")
    if option == 1:
        deposit = int(input("How much would you like to deposit?"))
        return accountPicked.deposit(deposit)


    elif option == 2:
        withdraw = int(input("How much would you like to withdraw?")
        return accountPicked.withdraw(withdraw)

    elif option == 3:
        return accountPicked.Check_bal()
    elif option == 4:
        print ("Have a nice day!")
        break

                        
     

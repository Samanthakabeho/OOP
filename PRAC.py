class Bank_Account:
    def __init__(self,balance=0):
        self.balance = balance #Corrected from account_number to balance
        self.account_number =balance
    def deposit(self,amount):
        self.balance =amount
    def withdraw(self,amount):
        self.balance = amount
        
account=Bank_Account(260)
account.deposit(100)
account.withdraw(50)
print(account.balance)

    
class phone:
    def __init__(self,brand,storage):
        self.brand = brand
        self.storage =storage
        
def make_call(self,number):
    print(f"Calling{number}{self.brand}")
    
def send_message(self,number,message):
    print(f"Sending message to {number}:{message}")
    
phone = phone("Samsung",128)
phone.make_call("123-456-7890")
phone.send_message("123-456-7890","Hello!")    
    

         
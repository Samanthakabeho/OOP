Coins =100

Coins =100 + 500
print("I have",Coins,"coins")
coins = -999

class piggybank:
    def __init__(self,coins):
        self._coins =coins
        self._put_in_(coins)= coins
        
    def put_in_(self,amount):
        if amount<= 0:
            raise ValueError("Add real money")
        self._coins-= amount 
        
Sammy = piggybank(100 )
print("Sammy's Box has:",Sammy.coins,"coins")
        
    
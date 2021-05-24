# Product class
# Product stores all atributes of a product. 
from datetime import datetime, timedelta

class Product():

    # Class attributes
    # None
    
    # Instance method
    # self is always passed by when call methodes 
    # expiration date , sell date and sell price dont need to be filled in.
    
    def __init__(self,id,name, price, date, expiration_date = "",sell_date = "",sell_price = "" ):
        
        self.id = int(id)
        self.name = name
        self.buy_price = float(price)
        self.buy_date = datetime. strptime(date, '%Y-%m-%d')  # date object
             
        # Could be empty "", if so keep empty
        if (sell_price !=""):
            self.sell_price = float(sell_price)
        else:
            self.sell_price= sell_price
    
        # check empty exp date 
        if (expiration_date !=""):
            self.expiration_date = datetime. strptime(expiration_date, '%Y-%m-%d')  # date object
        else:
            self.expiration_date= expiration_date

        # check empty sell date
        if (sell_date !=""):
            self.sell_date = datetime. strptime(sell_date, '%Y-%m-%d')  # date object
        else:
            self.sell_date =sell_date


    # when sell, product fill in sell atributes in Product instance.
    def sell(self,price,sell_date):
        self.sell_price = price
        self.sell_date = datetime. strptime(sell_date, '%Y-%m-%d')  # date object


    # test if product is expired , tested by given date.
    def isExpired(self,exp_date):

        if (exp_date !="") and (self.expiration_date !=""): # date object
            
            if (self.expiration_date < datetime.strptime(exp_date, '%Y-%m-%d') ):
                return True
            else:
                return False
        else:
            return False

    def isSold(self,date):
        if (self.sell_date !=""): 
            if (self.sell_date < datetime.strptime(date, '%Y-%m-%d') ):
                return True
            else:
                return False
            
        else:
            return False
            


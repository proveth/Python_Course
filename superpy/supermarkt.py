# Class supermarkt

from datetime import datetime, timedelta
import csv
from product_test import test_price
from product import Product

import matplotlib.pyplot as plt
import numpy as np

from collections import Counter

class Supermarkt():

    # Class attributes
    # None
    
    # Instance method
    # self is always passed by when call methodes 
    def __init__(self,name,place):
        
        self.name = name
        self.place = place
        self.inventory = []
        self.index = 0
        
    # add product to supermarkt, called in load from csv file
    def add(self,product):
        self.inventory.append(product)


    # buy object of class product
    # functions to becalled from superPy
    # shop.buy(Product(14,"garnaal",1.5,str(datetime.now().date())))
    def buyProduct(self,name,price,exp_date,buydate):

        # index is used for product id
        self.index = self.index +1
        self.inventory.append(Product(self.index,name,price,buydate,exp_date))


    # sell product 
    # update price and selldate
    def sellProductbyID(self,id,price,date):

        # search product and add sell price and date.
        p = [x for x in self.inventory if x.id == id]

        try:
            p[0].sell_price = price
            p[0].sell_date = datetime. strptime(date, '%Y-%m-%d')  # date object
        except IndexError:
            print("ERROR: Product not found")
        

    # sell product 
    # update price and selldate
    def sellProductbyName(self,name,price,date):

        # search product and add sell price and date.
        p = [x for x in self.inventory if x.name == name]

        try:
            i = 0
            while ((p[i].isExpired(date) == True) or (p[i].isSold ==True) ):
                i = i+1
                print("WARNING: Found expired product, take other product...")
        
                

            p[i].sell_price = price
            p[i].sell_date = datetime. strptime(date, '%Y-%m-%d')  # date object
            print("OK Sold")
        except IndexError:
            print("ERROR: Product not found")



    def findProductByName(self,name):
        return [x for x in self.inventory if x.name == name]

    def findProductByNearestExpiredate():
        pass


    def printColumn(self,list):
    
        # 22 characters are in 1 columnwidth
        row_data = "|"
        row_line = '+'
        for i in list:
            l = len(i)
            row_line = row_line + 20 * "-" + "--+"
            row_data = row_data + (20-l)*" "+ i +"  |"

        #print(row_line)
        print(row_data)
        print(row_line)


    def printHeader(self,list):

        # 23 characters are in 1 columnwidth
        row_data = "|"
        row_double_line = "+"

        for i in list:
            l = len(i)
            
            row_data = row_data + (20-l)*" "+ i +"  |"
            row_double_line = row_double_line + 20 * "=" + "==+"

        
        print(row_double_line)
        print(row_data)
        print(row_double_line)



    def printWholeInventoryList(self):

        self.printHeader(["Id","Product","buy Price"," buy Date","Exp. Date","Sell date","Sell price"])

        for i in self.inventory:
            
            # check if date is empty 
            if i.expiration_date == "":
                exp_d = ""
            else:
                exp_d = str(i.expiration_date.date())

                        # check if date is empty 
            if i.sell_date == "":
                sell_d = ""
            else:
                sell_d = str(i.sell_date.date())
                

            self.printColumn([str(i.id),i.name, str(i.buy_price), str(i.buy_date.date()),exp_d, sell_d , str(i.sell_price)])
        print("")
            


    def printCurrentInventoryList(self,date):
        
        self.printHeader(["Id","Product","buy Price"," buy Date","Exp. Date"])

        for i in self.inventory:
            
            # check if date is empty 
            if i.expiration_date == "":
                exp_d = ""
            else:
                exp_d = str(i.expiration_date.date())

        # check if is sold already and at which date.
        
            if i.sell_date != "":
                if (date <= i.sell_date) and (date > i.buy_date):
                    self.printColumn([str(i.id),i.name, str(i.buy_price), str(i.buy_date.date()),exp_d])
            else:
                if (date > i.buy_date):
                    self.printColumn([str(i.id),i.name, str(i.buy_price), str(i.buy_date.date()),exp_d])
        print("")



    def plotCurrentInventoryList(self,date):
        
        mylabels = [] # fill by product names
        #amount = np.array[]

        for i in self.inventory:
            
            # check if date is empty 
            if i.expiration_date == "":
                exp_d = ""
            else:
                exp_d = str(i.expiration_date.date())

        # check if is sold already and at which date.
        
            if i.sell_date != "":
                if (date <= i.sell_date) and (date > i.buy_date):
                    # add to list
                    mylabels.append(i.name)
            else:
                if (date > i.buy_date):
                    # Add to list
                    mylabels.append(i.name)

        # count product names
        setProducts = Counter(mylabels)
        
        plt.bar(setProducts.keys(), setProducts.values())
        #plt.pie(setProducts.values(),labels = setProducts.keys() )
        plt.show() 


    def printRevenue(self,date):

        # check if sold from date or later 
        revenue = 0.0

        for i in self.inventory:
        # check if is sold already and at which date.
        
            if i.sell_date != "":
                if (date >= i.sell_date):
                    revenue = revenue + i.sell_price

        print(" Revenue from "+ str(date.date()) +" is : "+ str(revenue) )

    def printProfit(self,date):
        # check if sold from date or later 
        profit = 0.0

        for i in self.inventory:
        # check if is sold already and at which date.
        
            if i.sell_date != "":
                if (date >= i.sell_date):
                    profit = profit + i.sell_price - i.buy_price

        print(" Profit from "+ str(date.date()) +" is : "+ str(profit) )
        





    # init the supermarkt inventary list by loading the CSV file.
    def init(self,filename):  


        # Open file and print data only
        # raise FileNotFoundError when file not exits
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter = ';')

            # increase index by 1 , skipp header
            next(csv_reader)

            for line in csv_reader:
                #print(line)

                # increase index ( ID product)
                self.index= self.index +1
                
                # id,name, price, date, expiration_date = None,sell_date = None,sell_ = None .
                self.add(Product(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))


    def save(self,filename):
        # Open new file
        # To write data use a tupple (var1,var2) or List [,]
        with open(filename,'w', newline = "") as new_file:
            csv_writer = csv.writer(new_file, delimiter = ';')
            csv_writer.writerow(["ID","Product Name","Buy Price","Buy date","Expiration date","Sell date","Sell Price" ])

            for i in self.inventory:
                
                # check if date is empty 
                if i.expiration_date == "":
                    exp_d = ""
                else:
                    exp_d = str(i.expiration_date.date())

                            # check if date is empty 
                if i.sell_date == "":
                    sell_d = ""
                else:
                    sell_d = str(i.sell_date.date())
                    

                csv_writer.writerow([str(i.id),i.name, str(i.buy_price), str(i.buy_date.date()),exp_d, sell_d , str(i.sell_price)])
# Do not change these lines. Used by Winc Academy
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

# Imports
import argparse
import csv

from datetime import date, datetime, timedelta

import sys


from product import Product
from supermarkt import Supermarkt



# date id file not exist use current date , else use date from file

# Open file with write permision
file = open("date.txt","r")
s= file.readline()
current_date = datetime.strptime(s, '%Y-%m-%d')
file.close()



shop = Supermarkt("C1000", "Utrecht")

shop.init("data.csv")

#shop.printWholeInventoryList()


def buy(args):
    #print(args.product_name)
    #print(args.price)
    #print(args.expiration_date)

    if (args.product_name == None) :  args.product_name = "unknown"
    if (args.price == None) :  args.price = 0
    if (args.expiration_date == None) :  args.expiration_date = ""
    
    shop.buyProduct(args.product_name,args.price,args.expiration_date,str(current_date.date()))
    print("OK Bought")

def sell(args):
    
    #shop.sellProductbyID(4,0.20,"2023-06-06")
    shop.sellProductbyName(args.product_name,args.price,str(current_date.date()))
    


def change_date(args):
    global current_date 
    if (args.date == "today") or (args.date == None):
        date = current_date
    elif (args.date == "yesterday"):
            date = current_date + timedelta(days = -1)
    elif (args.date == "tommorrow"):
            date = current_date + timedelta(days = 1)
    else:
        date = datetime. strptime(args.date, '%Y-%m-%d')  # date object

    
    current_date = date
    # Open file with write permision
    file = open("date.txt","w")
    file.write(str(current_date.date()))

    file.close()



    # save to text file.

    print("OK  date change to :" + str(current_date.date()))


def report(args):
    global current_date 
    if (args.date == "today") or (args.date == None):
        date = current_date
    elif (args.date == "yesterday"):
            date = current_date + timedelta(days = -1)
    elif (args.date == "tommorrow"):
            date = current_date + timedelta(days = 1)
    else:
        date = datetime. strptime(args.date, '%Y-%m-%d')  # date object


    if args.reportdetail =="total_list":
        shop.printWholeInventoryList()

    if args.reportdetail =="inventory":
        shop.printCurrentInventoryList(date)

    if args.reportdetail =="plot":
        shop.plotCurrentInventoryList(date)
        print("OK , close plot to continue...")

    if args.reportdetail =="revenue":
        shop.printRevenue(date)

    if args.reportdetail =="profit":
        shop.printProfit(date)


# Parser to intepret the arguments via command prompt 
def argument_parser():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--cmd")
    

    subparser = parser.add_subparsers()

    # create subparsers : buy orange --price 1.20 --expiration_date 2020-05-01 , default values so that None not happens.
    buyparser = subparser.add_parser("buy",help="buy in product")
    buyparser.add_argument("--product_name", nargs='?', const="Unkown", type=str)
    buyparser.add_argument("--price", nargs='?', const=0.0, type=float)
    buyparser.add_argument("--expiration_date", nargs='?', const="", type=str)
    buyparser.set_defaults(func= buy)

    # create subparsers : sell orange --price 1.20  , default values so that None not happens.
    sellparser = subparser.add_parser("sell",help="sell product")
    sellparser.add_argument("--product_name", nargs='?', const="Unkown", type=str)
    sellparser.add_argument("--price", nargs='?', const=0.0, type=float)
    sellparser.set_defaults(func= sell)
    
    # create subparsers : sell orange --price 1.20  , default values so that None not happens.
    reportparser = subparser.add_parser("report",help="reports")
    reportparser.add_argument("reportdetail", nargs='?', const= "total_list", type=str)
    reportparser.add_argument("--date", nargs='?', const= str(current_date.date()), type=str)
    reportparser.set_defaults(func= report)
    
    # create subparsers : change date  , default values so that None not happens.
    reportparser = subparser.add_parser("date_change",help="change the date")
    reportparser.add_argument("--date", nargs='?', const= str(current_date.date()), type=str)
    reportparser.set_defaults(func= change_date)
 


    # get arguments and call function from command 
    args = parser.parse_args()
    args.func(args)
    







# required , -- optional (default None)
if __name__ == '__main__':
    
    argument_parser()

    #shop.printWholeInventoryList()
    shop.save("data.csv")
#################################################
#     TEST FUNCTIONS
#################################################

# import main.py 
from superpy import *
import os



def test_buy():

   # Open file with write permision
    file = open("date.txt","w")
    file.write(str(datetime.now().date()))
    file.close()

    stream = os.popen('superpy.py buy --product_name Orange --price 2.00 --expiration_date 2022-01-01')
    output = stream.read()
    assert str(output) == "OK Bought\n"
    
def test_sell():
    stream = os.popen('superpy.py sell --product_name Orange --price 3.00')
    output = stream.read()
    assert str(output) == "OK Sold\n"

def test_profit():
    stream = os.popen('superpy.py report profit')
    output = stream.read()
    assert str(output) == " Profit from "+ str(datetime.now().date()) +" is : 1.0\n"

def test_revenue():
    stream = os.popen('superpy.py report revenue')
    output = stream.read()
    assert str(output) == " Revenue from "+ str(datetime.now().date()) +" is : 3.0\n"

def test_change_date():

    stream = os.popen('superpy.py buy --product_name milk --price 2.00 --expiration_date 2022-01-01')
    output = stream.read()

    stream = os.popen('superpy.py date_change --date 2023-01-01')
    output = stream.read()
    assert str(output) == "OK  date change to :2023-01-01\n"


def test_sell_not_available():
    stream = os.popen('superpy.py sell --product_name Niks --price 3.00')
    output = stream.read()
    assert str(output) == "ERROR: Product not found\n"


def test_sell_expired():
    
    stream = os.popen('superpy.py sell --product_name milk --price 3.00')
    output = stream.read()
    assert str(output) == "WARNING: Found expired product, take other product...\nERROR: Product not found\n"
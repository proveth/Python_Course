# Test module for Product class

from product import Product
from datetime import datetime, timedelta

def test_id():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.id == 1

def test_name():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.name == "Orange"

def test_price():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.buy_price == 0.23


def test_buy_date():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.buy_date == datetime.strptime("2020-01-01", '%Y-%m-%d')  # date object

def test_sell_price():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.sell_price == ""


def test_exp_date():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.expiration_date == ""

def test_sell_date():
    P1 = Product(1,"Orange",0.23,"2020-01-01")
    assert P1.sell_date == ""

def test_exp_date_2():
    P1 = Product(1,"Orange",0.23,"2020-01-01","2020-01-02","2020-01-05",1.20)
    assert P1.expiration_date == datetime.strptime("2020-01-02", '%Y-%m-%d')  # date object

def test_sell_date_2():
    P1 = Product(1,"Orange",0.23,"2020-01-01","2020-01-02","2020-01-05",1.20)
    assert P1.sell_date == datetime.strptime("2020-01-05", '%Y-%m-%d')  # date object

def test_sell_price_2():
    P1 = Product(1,"Orange",0.23,"2020-01-01","2020-01-02","2020-01-01",1.20)
    assert P1.sell_price == 1.20


def test_is_expired_1():
    P1 = Product(1,"Orange",0.23,"2020-01-01","2021-01-02","2020-01-01",1.20)
    print(P1.isExpired("2020-01-01") )
    assert P1.isExpired("2020-01-01") == False

def test_is_expired_2():
    P1 = Product(1,"Orange",0.23,"2020-01-01","2021-01-02","2020-01-01",1.20)
    print(P1.isExpired("2020-01-01") )
    assert P1.isExpired("2021-01-03") == True
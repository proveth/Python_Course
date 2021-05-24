# test for date

from datetime import datetime, timedelta
import time

# 2021-05-09 21:30:41.252910
x = datetime.now()

print(x)

print(x.year)               #year 2021
print(x.strftime("%A"))     #Day
print(x.strftime("%C"))     #Month

# Create date time object
x2 = datetime(2020, 5, 17)
print(x2)

# 17:40:00
start = datetime.now()
time.sleep(1.2)
end = datetime.now()

delta = end -start
print("delta: " + str(delta))


# Calculating future dates
# for two years
# Using current time
ini_time_for_now = datetime.now()
future_date_after_2yrs = ini_time_for_now + \
                        timedelta(days = 730)
  
future_date_after_2days = ini_time_for_now + \
                         timedelta(days = 2)
  
# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))

print(datetime.now().date())

import csv

# Open file append data
# To write data use a tupple (var1,var2) or List [,]
with open('data.csv','a',newline = "") as new_file:
    csv_writer = csv.writer(new_file, delimiter = ';')
    
    for i in range(0,5):
        csv_writer.writerow(["Python","MainStreet 17 ", i,None,6])

# Open file and print header and data
# raise FileNotFoundError when file not exits
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ';')

    for line in csv_reader:
        print(line)
        print(line[3]=="")

x =datetime.strptime("2021-05-03", '%Y-%m-%d')  # date object
print(x)

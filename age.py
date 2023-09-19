# Programme that, given the date, calculates the number of years between any of the dates
from datetime import datetime

today_date = "2023/09/19"
calc_date = input('Input a date in the format YYYY/MM/DD: ')\

# need to turn into strings
date1 = datetime.strptime(today_date, "%Y/%m/%d")
date2 = datetime.strptime(calc_date, "%Y/%m/%d")

diff = date2 - date1
print(f'The difference between the two dates is {diff}')

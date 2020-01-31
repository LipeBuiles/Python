#own modules
#thirdy party modules
#python modules

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=60))

from datetime import timedelta, date
print(timedelta(minutes=60))
print(date.today())

import Tmath
Tmath.add(1,2)
Tmath.substract(1,1)

from Tmath import add, substract
substract(10,5)
add(9,6)

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello Pinche Pastel")
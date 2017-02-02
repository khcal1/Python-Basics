# This program is a simple random number generator

import os
import sys
import random


random_num = random.randrange(0,100)

while(random_num != 45):
    print(random_num)
    random_num = random.randrange(0,100) #changes number each time

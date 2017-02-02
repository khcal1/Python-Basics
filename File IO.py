# This program displays how to create and open a file

import os
import sys
import random


test_file = open("test.txt" , "wb" )
print(test_file.mode) #output file mode
print(test_file.name) #prints file name

test_file.write(bytes("write me to file \n ", 'UTF-8'))

test_file.close()




#To read the previously closed file

test_file = open("test.txt" , 'rt')
text_in_file = test_file.read()
print(text_in_file)



#Delete the file

#os.remove("test.txt")
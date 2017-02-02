# Use a while loop and 3 for loops to make a diagram of a tree based on user input
                        #
                       ###
                      #####
                     #######
                    #########
                        #




import os
import sys
import random

tree_height = input("How tall is the tree: ")
tree_height = int(tree_height)


# Starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stom places for later
stump_spaces =  tree_height - 1

while tree_height !=0:
    for i in range(spaces):
        print(' ', end ='')

    for i in range(hashes):
        print('#', end ='')

    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end ='')

print('#')
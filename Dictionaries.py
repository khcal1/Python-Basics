# This program displays the basic creation and use of a dictionary

import os
import sys
import random

super_heroes = {'Batman': 'Bruce Wayne',
                  'Superman': 'Clark Kent',
                  'Wonder Woman': 'Diana',
                   'Flash': 'Barry Allen',
                   'Green Lantern': 'Hal Jordan'}

print(super_heroes)
print('\n')

'''Print all names
   Print all identities
   Print one single name
   Replace Wonder Woman with Aquaman'''

print(super_heroes.keys())
print('\n')
print(super_heroes.values())
print('\n')
print(super_heroes['Batman'])
print('\n')
super_heroes['Aquaman'] = 'Aruthur Curry'
del super_heroes['Wonder Woman']

print(super_heroes)
print('\n')



#Print all Identities using a for loop

for p in super_heroes.values():
    print(p.title())
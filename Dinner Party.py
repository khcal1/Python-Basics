'''This program displays the uses of List
    Start by inviting three people to a dinner party'''

import os
import sys
import random


guest_list = ['Socrates', 'King Tutt', 'Bas']

for guest in guest_list:
    print("{}, Welcome to the party.".format(guest))





'''One person cannot make it to the party.
Delete that person fromt he list and make a new one
inviting someone else and reprint the list'''

print("\nBas cannot make it to the party.\n")

guest_list.remove('Bas')

guest_list.append('Rihanna')

for guest in guest_list:
    print("{}, Welcome to the party.".format(guest))






#A bigger dinner table was found. Invite three more guests to the party



guest_list.append('Papa Johns')
guest_list.insert(2,'Judy')
guest_list.insert(3,'Khalil')

print("\n")
for guest in guest_list:
    print("{}, Welcome to the party.".format(guest))




'''You just found out you can only invite two guest.
Print a message that apologizes to the guests you cannot invite
while using the pop method to remove the guests from the list telling them they cannot come.
After you are done empty the list and print it'''

print('\n')


uninvited = guest_list.pop()
print("Sorry {}, you are not invited".format(uninvited))
uninvited = guest_list.pop()
print("Sorry {}, you are not invited".format(uninvited))
uninvited = guest_list.pop()
print("Sorry {}, you are not invited".format(uninvited))
uninvited = guest_list.pop()
print("Sorry {}, you are not invited".format(uninvited))

print("\n")
for guest in guest_list:
    print("{}, you are still invited.".format(guest))

print("\n")
guest_list.remove('Socrates')
guest_list.remove('King Tutt')
print(guest_list)


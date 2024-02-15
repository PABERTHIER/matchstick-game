# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:02:11 2017

@author: Pierre-Antoine
"""

# This file contains a variation of the matches game where two players take turns playing against each other.
import random

num_matches = int(input("Enter the number of matches: "))

player = random.randint(1, 2)

print("Remaining matches:", num_matches)

while num_matches > 0:
    for _ in range(num_matches):
        print("|", end='')
    print()
        
    print("- It's Player's turn:", player)
    print("Remaining matches:", num_matches)
    pick = int(input("Enter the number of matches to pick (1 to 3): ")) 
          
    while pick not in range(1, 4):
        pick = int(input("You did not enter a number between 1 and 3 (inclusive): "))
        
    num_matches -= pick
    player = player % 2 + 1

    if num_matches < 1:
        print("Player", player, "wins!")

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:02:11 2017

@author: Pierre-Antoine
"""

# This file contains the code for a simple matches game where one player plays against the computer or takes turns against another player.

num_matches = int(input("Enter the number of matches: "))
num_players = int(input("Enter the number of players: "))

while num_matches > 0:
    print(num_matches, "- Player :", num_players)
    pick = int(input("Enter the number of matches to pick (1 to 3): "))
    
    while not 1 <= pick <= 3:
        pick = int(input("You did not enter a number between 1 and 3 (inclusive): "))
        
    num_matches -= pick
    num_players = num_players % 2 + 1

    if num_matches < 1:
        print("Player", num_players, "wins!")

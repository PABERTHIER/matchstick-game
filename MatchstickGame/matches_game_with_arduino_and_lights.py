# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:02:11 2017

@author: Pierre-Antoine
"""

# This file extends the matches game with Arduino by adding light indicators to enhance the gaming experience.

import pyfirmata
import time

port = 'COM7'
board = pyfirmata.Arduino(port)
switch_pin = board.get_pin('d:11:i')
iterator = pyfirmata.util.Iterator(board)
iterator.start()
switch_pin.enable_reporting()
L1_pin = board.get_pin('d:13:o')
L2_pin = board.get_pin('d:12:o')

num_matches = int(input("Enter the number of matches: "))
num_players = int(input("Enter the number of players: "))

if num_players == 1:
    L1_pin.write(1)
    time.sleep(2.5)
    L1_pin.write(0)
else: 
    L2_pin.write(1)
    time.sleep(2.5)
    L2_pin.write(0)

while num_matches > 0:
    if num_players == 1:
        L1_pin.write(1)
        time.sleep(2.5)
        L1_pin.write(0)
    else: 
        L2_pin.write(1)
        time.sleep(2.5)
        L2_pin.write(0)
        
    print("- Player :", num_players)
    pick = int(input("Enter the number of matches to pick (1 to 3): "))

    while not 1 <= pick <= 3:
        pick = int(input("You did not enter a number between 1 and 3 (inclusive): "))

    num_matches -= pick
    num_players = num_players % 2 + 1
    
    if num_matches < 1:
        print("Player", num_players, "wins!")
        if num_players == 1:
            for _ in range(1, 5):
                L1_pin.write(1)
                time.sleep(0.5)
                L1_pin.write(0)
                time.sleep(0.5)
        else:
            for _ in range(1, 5):
                L2_pin.write(1)
                time.sleep(0.5)
                L2_pin.write(0)
                time.sleep(0.5)

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:02:11 2017

@author: Pierre-Antoine
"""

# This file incorporates Arduino functionality into the matches game, making it interactive with physical components.

from random import randrange
import pyfirmata
import time

port = 'COM7'
match_sensor_active = 0
match_taken_flag = 1
board = pyfirmata.Arduino(port)
switch_pin = board.get_pin('d:12:i')
iterator = pyfirmata.util.Iterator(board)
iterator.start()
switch_pin.enable_reporting()  
start_time = time.clock()
end_time = start_time

def match_counter():
    match_sensor_active = 0
    matches_taken = 0
    match_taken_flag = 1
    start_time = time.clock()
    end_time = time.clock()
    print("You have 5 seconds to take the match(es)")

    while end_time - start_time < 5:
        match_value = switch_pin.read()
        if match_value != 0.0 and match_sensor_active == 0:
            match_sensor_active = 1
            match_taken_flag = 0

        if match_value == 0.0 and match_taken_flag == 0:
            match_taken_flag = 1
            match_sensor_active = 0
            matches_taken += 1
        end_time = time.clock()

    if matches_taken <= 1:
        return 1
    elif matches_taken == 2:
        return 2
    elif matches_taken >= 3:
        return 3

num_players = int(input("Enter the number of players: "))

while num_players > 2 or num_players < 1:
    num_players = int(input("Enter the number of players: "))

if num_players == 2:
    player_turn = randrange(1, 2)
    num_matches = int(input("Enter the number of matches: "))

    while num_matches > 0:
        print(num_matches * "|")
        print("Player", player_turn)
        matches_taken = match_counter()
        print("You took", matches_taken, "match(es)")
        print(num_matches * "|")
        num_matches -= matches_taken
        player_turn = player_turn % 2 + 1

        if num_matches < 1:
            print("Player", player_turn, "wins!")

if num_players == 1:
    print("Choose difficulty level: 1: Normal  2: Difficult")
    difficulty_level = int(input())

    while difficulty_level < 1 or difficulty_level > 2:
        difficulty_level = int(input())

    if difficulty_level == 1:
        num_matches = int(input("Enter the number of matches: "))

        while num_matches > 0:
            print(num_matches * "|")
            matches_taken = match_counter()
            print("You took", matches_taken, "match(es)")
            num_matches -= matches_taken
            print(num_matches * "|")

            if num_matches <= 1:
                print("Player wins!")
                break

            if num_matches > 3:
                computer_matches = randrange(1, 3)

            if num_matches == 3:
                computer_matches = 2

            if num_matches == 2:
                computer_matches = 1

            num_matches -= computer_matches
            print("The computer took", computer_matches, "match(es)")
            print(num_matches * "|")

            if num_matches <= 1:
                print("The computer wins!")
                break

    if difficulty_level == 2:
        num_matches = int(input("Enter the number of matches: "))

        while num_matches > 0:
            print(num_matches * "|")
            matches_taken = match_counter()
            print("You took", matches_taken, "match(es)")
            num_matches -= matches_taken
            print(num_matches * "|")

            if num_matches <= 1:
                print("Player wins!")
                break

            computer_matches = 4 - matches_taken
            num_matches -= computer_matches
            print("The computer took", computer_matches, "match(es)")
            print(num_matches * "|")

            if num_matches <= 1:
                print("The computer wins!")
                break

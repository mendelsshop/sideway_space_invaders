import os
import random
import time
import keyboard
key_p = ''
z = 0
shoot = False
# create a list of 50 ' 's using a list comprehension
# the list comprehension will create a list of 50 ' 's
# the list comprehension will then be assigned to the variable 'board'

row = [' '] * 50
row.append('<')
# make a list called 'board' and assign it 5 'row'
board = [row] * 5

for i in range(50):
    
    time.sleep(.1)
    os.system("cls")
    
    print("-" * 51)
    # print board as a string
    for row in board:
        print("".join(row))
    print('-' * 51)

    key_p = ''
    shoot = False
    timer = time.time()
    while (time.time() - timer < 1):
        # if the 2 seconds have passed, quit the loop
        if keyboard.is_pressed("up"):
            
            key_p = 'up'
        elif keyboard.is_pressed("down"):
            
            key_p = 'down'
        if keyboard.is_pressed("space"):
            shoot = True
    

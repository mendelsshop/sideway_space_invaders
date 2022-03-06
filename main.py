import os
import random
import time
import keyboard
key_p = ''
player_ps = random.randrange(5)
shoot = False
prev_player_pos = None

# make a list called 'board' and assign it 5 'row'
board = {'row1': [' '] * 50, 'row2': [' '] * 50, 'row3': [' '] * 50, 'row4': [' '] * 50, 'row5': [' '] * 50}
#  for each row in the dictionary 'board' append the '<' to the end of the row
for row in board:
    board[row].append('<')

for i in range(50):
    
    time.sleep(.1)
    os.system("cls")
    if key_p == 'up' and prev_player_pos != 0:
        player_ps -= 1
    elif key_p == 'down' and prev_player_pos != 4:
        player_ps += 1
    else:
        player_ps = random.randrange(5)
    if shoot == True:
        pass
    print ("player_ps:", (player_ps+1,i))
    if prev_player_pos != None:
        print ("player_ps:", (prev_player_pos+1,prev_i))
        board['row' + str(prev_player_pos+1)][prev_i] = ' '
    
    board['row' + str(player_ps+1)][i] = 'O'

    print("-" * 51)

    for rows in board:
        print("".join(board[rows]))
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
    prev_player_pos = player_ps
    prev_i = i
    

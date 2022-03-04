import os
import random
import time
import keyboard
key_p = ''
z = 0
shoot = False
for i in range(50):
    
    time.sleep(.1)
    os.system("cls")
    
    print("-" * 51)
    if key_p == 'up' and z > 0:
        # move up the 'o relative to varaible z
        z -= 1 
        for k in range(z):
            print(' ' * 49, '<')
        if i == 49:
            print(' ' * 48, 'o<')
        elif i == 48:
            print(' ' * 47, 'o <')
        else:
            print((i * ' ') + 'o', end=' ')
            if shoot:
                left = 47 - i
                if left % 2 == 0:
                    left_left = int(left / 2)
                    left_right = int(left_left)
                else:
                    left_left = int((left - 1) / 2)
                    left_right = int(left/ 2) + 1
                print(' ' * left_right + '-' + ' ' * left_left + '<')

            else:
                print((' ' * (46 - i)), ' <')
        for j in range(4 - z):
            print(' ' * 49, '<')
    elif key_p == 'down' and z < 4:
        # move down the 'o relative to variable z
        z += 1
        for k in range(z):
            print(' ' * 49, '<')
        if i == 49:
            print(' ' * 48, 'o<')
        elif i == 48:
            print(' ' * 47, 'o <')
        else:
            print((i * ' ') + 'o', end=' ')
            if shoot:
                left = 47 - i
                if left % 2 == 0:
                    left_left = int(left / 2)
                    left_right = int(left_left)
                else:
                    left_left = int((left - 1) / 2)
                    left_right = int(left/ 2) + 1
                print(' ' * left_right + '-' + ' ' * left_left + '<')

            else:
                print((' ' * (46 - i)), ' <')
        for j in range(4 - z):
            print(' ' * 49, '<')

    else:
        z = random.randrange(5)
        for k in range(z):
            print(' ' * 49, '<')
        if i == 49:
            print(' ' * 48, 'o<')
        elif i == 48:
            print(' ' * 47, 'o <')
        else:
            print((i * ' ') + 'o', end=' ')
            if shoot:
                left = 47 - i
                if left % 2 == 0:
                    left_left = int(left / 2)
                    left_right = int(left_left)
                else:
                    left_left = int((left - 1) / 2)
                    left_right = int(left/ 2) + 1
                print(' ' * left_right + '-' + ' ' * left_left + '<')

            else:
                print((' ' * (46 - i)), ' <')

        for j in range(4 - z):
            print(' ' * 49, '<')

    print('-' * 51)
    # print(key_p)
    key_p = ''
    shoot = False
    # 
    timer = time.time()
    while (time.time() - timer < 1):
        # if the 2 seconds have passed, quit the loop
        
        if keyboard.is_pressed("up"):
            # print("up")
            key_p = 'up'
        elif keyboard.is_pressed("down"):
            # print("down")
            key_p = 'down'
        if keyboard.is_pressed("space"):
            shoot = True
    

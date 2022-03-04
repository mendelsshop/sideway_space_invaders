import os
import random
import time
import keyboard
key_p = ''
for i in range(50):
   
    time.sleep(.1)
    os.system("cls")
    
    print("-" * 51)
    z = random.randrange(5)
    for k in range(z):
        print(' ' * 49, '<')
    if i == 49:
        print(' ' * 48, 'o<')
    elif i == 48:
        print(' ' * 47, 'o <')
    else:
        print((i * ' ') + 'o', (' ' * (47 - i)), '<')  
    for j in range(4 - z):
        print(' ' * 49, '<')

    print('-' * 51)
    print(key_p)
    if keyboard.is_pressed('q'):
        break
    elif keyboard.is_pressed("up"):
        key_p = 'up'
    elif keyboard.is_pressed("down"):
        key_p = 'down'
    

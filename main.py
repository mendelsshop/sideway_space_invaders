import os
import random
import time
import sys
import keyboard

clears = "clear" if os.name == "posix" else "cls"
bullet_speed = 0.01 if os.name == "posix" else 0.000000000000000001
# make a variable for the length and height of the board so we can change it for different levels
# move most of the from here to somewhere else in src/ to make more modular
# make a function to display the board instead of doing it in three lines each time
# change it from a dictionary of lists to list list of lists


def readme():
    with open("README.txt", "r") as f:
        return f.read().format("⦓")


def clear(times):
    time.sleep(times)
    os.system(clears)


def create_board(x, y):
    board = [[" " for i in range(x)] for j in range(y)]
    enemy_pos = []
    for enemy_y in range(y):
        enemy_x = random.randrange(x - 6, x)
        enemy_pos.append([enemy_x, enemy_y])
    board = clear_enemys(board, range(44, 51), enemy_pos)
    return [board, enemy_pos]


def locate_min(list):
    smallest = min(list)
    return [index for index, element in enumerate(list) if smallest == element]


def best_place(enemy_pos):
    ys = [0, 0, 0, 0, 0]
    for enemy in enemy_pos:
        ys[enemy[1]] += 1
    return random.choice(locate_min(ys))


def clear_enemys(board, enemy_range, enemy_pos):
    for row in board:
        for enemy in enemy_range:
            if row[enemy] == "<":
                row[enemy] = " "
    for enemy in enemy_pos:
        board[enemy[1]][enemy[0]] = "<"
    return board


def spawan_enemys(board, enemy_pos):
    for i in range(random.randrange(0, 3)):
        x = random.randrange(44, 51)
        y = best_place(enemy_pos)
        if board[y][x] == "<":
            if y == 4:
                y = 0
            else:
                y += 1
        enemy_pos.append([x, y])
    if len(enemy_pos) > 10:
        while len(enemy_pos) > 7:
            enemy_pos.pop(len(enemy_pos) - 1)
    if len(enemy_pos) < 5:
        for i in range(5 - len(enemy_pos)):
            enemy_pos.append([random.randrange(44, 51), best_place(enemy_pos)])
    board = clear_enemys(board, range(44, 51), enemy_pos)
    return [board, enemy_pos]


clear(0)
print(readme())
print("press enter to start or q to quit")
while True:
    key = keyboard.is_pressed()
    if key == "enter":
        break
    elif key == "q":
        exit()
key_p = ""
player_ps = random.randrange(5)
shoot = False
prev_player_pos = None
board, enemy_pos = create_board(51, 5)
# if the '-' collides with '<' then '<' is destroyed
# if 'O' reaches the end of the board than you win the game
#  for each row in the dictionary 'board' append the '<' to the end of the row
len_board = len(board)


for i in range(51):
    clear(0.1)
    if key_p == "up" and prev_player_pos != 0:
        player_ps -= 1

    elif key_p == "down" and prev_player_pos != 4:
        player_ps += 1

    else:
        player_ps = random.randrange(5)

    if board[player_ps][i] == "<":
        board[prev_player_pos][prev_i] = ""
        board[player_ps][i] = "⦓"
        print("-" * 51)
        for row in range(len_board):
            print("".join(board[row]))
        print("-" * 51)
        print("You lose!")
        break

    if prev_player_pos != None:
        board[prev_player_pos][prev_i] = " "

    board[player_ps][i] = "O"
    if shoot:
        print("".join(board[rows]))
        print("-" * 51)
        prev_b = 0
        bulet = i + 1
        while bulet < 51:
            os.system(clears)
            print("-" * 51)
            for rowss in range(len_board):
                if board[player_ps] == board[rowss]:
                    # check if the current bulet position is the as "<"
                    if board[rowss][bulet] == "<":
                        enemy_pos.remove([bulet, rowss])
                        board, enemy_pos = spawan_enemys(board, enemy_pos)
                    board[rowss][bulet] = "-"
                    if prev_b != 0:
                        board[rowss][prev_b] = " "
                    prev_b = bulet
                    bulet += 1

                if bulet == 51 and board[rowss][bulet - 1] == "-":
                    board[rowss][bulet - 1] = " "
                board = clear_enemys(board, range(44, 51), enemy_pos)
                print("".join(board[rowss]))
                last_elemnt = len(board[rowss])

            print("-" * 51)
            time.sleep(bullet_speed)

    else:
        print("-" * 51)
        for rows in range(len_board):
            board = clear_enemys(board, range(44, 51), enemy_pos)
            print("".join(board[rows]))
        print("-" * 51)

    if board[player_ps][50] == "O":
        print("You win!")
        break

    key_p = ""
    shoot = False
    timer = time.time()
    while time.time() - timer < 1:
        key = keyboard.is_pressed()
        if key == "up":
            key_p = "up"
        if key == "down":
            key_p = "down"
        if key == "space":
            shoot = True
        if key == "q":
            print("Bye!")
            exit()

    prev_player_pos = player_ps
    prev_i = i

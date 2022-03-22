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


def create_board(x, y, max_enemys, enemy_range, min_enemys):
    board = [[" " for i in range(x)] for j in range(+y)]
    enemy_pos = []

    for enemy_y in range(random.randrange(min_enemys, max_enemys)):
        if enemy_y >= y:
            enemy_pos.append([random.randrange(enemy_range, x), random.randrange(0, y)])
            continue
        else:
            enemy_x = random.randrange(enemy_range, x)
        enemy_pos.append([enemy_x, enemy_y])
    board = clear_enemys(board, range(enemy_range - 1, x), enemy_pos)
    return [board, enemy_pos]


def locate_min(list):
    smallest = min(list)
    return [index for index, element in enumerate(list) if smallest == element]


def best_place(enemy_pos, height):
    ys = [0 for i in range(height)]
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


def spawan_enemys(
    board,
    enemy_pos,
    width,
    height,
    min_enemys,
    max_enemys,
    enemy_range,
    max_enemys_per_spawn,
):
    for i in range(random.randrange(0, max_enemys_per_spawn)):
        x = random.randrange(enemy_range, width)
        y = best_place(enemy_pos, height)
        # could probaly do this by checking if coord is in enemy_pos
        if board[y][x] == "<":
            if y == 4:
                y = 0
            else:
                y += 1
        enemy_pos.append([x, y])

    if len(enemy_pos) < height:
        for i in range(height - len(enemy_pos)):
            enemy_pos.append(
                [random.randrange(enemy_range, width), best_place(enemy_pos, height)]
            )
    if len(enemy_pos) > max_enemys:
        while len(enemy_pos) != min_enemys:
            enemy_pos.pop(len(enemy_pos) - 1)
    board = clear_enemys(board, range(enemy_range, width), enemy_pos)
    return [board, enemy_pos]


def configure_game():
    height = int(input("How high do you want the board to be? "))
    width = int(input("How wide do you want the board to be? "))
    max_enemys = int(input("How many enemys at most do you want on the board? "))
    min_enemys = int(input("How many enemys at least do you want on the board? "))
    enemy_range = int(input("Length of the enemy range? "))
    max_enemys_per_spawn = int(
        input("How many enemys at most do you want to spawn at once? ")
    )
    lives = int(input("How many lives do you want to start with? "))
    enemy_range = width - enemy_range
    return [
        height,
        width,
        max_enemys,
        min_enemys,
        enemy_range,
        max_enemys_per_spawn,
        lives,
    ]


def main():
    height = 5
    width = 51
    max_enemys = 10
    min_enemys = 5
    enemy_range = width - 6
    max_enemys_per_spawn = 3
    lives = 1
    clear(0)
    print(readme())
    print("press enter to start, q to quit, or c to configure the game")
    while True:
        key = keyboard.is_pressed()
        if key == "enter":
            break
        elif key == "q":
            exit()
        elif key == "c":
            clear(0)
            (
                height,
                width,
                max_enemys,
                min_enemys,
                enemy_range,
                max_enemys_per_spawn,
                lives,
            ) = configure_game()
            break
    key_p = ""
    player_ps = random.randrange(height)
    shoot = False
    prev_player_pos = None
    board, enemy_pos = create_board(width, height, max_enemys, enemy_range, min_enemys)
    len_board = len(board)
    # if the '-' collides with '<' then '<' is destroyed
    # if 'O' reaches the end of the board than you win the game
    #  for each row in the dictionary 'board' append the '<' to the end of the row
    for i in range(width):
        clear(0.1)
        if key_p == "up" and prev_player_pos != 0:
            player_ps -= 1

        elif key_p == "down" and prev_player_pos != 4:
            player_ps += 1

        else:
            player_ps = random.randrange(height)

        if board[player_ps][i] == "<":
            if lives == 0:
                board[prev_player_pos][prev_i] = ""
                board[player_ps][i] = "⦓"
                print("-" * width)
                for row in range(len_board):
                    print("".join(board[row]))
                print("-" * width)
                print("You lose!")
                break
            else:
                lives -= 1
                board[prev_player_pos][prev_i] = " "
                board[player_ps][i] = "O"
                print("-" * width)
                for row in range(len_board):
                    print("".join(board[row]))
                print("-" * width)
                clear(0.1)

        if prev_player_pos != None:
            board[prev_player_pos][prev_i] = " "

        board[player_ps][i] = "O"
        if shoot:
            print("".join(board[rows]))
            print("-" * width)
            prev_b = 0
            bulet = i + 1
            while bulet < width:
                os.system(clears)
                print("-" * width)
                for rowss in range(len_board):
                    if board[player_ps] == board[rowss]:
                        # check if the current bulet position is the as "<"
                        if board[rowss][bulet] == "<":
                            enemy_pos.remove([bulet, rowss])
                            board, enemy_pos = spawan_enemys(
                                board,
                                enemy_pos,
                                width,
                                height,
                                min_enemys,
                                max_enemys,
                                enemy_range,
                                max_enemys_per_spawn,
                            )
                        board[rowss][bulet] = "-"
                        if prev_b != 0:
                            board[rowss][prev_b] = " "
                        prev_b = bulet
                        bulet += 1

                    if bulet == width and board[rowss][bulet - 1] == "-":
                        board[rowss][bulet - 1] = " "
                    board = clear_enemys(board, range(enemy_range, width), enemy_pos)
                    print("".join(board[rowss]))
                    last_elemnt = len(board[rowss])

                print("-" * width)
                time.sleep(bullet_speed)

        else:
            board[player_ps][i] = "O"
            print("-" * width)
            for rows in range(len_board):
                board = clear_enemys(board, range(enemy_range, width), enemy_pos)
                print("".join(board[rows]))
            print("-" * width)

        if board[player_ps][width - 1] == "O":
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


if __name__ == "__main__":
    main()

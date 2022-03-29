import os
import random
import time
import sys
import csv
import keyboard

clears = "clear" if os.name == "posix" else "cls"
bullet_speed = 0.01 if os.name == "posix" else 0.000000000000000001
sep = "/" if os.name == "posix" else "\\"

path = os.path.dirname(os.path.abspath(__file__)).split(sep)

# make a variable for the length and height of the board so we can change it for different levels
# move most of the from here to somewhere else in src/ to make more modular
# make a function to display the board instead of doing it in three lines each time
# change it from a dictionary of lists to list list of lists


def readme():
    """
    this function prints the readme
    """
    with open("README.txt", "r") as f:
        return f.read().format("⦓")


def clear(times):
    """
    this function clears the screen
    it takes the amount of times to wait before clearing the screen
    it then clears the screen
    """
    time.sleep(times)
    os.system(clears)


def create_board(width, height, max_enemys, enemy_range, min_enemys):
    """
    This function will create the board.
    It will take the width and height of the board, the range of the enemy, the max number of enemies and the min number of enemies.
    It will then create the board and return the board.
    """

    # we make a list of lists with the length of the width and the height of the board
    board = [[" " for i in range(width)] for j in range(height)]
    enemy_pos = []

    # we then spawn the enemies on the board
    for enemy_y in range(random.randrange(min_enemys, max_enemys)):

        # if the current enemy y axis is greater than the height of the board we just spawn it at the randomly generated y axis
        if enemy_y >= height:
            enemy_pos.append(
                [random.randrange(enemy_range, width), random.randrange(0, height)]
            )
            continue

        else:
            enemy_x = random.randrange(enemy_range, width)

        # then we aare the enemy to enemy position list
        enemy_pos.append([enemy_x, enemy_y])

    # finally we spawn the enemies on the board
    board = clear_enemys(board, range(enemy_range - 1, width), enemy_pos)
    return [board, enemy_pos]


def locate_min(list):
    """
    This function will find the minimum value(s) in a list
    it takes a list and returns the minimum value(s) in the list
    """

    # we find the minimum value in the list
    smallest = min(list)

    # we make a list of the indexes that have the minimum value
    return [index for index, element in enumerate(list) if smallest == element]


def best_place(enemy_pos, height):
    """
    This function will find the best place to spawn an enemy on the y-axis.
    It will take the position of the enemies and the height of the board.
    It will then return the best place to spawn an enemy.
    """

    # we make a list of 0s one 0 for each row
    ys = [0 for i in range(height)]

    # we then add 1 to the list for each enemy on the board at the corresponing row
    for enemy in enemy_pos:
        ys[enemy[1]] += 1

    return random.choice(locate_min(ys))


def clear_enemys(board, enemy_range, enemy_pos):
    """
    this function takes the board, the range of the enemy and the position of the enemy
    clears the board of enemys that weren't removed from the board
    it then returns the board
    """

    # this removes all the enemys from the board
    for row in board:
        for enemy in enemy_range:
            # if we find a '<' (enemy) on the board we remove it
            if row[enemy] == "<":
                row[enemy] = " "

    # this adds all the enemys back to the board from the enemy_pos list
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
    """
    This function will spawn enemies on the board
    it takes the board, the position of the enemies, the width and height of the board, the min and max number of enemies, the range of the enemy, the max number of enemies per spawn and the lives
    it will then spawn the enemies on the board
    it will then return the board with the enemies on it and the position of the enemies
    """
    for i in range(random.randrange(0, max_enemys_per_spawn)):
        x = random.randrange(enemy_range, width)
        y = best_place(enemy_pos, height)

        # could probaly do this by checking if coord is in enemy_pos
        # if theres already an enemy there then we shift is down by one
        # and if by shifting we would go out of bounds then we just spawn it at the top
        if board[y][x] == "<":
            if y == height - 1:
                y = 0
            else:
                y += 1
        enemy_pos.append([x, y])

    # we try to keep the a enemy on each row
    if len(enemy_pos) < height:
        for i in range(height - len(enemy_pos)):
            enemy_pos.append(
                [random.randrange(enemy_range, width), best_place(enemy_pos, height)]
            )

    # if the amount of enemies is greater than the max then we remove enemies until we are at the min
    if len(enemy_pos) > max_enemys:
        while len(enemy_pos) != min_enemys:
            enemy_pos.pop(len(enemy_pos) - 1)

    # if the amount of enemies is less than the min then we add enemies until we are at the min
    elif len(enemy_pos) < min_enemys:
        while len(enemy_pos) != min_enemys:
            enemy_pos.append(
                [random.randrange(enemy_range, width), best_place(enemy_pos, height)]
            )

    # we then clear the board of any old non existing enemies
    board = clear_enemys(board, range(enemy_range, width), enemy_pos)
    return [board, enemy_pos]


def configure_game():
    """
    This function will configure the game.
    It will ask the user for the width and height of the board and the range of the enemies.
    It will also ask the user for the min and max number of enemies and the max number of enemies per spawn.
    It will then return the width, height, min_enemys, max_enemys, enemy_range, max_enemys_per_spawn
    """
    height = int(input("How high do you want the board to be? "))
    width = int(input("How wide do you want the board to be? "))
    max_enemys = int(input("How many enemys at most do you want on the board? "))
    min_enemys = int(input("How many enemys at least do you want on the board? "))

    # if min_enemys is greater than or equal to max_enemys then we set reask the min
    while min_enemys >= max_enemys:
        print("The min number of enemys must be less than the max number of enemys")
        min_enemys = int(input("How many enemys at least do you want on the board? "))

    enemy_range = int(input("Length of the enemy range? "))
    max_enemys_per_spawn = int(
        input("How many enemys at most do you want to spawn at once? ")
    )
    lives = int(input("How many lives do you want to start with? "))
    # enemy range is the length of the enemy minus range of the enemy
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


def level_list():
    """
    This function will return a list of all the levels
    from the level file
    """
    level_list = []
    with open(f"{sep.join(path)}{sep}levels{sep}levels.csv", "r") as level_file:
        filereader = csv.DictReader(level_file)
        for row in filereader:
            level_list.append(str(row["name"]))
    return level_list


def name_exists(name):
    """
    This function will check if the name exists in the list of names.
    It will take the name and check if the name is in the list of level names.
    It will then return true if the name is in the list of level names and false if it is not.
    """
    if name in level_list():
        return True
    return False


def configure_level():
    """
    This function will configure the game.
    It will ask the user for the width and height of the board and the range of the enemies.
    It will also ask the user for the min and max number of enemies and the max number of enemies per spawn.
    It will then write to the level file the name, width, height, min_enemys, max_enemys, enemy_range, max_enemys_per_spawn
    """
    level_name = input("What do you want the level name to be? ")
    while name_exists(level_name):
        print("That level name already exists")
        level_name = input("What do you want the level name to be? ")
    while level_name in ["h", "b", "q"]:
        print("That level name already is used in a menu")
        level_name = input("What do you want the level name to be? ")
    height = int(input("How high do you want the board to be? "))
    width = int(input("How wide do you want the board to be? "))
    max_enemys = int(input("How many enemys at most do you want on the board? "))
    min_enemys = int(input("How many enemys at least do you want on the board? "))

    # if min_enemys is greater than or equal to max_enemys then we set reask the min
    while min_enemys >= max_enemys:
        print("The min number of enemys must be less than the max number of enemys")
        min_enemys = int(input("How many enemys at least do you want on the board? "))

    enemy_range = int(input("Length of the enemy range? "))
    max_enemys_per_spawn = int(
        input("How many enemys at most do you want to spawn at once? ")
    )
    lives = int(input("How many lives do you want to start with? "))
    # enemy range is the length of the enemy minus range of the enemy
    enemy_range = width - enemy_range
    with open(f"{sep.join(path)}{sep}levels{sep}levels.csv", "a") as level_file:
        filewriter = csv.writer(level_file)
        filewriter.writerow(
            [
                level_name,
                height,
                width,
                min_enemys,
                max_enemys,
                enemy_range,
                max_enemys_per_spawn,
                lives,
            ]
        )


def read_level(level_name):
    """
    This function will read specific level from the level file
    and return the level's height, width, max_enemys, min_enemys, enemy_range, max_enemys_per_spawn, lives
    """
    level = []
    with open(f"{sep.join(path)}{sep}levels{sep}levels.csv", "r") as file:
        filereader = csv.DictReader(file)
        for row in filereader:
            if row["name"] == level_name:
                level = [
                    int(row["height"]),
                    int(row["width"]),
                    int(row["max_enemys"]),
                    int(row["min_enemys"]),
                    int(row["width"]) - int(row["enemy_range"]),
                    int(row["max_enemys_per_spawn"]),
                    int(row["lives"]),
                ]

    return level


def print_board(board, enemy_range, enemy_pos, width, height):
    """
    this function prints the board
    it take the actual board and range of the enemy and the position of the enemy and the width and height of the board
    it then clears the board of enemys that weren't removed and then prints the board
    returns only the board with the removed enemys
    """
    board = clear_enemys(board, range(enemy_range, width), enemy_pos)
    print("-" * width)
    for row in range(height):
        print("".join(board[row]))
    print("-" * width)


def main():
    # declare most of the variables
    height = 5  # height of the board can be changed with configure_game()
    width = 51  # width of the board can be changed with configure_game()
    max_enemys = 10  # max amount of enemys on the board at a timecan be changed with configure_game()
    min_enemys = 5  # minumum amount of enemys on the board at a time can be changed with configure_game()
    enemy_range = (
        width - 6
    )  # range in which enemy can be start at the end of the x axis can be changed with configure_game()
    max_enemys_per_spawn = 3  # max amount of enemys that can spawn at once can be changed with configure_game()
    lives = 1  # amount of lives the player has can be changed with configure_game()
    key_p = ""  # key pressed
    shoot = False  # if the player is shooting
    prev_player_pos = None  # previous position of the player

    # game intro
    clear(0)
    print(readme())  # print the readme/instructions
    print(
        """+---------------------------------------------------------+
|Press enter to start, q to quit, c to configure the game,|
|    n to create a new level, or l to load a level.       |
+---------------------------------------------------------+"""
    )
    while True:
        key = keyboard.is_pressed()
        if key == "enter":
            break

        elif key == "q":
            exit()

        # configuring the game
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

        elif key == "n":
            while True:
                clear(0)
                configure_level()
                print(
                    """+---------------------------------------------------+
|Press enter to start, b to go back to the main menu|, 
|     n to create another level, or q to quit.      |
+---------------------------------------------------+"""
                )
                continues = input("")
                if continues == "q":
                    exit()
                elif continues == "b":
                    break
                elif continues == "n":
                    continue

        elif key == "l":
            while True:
                clear(0)
                print(
                    """+--------------------------------------------------+
|    Enter a level name to start the level or      |
|          h to see the list of levels.         |
|Press b to go back to the main menu, or q to quit.|
+--------------------------------------------------+"""
                )
                level_name = input("")
                if level_name == "h":
                    for level in level_list():
                        print(f"{level}")
                    print("press enter to continue")
                    while True:
                        key = keyboard.is_pressed()
                        if keyboard.is_pressed() == "enter":
                            break
                elif level_name == "b":
                    break
                elif level_name == "q":
                    exit()
                elif level_name in level_list():
                    (
                        height,
                        width,
                        max_enemys,
                        min_enemys,
                        enemy_range,
                        max_enemys_per_spawn,
                        lives,
                    ) = read_level(level_name)
                    break
                else:
                    print("That level doesn't exist")
                    continue

    # create the board
    board, enemy_pos = create_board(width, height, max_enemys, enemy_range, min_enemys)

    # game loop
    for i in range(width):
        clear(0.1)
        # first if else is where on the y-axis (height) the player should be
        if key_p == "up" and prev_player_pos != 0:
            player_ps -= 1

        elif key_p == "down" and prev_player_pos != 4:
            player_ps += 1

        else:
            player_ps = random.randrange(height)

        # check if the player hits an enemy
        if board[player_ps][i] == "<":
            # if the player hits an enemy and has no lives left, game over
            # we show the final board and then exit the game
            if lives == 0:
                board[prev_player_pos][prev_i] = ""
                board[player_ps][i] = "⦓"
                print_board(board, enemy_range, enemy_pos, width, height)
                print("You lose!")
                break

            # if the player hits an enemy and has lives left, we remove the enemy and remove a life
            else:
                lives -= 1
                board[prev_player_pos][prev_i] = " "
                board[player_ps][i] = "O"
                print_board(board, enemy_range, enemy_pos, width, height)
                clear(0.1)

        # if the player has already moved, we remove the 'O' from the previous position to prevent an 'O' trail
        if prev_player_pos != None:
            board[prev_player_pos][prev_i] = " "

        board[player_ps][i] = "O"

        # if the player wants to shoot
        if shoot:
            # setting shooting variables
            prev_b = (
                0  # previous bullet position needed so we don't have a bullet trail
            )
            bulet = (
                i + 1
            )  # bullet position on the x-axis (width) its were the player is and one more so the bullet doesn't overlap the player

            # if the player is shooting and the bullet is on the board this could probably done with a for loop like for i in range(i+1, width)
            while bulet < width:
                os.system(clears)
                print("-" * width)
                for rowss in range(height):
                    # check if were on the same posotion on the y-axis as the player
                    if board[player_ps] == board[rowss]:
                        # check if the current bulet position is the as "<" meaning a bulet has hit an enemy
                        if board[rowss][bulet] == "<":
                            # if the bulet hits an enemy we remove the enemy
                            enemy_pos.remove([bulet, rowss])
                            # and also spawn new enemys
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

                        # if the bullet moves we want to clear the previos bullet position of '-' to prevent a bullet trail
                        if prev_b != 0:
                            board[rowss][prev_b] = " "

                        prev_b = bulet
                        bulet += 1

                    # to prevent bulet trail at end idk if its needed but no gonna remove just in case
                    if bulet == width and board[rowss][bulet - 1] == "-":
                        board[rowss][bulet - 1] = " "

                    board = clear_enemys(board, range(enemy_range, width), enemy_pos)
                    print("".join(board[rowss]))

                print("-" * width)
                time.sleep(bullet_speed)

        # if the player doesn't want to shoot we just move the player
        else:
            board[player_ps][i] = "O"
            print_board(board, enemy_range, enemy_pos, width, height)

        # if the player reaches the end of the x-axis he wins
        if board[player_ps][width - 1] == "O":
            print("You win!")
            break

        key_p = ""
        shoot = False

        timer = (
            time.time()
        )  # timer for the for the while loop below so that the you can only get keyboard input for 1 second
        # keyboard input for shooting and moving the player, and also for quitting the game
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

        # setting the previous position of the player to the current position cause its the end of the current iteration
        prev_player_pos = player_ps
        prev_i = i


if __name__ == "__main__":
    main()

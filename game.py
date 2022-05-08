import random
import os


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


def create_board(width, height, max_enemys, min_enemys, enemy_range):
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


def spawan_enemys(
    board,
    enemy_pos,
    width,
    height,
    max_enemys,
    min_enemys,
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
            try:
                enemy_pos.pop(len(enemy_pos) - 1)
            except IndexError:
                print(enemy_pos)
                print(len(enemy_pos))
                print(min_enemys)
                exit(1)

    # if the amount of enemies is less than the min then we add enemies until we are at the min
    elif len(enemy_pos) < min_enemys:
        while len(enemy_pos) != min_enemys:
            enemy_pos.append(
                [random.randrange(enemy_range, width), best_place(enemy_pos, height)]
            )

    # we then clear the board of any old non existing enemies
    board = clear_enemys(board, range(enemy_range, width), enemy_pos)
    return [board, enemy_pos]


if __name__ == "__main__":
    print("This is a game helper file.")
    print("Please run main.py instead.")
    continue_ = input("Do you want to run main.py? (y/n) ")
    if continue_ == "y":
        if os.name == "posix":
            try:
                os.system("python3 main.py")
            except:
                print("Could not run main.py.")
                print("Please run main.py manually.")

        elif os.name == "nt":
            try:
                os.system("python main.py")
            except:
                print("Could not run main.py.")
                print("Please run main.py manually.")

    exit()

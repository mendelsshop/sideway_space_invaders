# TODO: clean, comment and release

import os
import random
import time
import csv
import keyboard
import game
import menu


bullet_speed = 0.01 if os.name == "posix" else 0.000000000000000001
clears = "clear" if os.name == "posix" else "cls"


def main():
    # declare most of the variables
    height = 5  # height of the board can be changed with configure_game()
    width = 51  # width of the board can be changed with configure_game()
    max_enemys = 10  # max amount of enemys on the board at a timecan be changed with configure_game()
    min_enemys = 5  # minumum amount of enemys on the board at a time can be changed with configure_game()
    enemy_range = width - 6
    # range in which enemy can be start at the end of the x axis can be changed with configure_game()
    max_enemys_per_spawn = 3  # max amount of enemys that can spawn at once can be changed with configure_game()
    lives = 1  # amount of lives the player has can be changed with configure_game()
    key_p = ""  # key pressed
    shoot = False  # if the player is shooting
    prev_player_pos = None  # previous position of the player
    (
        height,
        width,
        max_enemys,
        min_enemys,
        enemy_range,
        max_enemys_per_spawn,
        lives,
    ) = menu.main_menu()
    # create the board
    board, enemy_pos = game.create_board(
        width, height, max_enemys, min_enemys, enemy_range
    )
    print(board)
    print(enemy_pos)
    time.sleep(10)
    # game loop
    for i in range(width):
        menu.clear(0.1)
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
                game.print_board(board, enemy_range, enemy_pos, width, height)
                print("You lose!")
                break

            # if the player hits an enemy and has lives left, we remove the enemy and remove a life
            else:
                lives -= 1
                board[prev_player_pos][prev_i] = " "
                board[player_ps][i] = "O"
                game.print_board(board, enemy_range, enemy_pos, width, height)
                menu.clear(0.1)

        # if the player has already moved, we remove the 'O' from the previous position to prevent an 'O' trail
        if prev_player_pos != None:
            board[prev_player_pos][prev_i] = " "

        board[player_ps][i] = "O"

        # if the player wants to shoot
        if shoot:
            # setting shooting variables
            prev_b = 0
            # previous bullet position needed so we don't have a bullet trail
            bulet = i + 1
            # bullet position on the x-axis (width) its were the player is and one more so the bullet doesn't overlap the player

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
                            board, enemy_pos = game.spawan_enemys(
                                board,
                                enemy_pos,
                                width,
                                height,
                                max_enemys,
                                min_enemys,
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

                    board = game.clear_enemys(
                        board, range(enemy_range, width), enemy_pos
                    )
                    print("".join(board[rowss]))

                print("-" * width)
                time.sleep(bullet_speed)

        # if the player doesn't want to shoot we just move the player
        else:
            board[player_ps][i] = "O"
            game.print_board(board, enemy_range, enemy_pos, width, height)

        # if the player reaches the end of the x-axis he wins
        if board[player_ps][width - 1] == "O":
            print("You win!")
            break

        key_p = ""
        shoot = False
        timer = time.time()
        # timer for the for the while loop below so that the you can only get keyboard input for 1 second
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

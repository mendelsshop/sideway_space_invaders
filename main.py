import os
import random
import time
import keyboard
import markdown
import html2text

# open readme.md and convert to html
def readme():
    with open("readme.md", "r") as f:
        text = f.read()
    return html2text.html2text(markdown.markdown(text))


print(readme(), end="")
print("press enter to start")
while True:
    if keyboard.is_pressed("enter"):
        break
key_p = ""
player_ps = random.randrange(5)
shoot = False
prev_player_pos = None
enemys = 5
# if the '-' collides with '<' then '<' is destroyed
# if 'O' reaches the end of the board than you win the game
def spawan_enemys(dict):
    for i in range(random.randrange(1, 2)):
        x = random.randrange(44, 51)
        y = random.randrange(4)
        if dict["row" + str(y + 1)][x] == "<":
            if y == 4:
                y = 0
            else:
                y += 1
        dict["row" + str(y + 1)][x] = "<"
    return dict


board = {
    "row1": [" "] * 50,
    "row2": [" "] * 50,
    "row3": [" "] * 50,
    "row4": [" "] * 50,
    "row5": [" "] * 50,
}
#  for each row in the dictionary 'board' append the '<' to the end of the row
for row in board:
    board[row].append("<")

for i in range(51):
    time.sleep(0.01)
    os.system("cls")
    if key_p == "up" and prev_player_pos != 0:
        player_ps -= 1

    elif key_p == "down" and prev_player_pos != 4:
        player_ps += 1

    else:
        player_ps = random.randrange(5)
    if board["row" + str(player_ps + 1)][i] == "<":
        print("-" * 51)
        for row in board:
            print("".join(board[row]))
        print("-" * 51)
        print("You lose!")
        break

    if prev_player_pos != None:
        board["row" + str(prev_player_pos + 1)][prev_i] = " "

    board["row" + str(player_ps + 1)][i] = "O"
    if shoot:
        print("".join(board[rows]))
        print("-" * 51)
        prev_b = 0
        bulet = i + 1
        while bulet < 51:
            os.system("cls")
            print("-" * 51)
            for rowss in board:
                if board["row" + str(player_ps + 1)] == board[rowss]:
                    # check if the current bulet position is the as "<"
                    if board[rowss][bulet] == "<":
                        enemys -= 1

                    board[rowss][bulet] = "-"

                    if prev_b != 0:
                        board[rowss][prev_b] = " "

                    prev_b = bulet
                    bulet += 1
                if enemys != 5:
                    board = spawan_enemys(board)
                    enemys = 5
                if bulet == 51 and board[rowss][bulet - 1] == "-":
                    board[rowss][bulet - 1] = " "

                print("".join(board[rowss]))

                last_elemnt = len(board[rowss])

            print("-" * 51)
            time.sleep(0.00000000000000000001)

    else:
        print("-" * 51)
        for rows in board:
            print("".join(board[rows]))
        print("-" * 51)
    if board["row" + str(player_ps + 1)][50] == "O":
        print("You win!")
        break

    key_p = ""
    shoot = False
    timer = time.time()
    while time.time() - timer < 0.5:
        # if the 2 seconds have passed, quit the loop
        if keyboard.is_pressed("up"):
            key_p = "up"

        elif keyboard.is_pressed("down"):
            key_p = "down"

        if keyboard.is_pressed("space"):
            shoot = True

    prev_player_pos = player_ps
    prev_i = i

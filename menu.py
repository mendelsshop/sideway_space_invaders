import csv
import keyboard
import os
import time

sep = "/" if os.name == "posix" else "\\"
path = os.path.dirname(os.path.abspath(__file__)).split(sep)
clears = "clear" if os.name == "posix" else "cls"


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


def configure_game():
    """
    This function will configure the game.
    It will ask the user for the width and height of the board and the range of the enemies.
    It will also ask the user for the min and max number of enemies and the max number of enemies per spawn.
    It will then return the width, height, min_enemys, max_enemys, enemy_range, max_enemys_per_spawn
    This function will optionally write to the level file the level
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
    while enemy_range > width:
        print("The enemy range must be less than the width of the board: ", width)
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
    # first we get level name
    level_name = input("What do you want the level name to be? ")
    # then we check if the name already exists or is not used in a menu or blank
    while (
        name_exists(level_name)
        or level_name == ""
        or level_name in ["h", "b", "q", "p"]
    ):
        print(
            "That level name already is used in a menu, is blank, or is a name that is"
            " already used."
        )
        level_name = input("What do you want the level name to be? ")

    # then we get the level info such as height, width, max_enemys, min_enemys,
    height = int(input("How high do you want the board to be? "))
    width = int(input("How wide do you want the board to be? "))
    max_enemys = int(input("How many enemys at most do you want on the board? "))
    min_enemys = int(input("How many enemys at least do you want on the board? "))

    # if min_enemys is greater than or equal to max_enemys then we set reask the min
    while min_enemys >= max_enemys:
        print("The min number of enemys must be less than the max number of enemys")
        min_enemys = int(input("How many enemys at least do you want on the board? "))

    # we continue by getting the enemy range
    enemy_range = int(input("Length of the enemy range? "))
    # then we check if the enemy range is greater than the width
    # because if so we would get a negative value for the enemy range
    while enemy_range > width:
        print("The enemy range must be less than the width of the board: ", width)
        enemy_range = int(input("Length of the enemy range? "))

    # then we get the max number of enemies per spawn, and lives
    max_enemys_per_spawn = int(
        input("How many enemys at most do you want to spawn at once? ")
    )
    lives = int(input("How many lives do you want to start with? "))
    # then we write to the level file the level
    with open(f"{sep.join(path)}{sep}levels{sep}levels.csv", "a") as level_file:
        filewriter = csv.writer(level_file)
        filewriter.writerow([
            level_name,
            height,
            width,
            max_enemys,
            min_enemys,
            enemy_range,
            max_enemys_per_spawn,
            lives,
        ])
    # and return the level name so it can be used for the p option
    return level_name


def read_level(level_name):
    """
    This function will read specific level from the level file
    and return the level's height, width, max_enemys, min_enemys, enemy_range, max_enemys_per_spawn, lives
    """
    level = []  # create a list in which to read the level info into
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

    print(level)
    return level


def main_menu():
    clear(0)
    print(readme())  # print the readme/instructions
    print("""+----------------------------------------------------------+
|Press enter to start, q to quit, c to configure the game, |
|    n to create a new level, or l to load a level.        |
+----------------------------------------------------------+""")
    while True:

        key = keyboard.is_pressed()
        if key == "enter":
            return read_level("Default")

        elif key == "q":
            exit()

        # configuring the game
        elif key == "c":
            clear(0)
            return configure_game()

        elif key == "n":
            while True:
                clear(0)
                new_level = configure_level()
                print("""+----------------------------------------------------+
|   Press enter to start, b to go back to the main   | 
|     n to create another level, p to play the new   |
|              level, or q to quit.                  |
+----------------------------------------------------+""")
                continues = input("> ")
                if continues == "q":
                    exit()

                elif continues == "b":
                    break

                elif continues == "n":
                    continue

                elif continues == "p":
                    return read_level(new_level)

        elif key == "l":
            while True:
                clear(0)
                print("""+---------------------------------------------------+
|    Enter a level name to start the level or       |
|          h to see the list of levels.             |
|    Press b to go back to the main  or q to quit.  |
+---------------------------------------------------+""")
                level_name = input("> ")
                if level_name == "h":
                    for level in level_list():
                        print(f"{level}")

                    print("press enter to continue.")

                    while True:
                        key = keyboard.is_pressed()
                        if keyboard.is_pressed() == "enter":
                            break

                elif level_name == "b":
                    break

                elif level_name == "q":
                    print("quitting...")
                    print("Have a nice day!")
                    exit()

                elif level_name in level_list():
                    print(
                        f"Starting level {level_name},"
                        f" {len(read_level(level_name))} levels left."
                    )
                    return read_level(level_name)

                else:
                    print(f"Level: {level_name} doesn't exist.")
                    print("press enter to continue.")
                    while True:
                        key = keyboard.is_pressed()
                        if keyboard.is_pressed() == "enter":
                            break


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

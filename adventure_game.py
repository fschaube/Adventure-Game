import time
import random
items = []


def print_pause(string, t):
    """Create a time delay between the strings and print the strings"""
    print(string)
    time.sleep(t)


def intro(monster):
    """print the intro"""
    print_pause("#### THE MONSTERS OF PRAGUE ####\n", 2)
    print_pause(
        'Every year the' + " " +
        monster.upper() +
        " " +
        "returns to the city of Prague.",
        2)
    print_pause("The streets of Prague are empty. It is a dark night", 2)
    print_pause("Everyone is afraid of his return.", 2)
    print_pause("As a tourist you arrived today in the center of the city.", 2)
    print_pause("Can't you find the monster and break the curse?", 2)


def appearing(monster):
    """let the monster appear"""
    print_pause("You walk on.", 2)
    print_pause("The" + " " + monster + " " + "appears!!!", 2)


def repeat_game():
    """repeat the game"""
    while True:
        playagain = input("Play again (yes/no)?\n")
        if playagain == "yes":
            items.clear()
            play_game()
        elif playagain == "no":
            break
        else:
            repeat_game()


def choice1(choice, monster):
    """handle the first choice"""
    if choice == "1":
        if "flashlight" not in items:
            print_pause("The Charles Bridge is really foggy", 2)
            print_pause("You can see absolute nothing", 2)
            print_pause("You walk on and find a flashlight", 2)
            light_choice(monster)
        else:
            print_pause(
                "You allready pasted this way\nPlease choose another way!", 2)
            logic(monster)


def choice2(choice, monster):
    """handle the second choice"""
    if choice == "2":
        if "mirrors" not in items:
            print_pause("The St. Vitus Cathedral is totally empty and dark", 2)
            print_pause(
                "You only hear the sound of" +
                "the wind that runs through the hall", 2)
            mirror_choice(monster)
        else:
            print_pause(
                "You allready pasted this way\nPlease choose another way!", 2)
            logic(monster)


def choice3(choice, monster):
    """handle the third choice"""
    if choice == "3":
        print_pause("You enter the castle.", 2)
        print_pause("You hear a terrible sound in the great hall", 2)
        print_pause("It is the" +
                    " " +
                    monster +
                    " " +
                    "that faces you!",
                    2)
        if "flashlight" in items and "mirrors" in items:
            if monster == "zombie horse":
                print_pause("### SHOWDOWN ####", 2)
                print_pause("The zombie horse begin to run.", 2)
                print_pause("It attacks you.", 2)
                print_pause(
                    "You combine the 2 items to one weapon\n" +
                    "so that the mirror reflect the light everywhere.",
                    2)
                print_pause("The" + monster + "get burned by the light.", 2)
                print_pause("YOU WON THE GAME!", 2)
                repeat_game()
            else:
                appearing(monster)
                print_pause("You faint.", 2)
                repeat_game()
        else:
            if monster == "zombie horse":
                print_pause(
                    "You enter the dark Prague" +
                    "Castle and walk to the cold rooms", 2)
                print_pause("Suddenly the" + " " + monster +
                            " " + "appears and attacks you.", 2)
                print_pause(
                    "You give everything but the" +
                    " " +
                    monster +
                    " " +
                    "is to strong.\nYou faint.",
                    2)
                print_pause("Something was missing...", 2)
                logic(monster)
            else:
                print_pause("The" + " " + monster + " " + "attacks you!", 2)
                print_pause("You faint!", 2)
                repeat_game()


def light_choice(monster):
    """handle the excplicit decision in choice1"""
    lightchoice = input("Do you wanna take it up (yes/no)?\n").lower()
    if lightchoice == "yes":
        items.append("flashlight")
        appearing(monster)
        if monster == "ghost":
            print_pause(
                "You activate your flashlight and the" +
                monster +
                "disappears.",
                2)
            print_pause("YOU WON THE GAME", 2)
            repeat_game()

        elif monster == "zombie horse":
            print_pause(
                "You can't fight the" + " " + monster + " yet", 2)
            print_pause("You need one more item!", 2)
            logic(monster)
        else:
            print_pause(
                "The flashlight has no" + " " +
                "effect on the scary pumpkin!", 2)
            print_pause("You faint!", 2)
            repeat_game()
    elif lightchoice == "no":
        if monster == "ghost":
            print_pause("You return to the starting point.", 2)
            logic(monster)
        else:
            appearing(monster)
            print_pause("You faint.", 2)
            repeat_game()
    else:
        print_pause("Please type your answer again!", 2)
        light_choice(monster)


def mirror_choice(monster):
    """handle the explicit decision in choice 2"""
    print_pause("There are to little mirrors at the altar.", 2)
    mirrorchoice = input("Do you wanna pick them up(yes/no)?\n").lower()
    if mirrorchoice == "yes":
        items.append("mirrors")
        appearing(monster)
        if monster == "ghost":
            if "flashlight" in items:
                print_pause("You activate your flashlight!", 2)
                print_pause("You shine on the mirrors.", 2)
                print_pause(
                    "That reflection builds an wall" +
                    "of light so that the ghost disappears.", 2)
                print_pause("YOU WON THE GAME!", 2)
                repeat_game()
            else:
                if monster == "zombie horse":
                    print_pause(
                        "Something is missing to fight the" +
                        " " +
                        monster +
                        " ",
                        2)
                    logic(monster)
                else:
                    print_pause("You faint!", 2)
                    repeat_game()
        else:
            print_pause("You can't fight the" + " " + monster + "yet", 2)
            print_pause("You need one more item!", 2)
            logic(monster)

    elif mirrorchoice == "no":
        print_pause("There is also oil lamp.", 2)
        oil_choice(monster)

    else:
        print_pause("Please type your answer again!", 2)
        mirror_choice(monster)


def oil_choice(monster):
    """handle the choice after the mirror choice"""
    oilchoice = input(
        "Do you wanna pick up the oil lamp (yes/no)?\n").lower()
    if oilchoice == "yes":
        if monster == "scary pumpkin":
            appearing(monster)
            print_pause("You turn your oil lamp on!", 2)
            print_pause("The" + " " + monster + " " + "get's burned and dies", 2)
            print_pause("YOU WON THE GAME!", 2)
            repeat_game()
        else:
            appearing(monster)
            print_pause("You faint!", 2)
            repeat_game()
    elif oilchoice == "no":
        appearing(monster)
        print_pause("You faint", 2)
        repeat_game()
    else:
        print_pause("Please type your answer again!", 2)
        oil_choice(monster)


def logic(monster):
    """handle the whole logic of the game"""
    print_pause("Where do you want to go?\n", 2)
    choice = input(
        "Choose on of the following numbers:\n1." +
        "Charles Bridge\n" +
        "2. St. Vitus Cathedral\n3. Prague Castle\n").lower()
    if choice not in "1" and choice not in "2" and choice not in "3":
        print_pause("\nSorry I don't understand!", 0)
        print_pause("Please repeat the input!\n", 0)
        logic(monster)
    choice1(choice, monster)
    choice2(choice, monster)
    choice3(choice, monster)


def play_game():
    """combine the most important functions"""
    monster = random.choice(["ghost", "zombie horse", "scary pumpkin"])
    intro(monster)
    logic(monster)


play_game()

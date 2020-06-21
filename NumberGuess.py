###################   Number Guessing Game ######################

def register():
    playerName = list()
    playCount  = 0
    counter = int(input("How many players are there?(1-10): "))
    if counter < 2 :
        print("Error,There should be more than Two players!")
        register()
    elif counter > 10 :
        print("Error ,There should be less than Ten players!")
        register()
    while playCount != counter:
        playerName.append(input(str("Enter Player {}'s Name : ".format(playCount+1))))
        playCount += 1
    return counter, playerName

counter,players = register()
scores = [0,0,0,0,0,0,0,0,0,0]


def menu(scores):
    print("\t\nWelcome to the Number Guessing Game\n\n")
    print("1. Play the Game")
    print("2. Scoreboard")
    print("3. Print scores to a .txt file")
    print("0. Exit Game")
    choice = int(input("Enter Choice(0-3) :" ))
    if choice == 0 :
        exit()
    elif choice == 1 :
        #scores = game(scores)
        #score(scores)
        print("play game")
    elif choice == 2 :
        #score(scores)
        print("scores")
    elif choice == 3 :
        print("file")
        #export(scores)

menu(scores)
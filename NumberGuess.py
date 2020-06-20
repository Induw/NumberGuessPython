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

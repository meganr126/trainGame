### 12/9/15: Megan decides to write a text-based game
### I don't even know why.

from random import *

### prints initial game message
def beginGame():
    print("Oh wow! You're a train!")
    print
    
    print("Being a train is so much fun! You get to do all sorts of fun train things!\n"+
          "Right now, you have to deliver some junk to the junkyard.\n"+
          "The junkyard is through the tunnel, but the tracks are pretty complicated.\n"+
          "Can you find the tunnel?")
    print

    print("\t[You must find the tunnel.\n\t"+
          "You are free to enter 'quit'\n\tat any time if you wish to do so."+
          " But you won't, right?\n\tYou're better than that.]")

### prints random message after each turn
def printMessage():
    dialogue = ["More trees. Shocking.", "Oh, hey, is that another train? Hi, other train!", "You see a cloud that looks like a star.",
                "You're tired. Wait, can trains even get tired?", "I wonder if trains can think.",
                "You see a car driving by. How exciting!",
                "You see pigeons!!!",
                "You begin to hum the Thomas the Tank Engine theme song.",
                "Damn this junkyard is far away.",
                "You reach a fork in the tracks, but it's not exciting because you know where you're going.",
                "You take a moment to realize that you're pretending to be a train right now.",
                "Oooh, is that a thunderstorm in the distance? No, wait. It's not."]

    num = randrange(1, len(dialogue))
    print(dialogue[num])

### checks if there is an object in the room
def checkObj(leftCount, upCount):
    roomNum = ((int(upCount)-1)*5)+int(leftCount)

    if roomNum == 6:
        return "passenger"
    elif roomNum == 20:
        return "light"
    else: return False

### checks if player is in final room and, if so,
### if they have the key to unlock the door or not
def checkFinal(roomNum, inventory):
    if roomNum == 22:
        if "light" in inventory: return "good"
        else: return "need light"
    else: return "bad"

### gets all possible movements for a turn 
def getMovements(leftCount, upCount, facing, inventory):
    objGotten = checkObj(leftCount, upCount)
    choices = []

    ### doors for rooms 1-25 when facing right
    facingRight=[["left"], ["left", "straight"], ["left", "back"], ["left"], ["left"],
                ["right", "straight"], ["back", "right"], ["left", "right"], ["right", "straight"], ["left", "right", "back"],
                ["straight", "left"], ["back", "straight"], ["straight", "right", "back"], ["back", "left"], ["left", "right"],
                ["left", "right"], ["left", "straight"], ["left", "back"], ["straight", "right"], ["left", "back", "right"],
                ["right"], ["right"], ["right", "straight"], ["straight", "back"], ["back", "right"]]

    ### doors for rooms 1-25 when facing left
    facingLeft=[["right"], ["right", "back"], ["right", "straight"], ["right"], ["right"],
                ["left", "back"], ["straight", "left"], ["right", "left"], ["left", "back"], ["left", "right", "straight"],
                ["back", "right"], ["back", "straight"], ["straight", "left", "back"], ["straight", "right"], ["left", "right"],
                ["left", "right"], ["right", "back"], ["right", "up"], ["back", "left"], ["left", "straight", "right"],
                ["left"], ["left"], ["left", "back"], ["straight", "back"], ["straight", "left"]]

    ### doors for rooms 1-25 when facing up
    facingUp=[["straight"], ["right", "straight"], ["straight", "left"], ["straight"], ["straight"],
                ["right", "back"], ["left", "back"], ["straight", "back"], ["right", "back"], ["left", "straight", "back"],
                ["straight", "right"], ["left", "right"], ["left", "right", "back"], ["straight", "left"], ["straight", "back"],
                ["straight", "back"], ["straight", "right"], ["straight", "left"], ["back", "right"], ["left", "back", "straight"],
                ["back"], ["back"], ["back", "right"], ["right", "left"], ["back", "left"]]

    ### doors for rooms 1-25 when facing down
    facingDown=[["back"], ["left", "back"], ["back", "right"], ["back"], ["back"],
                ["left", "straight"], ["right", "straight"], ["straight", "back"], ["left", "straight"], ["right", "straight", "back"],
                ["back", "left"], ["left", "right"], ["left", "right", "straight"], ["back", "right"], ["left", "straight"],
                ["straight", "back"], ["back", "left"], ["back", "right"], ["straight", "left"], ["right", "back", "straight"],
                ["straight"], ["straight"], ["straight", "left"], ["right", "left"], ["straight", "right"]]

    ### if there is an object in the room, print appropriate message
    ### and append that object to the list of possible move choices
    if objGotten != False:
        if objGotten == "passenger" and "passenger" not in inventory:
            print("There's a passenger sitting on a bench by the track. You can let them in.")
            choices.append("passenger")
        elif objGotten == "light" and "light" not in inventory:
            print("There is a light sitting near the tracks. That looks like it could be useful.")
            choices.append("light")

    ### adjust choices based on room number and
    ### direction player is facing
    roomNum = ((int(upCount)-1)*5)+int(leftCount)
    if facing == "left":
        choices = choices + facingLeft[roomNum-1]
    elif facing == "up":
        choices = choices + facingUp[roomNum-1]
    elif facing == "right":
        choices = choices + facingRight[roomNum-1]
    elif facing == "down":
        choices = choices + facingDown[roomNum-1]

    ### check if in final room and, if so, if door can
    ### be unlocked 
    finalCheck = checkFinal(roomNum, inventory)
    if finalCheck == "good":
        print("You see a tunnel in the distance, and you turn on your light as you approach.\n"+
              "You're almost there!")
        choices.append("tunnel")
    elif finalCheck == "need key":
        print("You see a tunnel, but it is much too dark for you to feel safe entering."+
              "If only there were some kind of light somewhere that you could take.")

    ### print random turn message
    print
    printMessage()

    ### arranges list of possible moves by creating list
    msg, toAdd = "You can", []
    if "passenger" in choices:
        toAdd.append(" pick up the passenger")
    if "light" in choices:
        toAdd.append(" pick up the light")
    if "left" in choices:
        toAdd.append(" go left")
    if "right" in choices:
        toAdd.append(" go right")
    if "back" in choices:
        toAdd.append(" go back")
    if "straight" in choices:
        toAdd.append(" go straight")
    if "tunnel" in choices:
        toAdd.append(" enter the tunnel and venture forth")

    ### takes list of possible moves and arranges them
    ### with proper grammar because i care about that
    for x in range(0, len(toAdd)-1):
        msg = msg + toAdd[x] + ","
    if len(toAdd) > 1:
        if len(toAdd) == 2:
            msg = msg[0:-1]
        msg = msg + " or"
    msg = msg + toAdd[-1] + "."
    print(msg)
    print

    ### get command, do the thing
    inp = raw_input("What do you do? ")
    command, inventory = getCommand(inp, choices, inventory)

    ### adjust counts if facing up
    if facing == "up":
        if command == "left":
            leftCount = leftCount - 1
            facing = "left"
        elif command == "right":
            leftCount = leftCount + 1
            facing = "right"
        elif command == "straight":
            upCount = upCount + 1
            facing = "up"
        elif command == "back":
            upCount = upCount - 1
            facing = "down"

    ### adjust counts if facing down
    elif facing == "down":
        if command == "left":
            leftCount = leftCount + 1
            facing = "right"
        elif command == "right":
            leftCount = leftCount - 1
            facing = "left"
        elif command == "straight":
            upCount = upCount - 1
            facing = "down"
        elif command == "back":
            upCount = upCount + 1
            facing = "up"

    ### adjust counts if facing left
    elif facing == "left":
        if command == "left":
            upCount = upCount - 1
            facing = "down"
        elif command == "right":
            upCount = upCount + 1
            facing = "up"
        elif command == "straight":
            leftCount = leftCount - 1
            facing = "left"
        elif command == "back":
            leftCount = leftCount + 1
            facing = "right"

    ### adjust counts if facing right
    elif facing == "right":
        if command == "left":
            upCount = upCount + 1
            facing = "up"
        elif command == "right":
            upCount = upCount - 1
            facing = "down"
        elif command == "straight":
            leftCount = leftCount + 1
            facing = "right"
        elif command == "back":
            leftCount = leftCount - 1
            facing = "left"

    return command, leftCount, upCount, facing, inventory

### takes user input, splits on common punctuation and 
### spaces so that only words remain
def stringSplit(string):
    string = string.split(".")
    
    string = "".join(string)
    string = string.split(",")

    string = "".join(string)
    string = string.split("?")

    string = "".join(string)
    string = string.split("!")

    string = "".join(string)
    string = string.split(" ")

    return string

### takes user input and gets command
def getCommand(string, choices, inventory):
    command, turnSuccess = [], False

    while turnSuccess == False:
        ### splits the string and formats it
        string = string.lower()
        splitStr = stringSplit(string)

        ### if input includes one object or direction word,
        ### the turn is a success, and that is what the player
        ### will do
        for direction in choices:
            if direction in splitStr:
                if command == []:
                    command.append(direction)
                    if command in ([["left"], ["straight"], ["right"], ["back"]] or
                                   [["passenger"], ["light"], ["passenger"]] or
                                   [["tunnel"]]):
                        turnSuccess = True
                else:
                    ### if it includes more than one, it is invalid
                    command = []
                    turnSuccess = False

        ### if turn is a success, print the chosen course of action
        if len(command) == 1:
            if command in [["left"], ["straight"], ["right"], ["back"]]:
                print("\nYou go " + command[0] + ".")
                turnSuccess = True
            elif command in [["passenger"], ["light"], ["passenger"]]:
                print("\nYou pick up the " + command[0] + ".")
                inventory = inventory + command
                turnSuccess = True
            elif command in [["unlock"]]:
                turnSuccess = True

        ### if not a success, print easter egg or error
        else:
            ### there is no reason for all of these. but whatever.
            if "dance" in splitStr:
                print("\nYou're... dancing. Apparently the maze is really getting to you.")
            elif "eat" in splitStr:
                print("\nYou've got nothing to eat. Well, besides yourself.\n"+
                      "But that would be counterproductive.")
            elif "megan" in splitStr:
                print("\n:D")
            elif "fuck" in splitStr:
                print("\nA robotic arm descends from the ceiling and flicks you on the arm.\n"+
                      "No swearing.")
            elif "sing" in splitStr:
                print("\nOnly if your roommate is singing.\nWait, you're alone.\nNever mind. Go for it.")
            elif "run" in splitStr:
                print("\nMaking my way downtown.\n  Walking fast\n    Faces Pass\n" +
                      "      And I'm home bound.")

            ### tried to use wrong direction words
            elif ("forward" or "forwards") in splitStr:
                print("\n\t[Acceptable commands include the words\n\t'left,' 'straight,' 'right,'"+
                      " or 'back.']")
            elif ("backward" or "backwards") in splitStr:
                print("\n\t[Acceptable commands include the words\n\t'left,' 'straight,' 'right,'"+
                      " or 'back.']")

            ### gave up
            elif ("quit" in splitStr):
                command = ["quit"]
                turnSuccess = True

            ### generic error
            else:
                print("\nThat wasn't a good thing to do.")

            ### get new input if they haven't given up
            if command != ["quit"]:                           
                print("Why don't you try something else?\n")
                string = input("What do you do? ")


    return command[0], inventory

### run the game
def main():
    inventory = []
    beginGame()
    choice, leftCount, upCount, facing, inventory = getMovements(3, 1, "up", inventory)
    unlocked, directions = False, ["left", "straight", "right", "back"]

    ### while the game hasn't ended, continue running turns
    while (choice != "tunnel" and
           choice != "quit"):
        choice, leftCount, upCount, facing, inventory = getMovements(leftCount, upCount, facing, inventory)
        if choice in ["passenger", "light"]:
            inventory.append(choice)

    ### if player gives up, print give up message
    if choice == "quit":
        print("\nYou seem to have run out of fuel.")
        print
        print("Time to wait for another train to come by and rescue you.")
        print
        print("Oh well.")
        print
        print
        print("GAME OVER.")

    ### if player unlocks the door and escapes, print
    ### escape message
    if choice == "unlock":
        print("\n\nYou enter the tunnel and darkness surrounds you.")
        print
        print("As you exit, the junkyard becomes visible in the distance.")
        print
        print
        print("You made it!")
        print
        print
        print
        print("THE END")

main()

### fin.

import random



def main ():

    dices = [0,0,0,0,0]
    scoreOne = 0
    scoreTwo = 0
    turn = 0
    rolls = 0

    input("Press enter to start")
    
    while(True):
        

        if rolls == 0:
            if turn % 2:
                print("Player Two rolled for ", int(turn/2) + 1, "'s")
            else:
                print("Player One rolled for ", int(turn/2) + 1, "'s")
            rolls += 1
            dices = roll(dices)
        elif rolls < 3:
            rr = input("Which dices would you like to re-roll? (1 - 6, or enter pass): ")
            rerolls = rr.split(' ')
            if(rr == ""):
                if turn % 2:
                    scoreTwo += score(turn, dices)
                    print("Player Two's score: ", scoreTwo, "\n\n")
                else:
                    scoreOne += score(turn, dices)
                    print("Player One's score: ", scoreOne, "\n\n")
                rolls = 0
                turn += 1

            else:
                dices = reroll(rerolls, dices)
                rolls += 1

        else:
            if turn % 2:
                scoreTwo += score(turn, dices)
                print("Player Two's score: ", scoreTwo, "\n\n")
            else:
                scoreOne += score(turn, dices)
                print("Player One's score: ", scoreOne, "\n\n")
            rolls = 0
            turn += 1
            
        if turn >= 12:
            winner(scoreOne, ScoreTwo)
            print("Press Enter to quit the application")
            break;




def roll (dices):
    for i in range(0,5):
        dices[i] = random.randint(1, 6);
    print(dices)
    return dices

def reroll(indices, dices):
    for i in indices:
        dices[int(i) - 1] = random.randint(1, 6);
    print(dices)
    return dices

def winner(scoreOne, ScoreTwo):
    if scoreOne > scoreTwo:
        print("Player One won with the score ", scoreOne, " to ", scoreTwo, "!")
    elif scoreTwo > scoreOne:
        print("Player Two won with the score ", scoreTwo, " to ", scoreOne, "!")
    else:
        print("Both players tied with the score ", scoreOne, "!")

def score(turn, dices):
    newScore = 0
    if turn < 12:
        for i in range(0,5):
            if dices[i] == int(turn/2) + 1:
                newScore += 1
    return newScore

if __name__ == "__main__": main()

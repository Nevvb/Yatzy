import random


def main():
    
    scoreOne = 0
    scoreTwo = 0
    dices = [0,0,0,0,0]
    turn = 0
    rolls = 0

    while(True):

       

        if rolls == 0:
            if turn % 2:
                print("Player Two rolled for ", int(turn/2) + 1 , "'s")
            else:
                print("Player One rolled for ", int(turn/2) + 1 , "'s")
            dices = roll(dices)
            print(dices)
            rolls += 1
        elif rolls < 3:
            strRe = input("Which dice would you like to re-roll? (1 - 5 with spaces or Enter to pass) ")
            rerolls = strRe.split(' ')
            if strRe == "":
                if turn % 2:
                    scoreTwo += score(dices, turn)
                    print("Player Two's score: ", scoreTwo, "\n\n")
                else:
                    scoreOne += score(dices, turn)
                    print("Player One's score: ", scoreOne, "\n\n")
                rolls = 0
                turn += 1
            else:
                dices = reroll(dices, rerolls)
                print(dices)
                rolls += 1
                
        else: 
            if turn % 2:
                scoreTwo += score(dices, turn)
                print("Player Two's score: ", scoreTwo, "\n\n")
            else:
                scoreOne += score(dices, turn)
                print("Player One's score: ", scoreOne, "\n\n")

            rolls = 0
            turn += 1

        if(turn >= 12):
            winner(scoreOne, scoreTwo)
            input("Press Enter to quit")
            break



def roll(dices):
    for i in range(0,5):
        dices[i] = random.randint(1, 6);
    return dices

def reroll(dices, indices):
    for i in indices:
        dices[int(i) - 1] = random.randint(1,6)
    return dices

def score(dices, turn):
    newscore = 0
    for i in range(0,5):
        if dices[i] == int(turn/2) + 1:
            newscore += int(turn/2) + 1
    return newscore

def winner(scoreOne, scoreTwo):
    if scoreOne > scoreTwo:
        print("Player One won with the score ", scoreOne, " to ", scoreTwo, "!")
    elif scoreTwo > scoreOne:
        print("Player Two won with the score ", scoreTwo, " to ", scoreOne, "!")
    else:
        print("Players tied with the score ", scoreOne, " to ", scoreTwo, "!")

if __name__ == "__main__": main()
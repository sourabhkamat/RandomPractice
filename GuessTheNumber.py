Guess = 18

NOG = 7 # Number Of Guesses
NOG1 = NOG

while True:
    if NOG >= 1:
        print("\nYou Have", NOG, "Guesses.\n")
        
        Guessed = int(input("Enter Number : "))
        
        if Guessed > Guess:
            print("Number is greater")
        
        elif Guessed < Guess:
            print("Number is smaller")
        
        elif Guessed == Guess:
            print("Correct! You Won, it\'s", Guess)
            print("You Took", (NOG1+1) - NOG, "Guesses.")
            break
            
    else:
        print("Game Over, Number is", Guess)
        break
            
    NOG -= 1

n = 5
guess=0

print("Guesses are limited to 5 only")

while(guess<=5):
    user_choice = int(input("Guess the number\n"))

    if(user_choice<55):
        print("THE number you have guess is smaller than the input number")

    elif (user_choice > 55):
        print("THE number you have guess is larger than the input number")

    else:
        print("THE number you have guess is corret\n "
              "YOU WON")
        break

    print(5-guess,"no. of guess is left\n")
    guess = guess+1

if (guess<=0):
 print("OOPS!! You Lost the game")






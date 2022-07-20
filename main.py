# There is a 2 digit number in our programme, user have 9 chances to guess it

number = 45
print("Guess the number")
print("There is a secret number and you have total 9 chances to guess it")
chance = 9
while chance >=1:
    num = int(input("Enter your guess: "))
    if num==number:
        print("You guessed it right champ!")
        break
    elif num>number:
        print("Your guess is higher")
    elif num<number:
        print("Your guess is lesser")
    chance -= 1
    print("You have {} chances left".format(chance))
    if chance<1:
        print("Your chances are over, better luck next time!")

import random
print("Welcome to my arcade!")
print("Which activity would you like to choose today?")

Answer = int(input
        ("\n 1) To play Guess the verb press 1 \n\n 2) To Play Number Hunt press 2  \n\n 3) To book Cinema press 3\n\n"))

if Answer == 1:

    Words = ["Walk", "Run", "Jump", "Swim", "Dance", "Climb",
             "Drive", "Fly", "Go", "Come", "Arrive", "Leave"]
    attempts = 0
    secret_word = random.choice(Words)
    done = False
    while not done:
        guess = (input("guess the verb from the following options:"))
        print ("Walk", "Run", "Jump", "Swim", "Dance", "Climb","Drive", "Fly", "Go", "Come", "Arrive", "Leave")
        attempts = attempts + 1

        if guess.casefold() == secret_word.casefold():
            print("yay its is correct")
            print('You took ', attempts, 'attempts to guess it.')
            print("BYE hope you had a nice time")
            done = True

if Answer == 2:

    n = random.randint(1, 100)

    # You have to guess the number between 1 to 100
    print('I have selected a number between 1 and 100. Can you guess?')

    # attempt variable will hold the count of your guess
    attempts = 0

    # done is boolean variable and will hold true or false
    done = False

    # the while loop is the main part of the code, it lets us guess the number as per the hints
    while not done:
        # guess variable with hold guess number
        guess = int(input('Guess the number\n'))
        attempts = attempts + 1

        if guess > n:
            print('My number is smaller than that.\n')

        if guess < n:
            print('My number is larger than that.\n')

        if guess == n:
            print('Yay, that is correct.')
            print('You took ', attempts, 'attempts to guess it.')
            print("BYE hope you had a nice time")
            done = True


if Answer == 3:
    age = int(input("Enter customer age: "))
    show_time = int(input("Enter showtime hour (24-hour format) "))
    ticket_price = 0.0
    
    if age < 0:
        print(" Invalid age entered.")

    elif age <= 3:
        print("  Ticket for Free ")
        ticket_price = 0.0

    elif age <= 12:
        print(" Category: Child")
        ticket_price = 250
        print("Ticket price is 250 rupees")
    elif age <= 20:
        print(" Category: Adult")
        ticket_price = 500
        print("Ticket price is 500 rupees")

    elif age >= 18:
        print(" Category: Adult")
        ticket_price = 500
        print("Ticket price is 500 rupees")



    if ticket_price > 0:

        if show_time < 17:
            print(" Matinee discount applied (-$2.00)")
            ticket_price -= 2.00
        else:
            print(" Evening peak pricing applied (No time discount)")
            print("BYE hope you had a nice time")

else:
    print("Ok bye")

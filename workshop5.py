import random


def guess_random_number(tries, start, stop):
    correct_number = random.randint(start, stop)

    while tries != 0:
        print("You have", tries, "tries left")
        guess = input("Please guess a number between 1 and 10: ")

        if int(guess) == correct_number:
            print("You guessed tha correct number!")
            return

        if int(guess) < correct_number:
            print("Guess higher!")

        if int(guess) > correct_number:
            print("Guess lower!")

        if int(guess) != correct_number:
            tries -= 1
    if tries == 0:
        print("You have failed to guess the correct number which is:",
              correct_number)


guess_random_number(3, 0, 10)


def guess_random_num_linear(tries, start, stop):
    correct_number2 = random.randint(start, stop)
    print("The number for the program to guess is: ", correct_number2)
    print("Number of tries left:", tries)

    for x in range(start, stop+1):
        if x == correct_number2:
            print("The Program is guessing....", x)
            print("The Program guessed the correct number!")
            return
        elif x != correct_number2:
            print("The Program is guessing....", x)
            print("Number of tries left", tries)

        elif tries == 0:
            print("The computer has failed to guess the correct number of",
                  correct_number2)
            return
        tries -= 1


guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    rand_num = random.randint(start, stop)
    print("Random number to find is", rand_num)

    while tries:
        pivot = (start + stop) // 2

        if pivot == rand_num:
            print("Found it!", pivot)
            return
        if pivot > rand_num:
            print("Guessing lower!")
            stop = pivot - 1

        else:
            print("Guessing higher!")
            start = pivot + 1
        tries -= 1
    print("Your program failed to find the number.")


guess_random_num_binary(5, 0, 100)

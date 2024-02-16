def main():
    correct = 12
    valid = 0
    invalid = 0

    print("I'm thinking of a number from 1 to 100")
    while True:

        try:

            guess = int(input("Try to guess my number: "))
            valid += 1
            if guess == correct:
                print(guess, "is correct!", "You guessed my number in", valid, "guesses and made", invalid, "invalid guesses.")
                break
            else:
                print(guess, "is too low -", end=" ")
        except ValueError:
            print("It is not a valid guess -", end=" ")
            invalid += 1


if __name__ == "__main__":
    main()

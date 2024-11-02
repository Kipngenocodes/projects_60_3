import random

def Guess_game(guess, answer):
    if 0< guess < 11:
            if guess == answer:
                print(f'You got it right the number was:  {answer}')
                return True
    else:
        print("I have said between 1 ~ 10. " )
        return False

if __name__ == "__main__":
    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Guess an integer between 1 ~ 10: "))
            if (Guess_game(guess, answer)):
                break
            
        except ValueError:
            print("Please Enter a number: ")
            continue
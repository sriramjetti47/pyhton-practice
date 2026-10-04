import random
comp = random.randint(1,100)
playing = True
while playing:
    user = int(input("enter any number between 1-100: "))

    if user <comp:
        print("too low")
    elif user > comp:
        print("too high")
    elif user == comp:
        print("correct")

        play_again = input("play again?(y/n: ").lower()
        if play_again != "y" :
            playing = False
            print("thanks for palying")



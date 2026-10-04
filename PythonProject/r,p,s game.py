import random

choices = ("rock","paper","scissors")


playing =True
while playing:

     user = input("enter ur choice(rock,paper,scissors): ")
     if  not user in choices:
         print("invalid")
         user = input("enter ur choice(rock,paper,scissors): ")
     comp = random.choice(choices)


     if user == comp :
        print("its a tie")
     elif user == "rock" and comp == "scissors":
        print(f"comp choice: {comp}")
        print("you won")
     elif user == "paper" and comp == "rock":
        print("you won")
        print(f"comp choice: {comp}")
     elif user == "scissors" and comp == "paper":
        print("you won")
        print(f"comp choice:  {comp}")
     else:
        print(f"computer choice is {comp}")
        print("you lose")




















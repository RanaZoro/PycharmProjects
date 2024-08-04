import random
while True:
    choices = ["rock", "paper", "scissors"]
    bot = random.choice(choices)
    userchoice = None
    while userchoice not in choices:
        userchoice = input("Enter One Of The Following Options (rock/paper/scissors) = ").lower()
    if bot == "rock" and userchoice == "rock":
        print("Bot Chose Rock, Its A Tie")
    elif bot == "rock" and userchoice == "paper":
        print("Bot Chose Rock, You Win!")
    elif bot == "rock" and userchoice == "scissors":
        print("Bot Chose Rock, You Lose!")
    elif bot == "paper" and userchoice == "rock":
        print("Bot Chose Paper, You Lose!")
    elif bot == "paper" and userchoice == "paper":
        print("Bot Chose Paper, Its A Tie!")
    elif bot == "paper" and userchoice == "scissors":
        print("Bot Chose Paper, You Win!")
    elif bot == "scissors" and userchoice == "rock":
        print("Bot Chose Scissors, You Win!")
    elif bot == "scissors" and userchoice == "paper":
        print("Bot Chose Scissors, You Lose!")
    elif bot == "scissors" and userchoice == "scissors":
        print("Bot Chose Scissors, Its A Tie!")
    pagain = input("Play Again? (y/n) = ").lower()
    if pagain != "y":
        break
print("Bye!")
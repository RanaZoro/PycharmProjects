def new_game():
    guesses = []
    correct_guesses = 0
    question_no = 1
    for key in quest:
        print("-----------------------------")
        print(key)
        guess = ""
        for i in options[question_no-1]:
            print(i)
        guess = ""
        while guess not in ("A", "B", "C", "D"):
            guess = input("Enter A, B, C, or D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(quest.get(key),guess)
        question_no += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("*BUZZER* WRONG!")
        return 0
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULTS")
    print("Answers: ", end="")
    for i in quest:
        print(quest.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end = " ")
    print()
    score = int(((correct_guesses/len(quest))*100))
    print("Your Score Is = {}%".format(score))
def play_again():
    while True:
        new_game()
        again = input("Do You Want To Play Again? (y/n) = ")
        if again != "y":
            break
#---------------------------------------------------
quest = {"A.Samad's Friend Is?: ":"A",
         "A.Samad's Fav Food?: ":"D",
         "A.Samad's Fav Anime?: ":"B",
         "Sun Rises From: ":"C"
         }
options = [["A. Kashan","B. Ali","C. Huzaifa","D. Umer"],
           ["A. Pulao","B. Karahi","C. Korma","D. Biryani"],
           ["A. Naruto","B. One Piece","C. JJBA","D. JJK"],
           ["A. North","B. West","C. East","D. South"]]
play_again()
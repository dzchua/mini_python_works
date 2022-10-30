# exercise 1
# def return_distincts(para):
#     if sum(para) > 15:
#         return max(para)
#     elif sum(para) < 10:
#         return min(para)
#     elif sum(para) >= 10 and sum(para) <= 15:
#         return sum(para) / 2


# para = [1, 2, 12]
# print(return_distincts(para))

from random import choice

guess = ["pokemon", "microsoft", "aeroplane"]
life = 6
correct = []
incorrect = []
ans = 0
game_over = False


def choices(word):
    choose = choice(word)  # random pick from guess
    diff_letter = len(set(choose))  # store no. of letters that don't repeat themselves
    return choose, diff_letter


def reveal(choose):
    hidden = []
    for l in choose:
        if l in correct:  # append correct guess
            hidden.append(l)
        else:  # remain hidden for the rest/incorrect
            hidden.append("-")
    print(" ".join(hidden))


def ask():
    choose = ""
    is_valid = False
    alpha = "abcdefghijklmnopqrstuvwxyz"
    while not is_valid:
        choose = input("Choose a letter: ")
        if choose in alpha and len(choose) == 1:  # one alphabet chosen
            is_valid = True
        else:
            print("Incorrect letter")
    return choose


def check_letter(choose, hidden_word, life, matches):
    end = False
    if choose in hidden_word and choose not in correct:
        correct.append(choose)
        matches += 1
    elif choose in hidden_word and choose not in correct:
        print("It's the same letter! Choose another.")
    else:
        incorrect.append(choose)
        life -= 1
    if life == 0:
        end = lose()
    elif matches == unique_letter:
        end = win(hidden_word)

    return life, end, matches


def lose():
    print("No life left")
    print("Hidden word: ", word)

    return True


def win(reveal_word):
    reveal(reveal_word)
    print("You guessed right")

    return True


word, unique_letter = choices(guess)

while not game_over:
    print("\n" + "*" * 15 + "\n")
    reveal(word)
    print("\n")
    print("Incorrect letters: " + "-".join(incorrect))
    print(f"Tries: {life}")
    print("\n" + "*" * 15 + "\n")
    letter = ask()
    life, over, ans = check_letter(letter, word, life, ans)
    game_over = over

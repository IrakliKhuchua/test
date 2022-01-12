import random

words = ["crocodile", "painter", "home", "sea", "ship", "shark"]
game = True
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
used_letters = []
health = 6
random_word = random.choice(words)
guess_word = list(random_word)
print("Welcome to Guessing game ^^ \nWord that you should guess looks like this:")

for x in guess_word:
    print("*", end=" ")

print("\nAs you can see, it contains " + str(len(guess_word)) + " letters.\nYou have 6 tries to guess the word. "
      "you can guess it letter by letter, or the whole word. And here is your hint:")

if random_word == words[0]:
    print("\nIt is green, big and dangerous animal. Now guess the letter/word: \nP.s type exit to turn off game \n ")
elif random_word == words[1]:
    print("\nThis is profession. Now guess the letter/word: \nP.s type exit to turn off game \n ")
elif random_word == words[2]:
    print("\nThis is building, that we usually love very much. Now guess the letter/word: "
          "\nP.s type exit to turn off game \n ")
elif random_word == words[3]:
    print("\nBig, blue and mystic. Now guess the letter/word: \nP.s type exit to turn off game \n ")
elif random_word == words[4]:
    print("\nVariation of transport, mostly used in specific geography. Now guess the letter/word: "
          "\nP.s type exit to turn off game \n")
else:
    print("\nType of fish. Now guess the letter/word: \nP.s type exit to turn off game \n ")

while game:
    user_input = input().lower()
    if user_input in used_letters:
        print("You already used that letter. Try another! \n")
    if len(user_input) > 1:
        if user_input.lower() == random_word:
            print("Bravo, you won!")
            break
        elif user_input.lower() == "exit":
            break
        else:
            print("Wrong, try again!: \n")
            health -= 1
            print("You have " + str(health) + " lives left.")
    else:
        if user_input in letters:
            if user_input in guess_word:
                used_letters.append(user_input)
                for x in guess_word:
                    if x in used_letters:
                        print(x, end=" ")
                    else:
                        print("*", end=" ")
                print("\n")
            else:
                print("Wrong, try again!: \n")
                health -= 1
                print("You have " + str(health) + " lives left.")
            letters.remove(user_input)
        else:
            print("You already used that letter. Try another! \n")
    print("This are letters you have not used:")
    print(letters)
    if len(used_letters) == len(guess_word):
        print("Congratulations, You Won!")
        break
    if health == 0:
        print("You Lost!")
        break

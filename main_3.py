import random
easy_words=["apple", "banana","tiger","india","money"]
medium_words=["python", "bottle","monkey","planet","laptop"]
hard_words=["elephent", "computer","dimond","umbrella","mountain"]

print("Welcome to the password guessing game")
print("choose a level: easy,medium,hard")
while True:
    level = input("choose the level: ").lower()
    if level == "easy":
        secret = random.choice(easy_words)
    elif level=="medium":
        secret = random.choice(medium_words)
    elif level=="hard":
        secret = random.choice(hard_words)
    else:
        print("invalid choice.defulting to easy level")
        secret = random.choice(easy_words)
    attempts = 0
    print("\nGuess the secret password")
    while True:
        guess = input("Enter your guess: ").lower()
        attempts+=1
        if guess==secret:
            print(f'congratulation! you guessed it in {attempts} attempts.')
            break
        hint = ""
        for i in range(len(secret)):
            if i<len(guess) and guess[i]==secret[i]:
                hint+=guess[i]
            else:
                hint+="_"
        print("Hint",hint)
    choice = input("do you want to play more (yes/no)")
    if choice == "no":
        print("thank you to play")
        break





    
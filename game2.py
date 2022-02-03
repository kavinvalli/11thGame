import words
import random
number_of_attempts = 10
attempt_number = 1
word = words.words[random.randint(0, len(words.words) - 1)]
guessed_chars = []
print(f"{len(word)} letter word")
for _ in word:
    guessed_chars.append('_')
while attempt_number <= number_of_attempts:
    guess = input(f"Guess number {attempt_number}: ")
    for i in range(len(guess)):
        if guess[i] == word[i]:
            guessed_chars[i] = word[i]
    if "".join(guessed_chars) == word:
        print("GUESSED")
        break
    print("".join(guessed_chars))
    attempt_number += 1
else:
    print("Number of attempts over")
    print(word)

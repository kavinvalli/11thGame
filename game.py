import words
import sys
import time
import random
seconds_left = 60
random_words = []
number_of_chars = 0
current_number_of_chars = 0
MAX_LIMIT = 40
for i in range(MAX_LIMIT):
    word = words.words[random.randint(0, len(words.words) - 1)]
    while word in random_words:
        word = words.words[random.randint(0, len(words.words) - 1)]
    else:
        number_of_chars += len(word)
        random_words.append(word)

print(" ".join(random_words))
print("")
to_start = input("Hit enter when you are ready ")
start = time.time()
user_input = input("Enter the words: ").split(" ")
end = time.time()
for i in range(MAX_LIMIT):
    if len(user_input) > i:
        for j in range(len(list(random_words[i]))):
            if len(user_input[i]) > j:
                if random_words[i][j] == user_input[i][j]:
                    current_number_of_chars += 1
accuracy = current_number_of_chars / number_of_chars * 100
raw_wpm = len(user_input) / ((end-start)/60)
wpm = accuracy / 100 * raw_wpm
print(f"Your accuracy is {accuracy}")
print(f"Your raw wpm is {raw_wpm}")
print(f"Your wpm is {wpm}")
sys.exit(0)

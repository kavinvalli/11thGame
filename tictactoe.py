from random import randint

tiles = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

toss_player = int(input("Which player will call during the toss (1 / 2)? "))
toss_choice = input("Heads or tails? (H/T)\n> ")
toss_won_by = 1
heads_or_tails = "h" if randint(0, 1) == 0 else "t"
while toss_choice.lower() != "h" and toss_choice.lower() != "t":
    print("You need to choose h or t")
    toss_choice = input("Heads or tails? (H/T)\n>")
else:
    print("\n" * 40)
    text = "Heads" if heads_or_tails == "h" else "Tails"
    if heads_or_tails == toss_choice.lower():
        print("You picked right! It was indeed", text)
        toss_won_by = toss_player
    else:
        print("You picked wrong! It was", text)
        toss_won_by = 1 if toss_player == 2 else 2

toss_choice_position = int(input(
    f"Player {toss_won_by}, Do you want to go first or second (1 / 2)? "))

if toss_choice_position == 1:
    player_number = toss_won_by
else:
    player_number = 1 if toss_won_by == 2 else 2

print(f"Player {player_number} will start")

input("Press enter when ready!")

print("\n" * 40)
print("Game Begins")

for row in tiles:
    print(" |", " | ".join(row), "| ")
print(f"Player {player_number}")

won = False
drawn = False

while not won and not drawn:
    correct_tile_filled = False
    player_input_row = 4
    player_input_column = 4
    while correct_tile_filled == False:
        player_input_row = input("Enter row (1 / 2 / 3)\n> ")
        while player_input_row == None or player_input_row == '':
            print("Enter Something!")
            player_input_row = input("Enter row (1 / 2 / 3)\n> ")
        player_input_row = int(player_input_row) - 1
        while player_input_row < 0 or player_input_row > 2:
            print("The row number needs to be either 1, 2, or 3")
            player_input_row = int(input("Enter row (1 / 2 / 3)\n> ")) - 1
        player_input_column = input("Enter column (1 / 2 / 3)\n> ")
        while player_input_column == None or player_input_column == '':
            print("Enter Something!")
            player_input_column = input("Enter column (1 / 2 / 3)\n> ")
        player_input_column = int(player_input_column) - 1
        while player_input_column < 0 or player_input_column > 2:
            print("The column number needs to be either 1, 2, or 3")
            player_input_column = int(
                input("Enter column (1 / 2 / 3)\n> ")) - 1
        if tiles[player_input_row][player_input_column] != "_":
            print("You cannot fill an already filled tile")
        else:
            correct_tile_filled = True
            break
    tiles[player_input_row][player_input_column] = "O" if player_number == 1 else "X"
    print('\n' * 40)
    for row in tiles:
        print(" |", " | ".join(row), "| ")
    row_1_correct = tiles[0][0] == tiles[0][1] == tiles[0][2] != "_"
    row_2_correct = tiles[1][0] == tiles[1][1] == tiles[1][2] != "_"
    row_3_correct = tiles[2][0] == tiles[2][1] == tiles[2][2] != "_"
    column_1_correct = tiles[0][0] == tiles[1][0] == tiles[2][0] != "_"
    column_2_correct = tiles[0][1] == tiles[1][1] == tiles[2][1] != "_"
    column_3_correct = tiles[0][2] == tiles[1][2] == tiles[2][2] != "_"
    diagonal_1_correct = tiles[0][0] == tiles[1][1] == tiles[2][2] != "_"
    diagonal_2_correct = tiles[0][2] == tiles[1][1] == tiles[2][0] != "_"
    if (row_1_correct
            or row_2_correct
            or row_3_correct
            or column_1_correct
            or column_2_correct
            or column_3_correct
            or diagonal_1_correct
            or diagonal_2_correct
            ):
        won = True
        print(f"Player {player_number} won")
    else:
        draw = True
        for row in tiles:
            if '_' in row:
                draw = False
        if draw:
            print("The game is drawn")
            break
        else:
            player_number = 2 if player_number == 1 else 1
            print("Player", player_number)

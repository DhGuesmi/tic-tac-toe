game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_game(game_to_print):
    print("---------\n",
          "\b|", game_to_print[0][0], game_to_print[0][1], game_to_print[0][2], "|\n",
          "\b|", game_to_print[1][0], game_to_print[1][1], game_to_print[1][2], "|\n",
          "\b|", game_to_print[2][0], game_to_print[2][1], game_to_print[2][2], "|\n",
          "\b---------")


print_game(game)  # Print empty grid


def coordinates_tester(game_input, coordinates):
    if coordinates[0].isdigit() == False or coordinates[1].isdigit() == False:
        print("You should enter numbers!")
        return False
    elif 1 > int(coordinates[0]) or int(coordinates[0]) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif 1 > int(coordinates[1]) or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif game_input[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True


def win_tester(game_input, player):
    if [game_input[0][i] for i in range(0, 3)].count(player) == 3 or \
            [game_input[1][i] for i in range(0, 3)].count(player) == 3 \
            or [game_input[2][i] for i in range(0, 3)].count(player) == 3 \
            or [game_input[i][0] for i in range(0, 3)].count(player) == 3 \
            or [game_input[i][1] for i in range(0, 3)].count(player) == 3 \
            or [game_input[i][2] for i in range(0, 3)].count(player) == 3 \
            or [game_input[0][0], game_input[1][1], game_input[2][2]].count(player) == 3 \
            or [game_input[0][2], game_input[1][1], game_input[2][0]].count(player) == 3:
        return 1
    else:
        return 0


player = "X"
round_number = 1
while True:
    while True:
        player_input = input("Enter the coordinates: ").split()
        if coordinates_tester(game, player_input):
            game[int(player_input[0])-1][int(player_input[1])-1] = player
            print_game(game)
            break
    if win_tester(game, player):
        print(player, "wins!")
        break
    elif round_number == 9:
        print("Draw")
        break
    else:
        round_number += 1
        if round_number % 2 == 0:
            player = "O"
        else:
            player = "X"

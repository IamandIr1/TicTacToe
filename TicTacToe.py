import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal Win
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (-)!")
            return True

    # Diagonal Win
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True

    # Vertical Win
    for col in range(len(game)):
        check = []

    for row in game:
        check.append(row[col])

    if all_same(check):
        print(f"Player {check[0]} is the winner vertically (|)!")
        return True
    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Please select another.")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Erro: Be sure to input row/col as 0 | 1 or 2? Becasue", e)
        return False

    except Exception as e:
        print("Something went horribly wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:

    game_size = int(input("What size of tic tac toe would you like to play? (Must be a number): "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column choice do you want to play (0, 1, 2)?: "))
            row_choice = int(input("What row choice do you want to play (0, 1, 2)?: "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        if win(game):
            game_won = True
            again = input("Game is over, would you like to play again? (Y/N)")
            if again.lower() == "y":
                print("Restarting game...")
            elif again.lower() == "n":
                print("Ok, great game!")
                play = False
            else:
                print("Sorry, not a valid input. Exiting game...")
                play = False

'''
game = game_board(game, just_display=True)
game = game_board(game, player=1, row=3, column=2)
'''

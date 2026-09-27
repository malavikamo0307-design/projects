def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def play_game():
    board = [" "] * 9
    player = "X"

    while True:
        display_board(board)
        print("Player", player)

        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number from 1 to 9.")
                continue

            position -= 1

            if board[position] != " ":
                print("That position is already occupied.")
                continue

            board[position] = player

            if check_winner(board, player):
                display_board(board)
                print("Player", player, "wins!")
                break

            if " " not in board:
                display_board(board)
                print("It's a draw!")
                break

            if player == "X":
                player = "O"
            else:
                player = "X"

        except ValueError:
            print("Invalid input! Please enter a number.")


while True:
    play_game()

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break
from tictactoe.helper import get_character_choice, get_move_input
from tictactoe.player import Player
from tictactoe.tictactoe import TicTacToeBoard


# ... (get_character_choice and get_move_input functions here)



def play_game():
    tictactoe_board = TicTacToeBoard()

    character_choice1 = get_character_choice(1)
    player1 = Player("Player 1", character_choice1)

    character_choice2 = "X" if character_choice1 == "O" else "O"
    player2 = Player("Player 2", character_choice2)

    for _ in range(9):
        tictactoe_board.print_board()

        row, col = get_move_input(player1)
        while not player1.make_move(tictactoe_board.board, row, col):
            print("Invalid move. Try again.")
            row, col = get_move_input(player1)

        if tictactoe_board.check_winner():
            print(f"{player1.name} wins!")
            break

        tictactoe_board.print_board()

        row, col = get_move_input(player2)
        while not player2.make_move(tictactoe_board.board, row, col):
            print("Invalid move. Try again.")
            row, col = get_move_input(player2)

        if tictactoe_board.check_winner():
            print(f"{player2.name} wins!")
            break

    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()

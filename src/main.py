import random

class TicTacToe:
    def __init__(self):
        self.board = list(' ' * 10)
        self.player_turn = self.random_first_player()

    def random_first_player(self):
        return random.choice(['X', 'O'])
    
    def show_board(self):
        print("\n")
        print(f"{self.board[1]}|{self.board[2]}|{self.board[3]}")
        print("-----")
        print(f"{self.board[4]}|{self.board[5]}|{self.board[6]}")
        print("-----")
        print(f"{self.board[7]}|{self.board[8]}|{self.board[9]}")
        print("\n")

    def is_board_full(self):
        return ' ' not in self.board[1:]
    
    def swap_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O' 
        else:
            self.player_turn = 'X'

    def fix_spot(self, cell, player):
        self.board[cell] = player

    def has_player_won(self, player):
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]

        for win in win_combinations:
            if all([self.board[cell] == player for cell in win]):
                return True
            
        return False
    
    def start(self):
        while True:
            self.show_board()
            print(f"Player {self.player_turn} turn")
            cell = int(input("Enter sell number from 1 to 9: "))

            if 1 <= cell <= 9 and self.board[cell] == ' ':
                self.fix_spot(cell, self.player_turn)

                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print("Congrats! You Won!")
                    break

                if self.is_board_full():
                    print("Draw!")
                    break

                self.swap_player()

            else:
                print("Invalid choice. Try again")
                continue
    

if __name__ == '__main__':
    game = TicTacToe()
    game.start()

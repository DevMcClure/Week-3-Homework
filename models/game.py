class Game:
    def __init__(self):
       self.how_to_win = {
           "rock": "scissors",
           "paper" : "rock",
           "scissors" : "paper",
           
       }
        
    def win_game(self, player1, player2):
        if self.how_to_win[player1.choice.lower()] == player2.choice.lower():
            winner = player1
        elif self.how_to_win[player2.choice.lower()] == player1.choice.lower():
            winner = player2
        return winner

 
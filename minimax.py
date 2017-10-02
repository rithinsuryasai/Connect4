import maxconnect4
from MaxConnect4Game import *

class miniMax:
    def minimax(self,current_state_of_the_game):
        print "This is the current state right now"
        print ' -----------------'
        for i in range(6):
            print ' |',
            for j in range(7):
                print('%d' % current_state_of_the_game[i][j]),
            print '| '
        print ' -----------------'
        current_game = maxConnect4Game()
        current_game.playPiece(self,1)
        # print('Score: Player 1 = %d, Player 2 = %d\n' % (maxconnect4.maxConnect4Game.player1Score, maxconnect4.maxConnect4Game.player2Score))



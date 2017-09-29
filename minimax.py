from MaxConnect4Game import *
get_max_connect_methods = maxConnect4Game()
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

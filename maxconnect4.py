#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
import os
from MaxConnect4Game import *
import time

def oneMoveGame(currentGame,depth):
    start = time.time()
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    currentGame.aiPlay(int(depth)) # Make a move (only random is implemented)

    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()
    print "Time take for the computers decision is"
    print time.time() - start


def interactiveGame(currentGame,next_chance,depth,inFile):

    if next_chance == "human-next":
        print "Its humans turn now"
        while currentGame.pieceCount != 42:
            userMove = input("Enter the column number [1-7] where you would like to play : ")
            if not 0 < userMove < 8:
                print "Invalid column number!"
                continue
            if not currentGame.playPiece(userMove - 1):
                print "This column is full!"
                continue

            if os.path.exists("input.txt"):
                print "Do not reset the game"
            else:
                game_state = "0000000\n0000000\n0000000\n0000000\n0000000\n0000000\n1"
                text_file = open("input.txt", "w")
                text_file.write(game_state)
                text_file.close()
            try:
                currentGame.gameFile = open("human.txt", 'w')
                #currentGame.playPiece(userMove)
                #currentGame.gameFile.write(currentGame.gameBoard)
                print "You have made a move at column "+str(userMove)
                currentGame.printGameBoardToFile()
                currentGame.gameFile.close()
                print "Computer will think "+str(depth)+" steps ahead and make a move"
                if currentGame.currentTurn == 1:
                    currentGame.currentTurn = 2
                elif currentGame.currentTurn == 2:
                    currentGame.currentTurn = 1
                currentGame.aiPlay(int(depth))
                currentGame.gameFile = open("computer.txt", 'w')
                # currentGame.playPiece(userMove)
                # currentGame.gameFile.write(currentGame.gameBoard)
                print "Computer has made a move at column " + str(currentGame.computer_column)
                currentGame.printGameBoardToFile()
                currentGame.printGameBoard()
                currentGame.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                #print currentGame.checkPieceCount()
                #print currentGame.gameBoard()
                currentGame.gameFile.close()
            except Exception,e:
                print e

    elif next_chance == "computer-next":
        currentGame.aiPlay(int(depth))
        currentGame.gameFile = open("computer.txt", 'w')
        # currentGame.playPiece(userMove)
        # currentGame.gameFile.write(currentGame.gameBoard)
        print "Computer has made a move at column " + str(currentGame.computer_column)
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        interactiveGame(currentGame,"human-next",depth,inFile)

    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    currentGame.aiPlay() # Make a move (only random is implemented)

    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    next_chance = argv[3]
    depth = argv[4]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame,next_chance,depth,inFile) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,depth) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



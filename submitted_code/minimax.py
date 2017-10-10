def minimax(self, current_node):
    current_state = copy.deepcopy(current_node)
    for i in range(0, 6, 1):
        if self.playPiece(i) != None:
            # print self.gameBoard
            if self.pieceCount == 42:
                self.gameBoard = copy.deepcopy(current_state)
                return i
                # return np.argmax(score_list)
            else:
                # print self.gameBoard
                # print "first tree"
                # print self.gameBoard
                score_list.append(self.min_value(self.gameBoard))
                self.gameBoard = copy.deepcopy(current_state)
                # for s in score_list:
                #    print s
                # print self.gameBoard
                # return np.argmax(score_list)


def max_value(self, current_node):
    parent_node = copy.deepcopy(current_node)
    v = -infinity
    track_of_child_nodes = []
    for j in range(0, 6, 1):
        current_state = self.playPiece(j)
        if current_state != None:
            # print j
            track_of_child_nodes.append(self.gameBoard)
            self.gameBoard = copy.copy(parent_node)

    if track_of_child_nodes == []:
        # print "This is the score for maximum"
        # print self.player1Score
        score = self.eval_function(self, self.gameBoard)
        self.countScore1(self.dashBoard)
        return self.player1Score
    else:
        max_score_list = []
        for child in track_of_child_nodes:
            # print self.pieceCount
            # print "This is for Max Player"
            # print child
            self.gameBoard = copy.deepcopy(child)
            v = max(v, self.min_value(child))
            # print "Value of v from max"
            # print v
            # max_score_list.append(v)
        return v


def min_value(self, current_node):
    parent_node = copy.deepcopy(current_node)
    if self.currentTurn == 1:
        opponent = 2
    elif self.currentTurn == 2:
        opponent = 1
    # if self.pieceCount == 42:
    #     return self.player1Score

    v = infinity
    track_of_child_nodes = []
    for j in range(0, 6, 1):
        current_state = self.checkPiece(j, opponent)
        if current_state != None:
            track_of_child_nodes.append(self.gameBoard)
            self.gameBoard = copy.copy(parent_node)

    if track_of_child_nodes == []:
        # print "this is the final score for minimum"
        self.countScore1(self.gameBoard)
        return self.player1Score
    else:
        for child in track_of_child_nodes:
            # print self.pieceCount
            # print "This is for opponent"
            # print child
            self.gameBoard = copy.deepcopy(child)
            v = min(v, self.max_value(child))
            # print "this is the value of v which will be sent"
            # print v
        return v
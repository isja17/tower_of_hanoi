from toh_game import Game
from copy import deepcopy
import data_structures

class searchAgent( Game ):
    """
    In this I have implemented a search agent which uses either breadthFirstSearch
    or depthFirstSearch to try to solve the tower of hanoi. They work, and I am
    sure they can solve the problem (bfs certain can, as it is garunteed to find
    a solution if one exists), but they take a crazy amount of time because there
    are so many possibilities. Look at the bottom to see how dfs acts when there
    are only 5 poles, then imagine adding more.

    breadthFirstSearch was a bit of an after thought for me, and the primary reason
    I did it is to see if my code and the game actually work because I originally
    was setting the number of poles to be too high to see if depthFirstSearch was
    doing what its supposed to. That is why I did not (re)implement the Queue myself,
    but theother data structures used are mine.
    """
    def __init__(self, numPieces):
        self.game = Game(numPieces)
        self.initState = self.game.getStartState()

    def getStartState(self):
        return self.initState

    def isGoalState(self, gameState):
        return self.game.isGoalState(gameState)

    def isLegal(self, gameState, startPoleI, targetPoleI):
        """
        True only if a move follows the rules of tower of hanoi
        """
        targetPole = gameState[targetPoleI]
        startPole = gameState[startPoleI]

        if len(startPole) == 0: return False

        #dont allow moves to same pole.
        if startPoleI == targetPoleI: return False

        #if target pole has pieces in it
        if len(targetPole) != 0:
            piece = startPole[0]
            if targetPole[0] < piece: return False
            #bigger pieces cannot be put onto smaller ones

        return True

    def getSuccessors(self, gameState):
        """
        returns [([succState], (startPoleI, targetPoleI)), ... ]
        """
        copy = deepcopy(gameState)
        successors = []
        actions = self.game.legalActions(gameState)

        for action in actions:
            startPole = action[0]
            targetPole = action[1]

            #simulate the move on copy
            result = self.simAction(copy, startPole, targetPole)

            #put result into successor
            successors.append((result, (action[0], action[1])))

            #reset copy
            copy = gameState

        return successors

    def simAction(self, gameState, startPoleIndex, targetPoleIndex):
        """
        Returns the resulting succState without changing the real gameState

        note: it does change the real game state right now sadly
        """
        copy = deepcopy(gameState)
        piece = copy[startPoleIndex][0]
        copy[targetPoleIndex].insert(0, piece)
        copy[startPoleIndex].remove(piece)
        return copy

    def depthFirstSearch(self):
        """
        note: this is from my ai course. same with breadthFirstSearch.
        
        depth first search is an algorithm that shoots down the tree, which represents
        gameStates and moves, as fast as it possibly can. This means it is not
        garunteed to be optimal, and it will often take a ton of time.

        Regardless, this returns a list of actions from the start state to the
        goal state.
        """
        startNode = deepcopy(self.getStartState())
        stack = data_structures.Stack()

        explored = []
        stack.push( (startNode, []) )
        while not stack.isEmpty():

            currState, actions = stack.pop()

            if currState not in explored:
                explored.append(currState)

                if self.isGoalState(currState):
                    actions.append([])
                    return actions

                successors = self.getSuccessors(currState)
                for succState, action in successors:
                    newAction = actions + [action]
                    stack.push((succState, newAction))

    def breadthFirstSearch(self):
        """
        Like DFS, but we don't shoot down the tree, we traverse through each node
        at depth before going down further. This means it is garunteed to be optimal,
        and if the number of poles is small, it will be faster than DFS.

        Returns a list of actions from start to goal states.
        """
        startNode = deepcopy(self.getStartState())
        queue = data_structures.Queue()
        explored = []
        queue.enQueue((startNode, []))

        while not queue.isEmpty():

            currState, actions = queue.deQueue()

            if currState not in explored:
                explored.append(currState)

                if self.isGoalState(currState):
                    actions.append([])
                    return actions

                successors = self.getSuccessors(currState)
                for succState, action in successors:
                    newAction = actions + [action]
                    queue.enQueue((succState, newAction))

    def searchDFS(self):
        print "Starting search with DFS...."
        actions = self.depthFirstSearch()
        self.game.doActions(self.initState, actions)

    def searchBFS(self):
        print "Starting search with BFS...."
        actions = self.breadthFirstSearch()
        self.game.doActions(self.initState, actions)


search = searchAgent(5).searchBFS()


"""
With only 5 pieces, here is what depthFirstSearch returns for me:

[(0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1), (0, 2), (1, 2),
(2, 0), (1, 2), (0, 2), (2, 1), (2, 0), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1),
(0, 2), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (1, 2),
(0, 2), (2, 1), (2, 0), (1, 2), (2, 0), (1, 2), (0, 2), (2, 1), (0, 2), (1, 2),
(2, 0), (2, 1), (0, 2), (2, 1), (2, 0), (1, 2), (2, 0), (1, 2), (0, 2), (2, 1),
(2, 0), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (2, 1),
(0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (1, 2), (0, 2), (2, 1), (2, 0), (1, 2),
(2, 0), (2, 1), (0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1),
(0, 2), (1, 2), (2, 0), (1, 2), (0, 2), (2, 1), (2, 0), (1, 2), (2, 0), (1, 2),
(0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1), (2, 0), (1, 2),
(2, 0), (1, 2), (0, 2), (2, 1), (2, 0), (1, 2), (2, 0), (1, 2), (0, 2), (2, 1),
(0, 2), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (1, 2),
(0, 2), []]


On the other hand, breadthFirstSearch is garunteed to find a solution provided the state
space is finite, i.e. if it wont have to consider infinite many moves. And,
since it does not in this case, it returns:

[(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (0, 1), (2, 1), (2, 0),
(1, 0), (2, 1), (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (1, 0),
(2, 1), (2, 0), (1, 0), (1, 2), (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2),
(0, 2), []]
"""

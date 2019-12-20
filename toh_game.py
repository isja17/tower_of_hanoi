import matplotlib.pyplot as plt
#tet getSucc whatever (last fn)
class Game():
    """
    All stuff related to the gameState. Go to readme for more information.
    """
    def __init__(self, numPieces):
        """
        initializes game state data

        note: using a large number of pieces will cause search algos to take a very long time
        as 1) the number of steps needed grows exponentially and 2) the number
        of possible gameStates increases drasticlly.
        """
        self.numPieces = numPieces
        self.numPoles = 3
        self.poles = [[] for _ in range(self.numPoles)]
        [self.poles[0].append(i) for i in range(self.numPieces)]
        self.initState = self.poles
        self.goalPoleIndex = -1 #change to test if other poles possible

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

    def legalActions(self, gameState):
        """
        find each possible legal move. Returns a list of tuples:
        [(startPoleIndex, targetPoleIndex), .... ]
        """
        actions = []
        if len(gameState[self.goalPoleIndex])-1 == self.numPieces:
            return None

        for pole in range(self.numPoles): #for each pole

            if len(gameState[pole]) != 0: #if our pole has things on it

                for nextPole in range(self.numPoles): #for each remaining pole

                    if nextPole != pole:#if its not curr pole

                        if self.isLegal(gameState, pole, nextPole):
                            actions.append((pole, nextPole))
        return actions


    def doAction(self, gameState, startPoleIndex, targetPoleIndex):
        """
        Takes in a gameState and proposed piece move. Returns the updated
        gameState
        """
        #this should always be true, but its best to be safe
        if self.isLegal(gameState, startPoleIndex, targetPoleIndex):
            piece = gameState[startPoleIndex][0]
            gameState[targetPoleIndex].insert(0, piece)
            gameState[startPoleIndex].remove(piece)
            return gameState

    def doActions(self, gameState, actionList):
        """
        actionList = [(startPoleIndex, targetPoleIndex), .. ]
        goes through each action, updating and visualizing the gamestate
        """
        print actionList
        if actionList == None:
            return gameState

        for action in actionList:

            if action == None or action == []:
                print "No moves left. Resulting game state:"
                print gameState
                if self.isGoalState(gameState):
                    print "Victory!"
                return gameState

            if self.isLegal(gameState, action[0], action[1]):
                gameState = self.doAction(gameState, action[0], action[1])
                print gameState
        return gameState


    def visualizeGame(self, gameState):
        """
        represents the game as a bar graph.
        """
        x_axis = ("pole 0", "pole 1", "pole 2")
        heights = [len(pole) for pole in gameState]
        plt.bar(x_axis, heights)
        plt.show()

    def isGoalState(self, gameState):
        return len(gameState[self.goalPoleIndex]) == self.numPieces

    def getStartState(self):
        return self.initState

    def getNumPieces(self):
        return self.numPieces

    def getNumPoles(self):
        return self.numPoles

    def getPoles(self):
        return self.poles

#Here is an example of how you can play by yourself. Just uncomment them.
#you can also do it move-wise instead of a list of actions, but I just put
#new actions at the end of actionlist to make my moves

game = Game(10)
#gameState = game.getStartState()
#print gameState
#game.legalActions(gameState)
#gameState = game.doActions(gameState, [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), []])
#print gameState

Tower of Hanoi Overview:

This is a program for the tower of hanoi puzzle. The puzzle goes as follows:
Imagine you have three poles. On one of these poles, generally the left-most,
sits N discs which are in ascending order, i.e. the smallest piece is on top,
the biggest is on the bottom. Now you are tasked with moving the pieces on this
start pole to the right-most pole with the following rules:

	1. You can only move one piece at a time
  	2. Bigger pieces cannot be set ontop of smaller pieces
  	3. Each move takes the top-most disc from one pole and moves it to the top-most position on the target pole




Files overview:

toh_game: all of the stuff that controls the game; where actions are

search_agent: all the stuff that goes into making breadth first search and depth
first search work

data_structures: my implementation of node, double link list, stack, queue





How to use the AI/search algorithms:

Firstly, this is in python 2.7, so have that installed.
In terminal, go to tower_of_hanoi directory and run 
search_agent.py.

When you do this, you will see the game states that the search algo is considering.

When it finds an answer, you will also see the list of actions it took to get to goal.

Note: you can change the number of pieces and the search algorithm at the bottom of search_agent
There you will find:

search = searchAgent(5).searchBFS()

If you want to change the number of pieces, change the 5.

If you want depth first search, change searchBFS() to searchDFS().

I suggest not putting more than 10 pieces because the state space and minimum
number of moves necessary to get to goal grows exponentially.

To play the game yourself:

Go to toh_games.py, create a Game() object, initialize the game, and make your actions.
I have an example of how to do this at the bottom of toh_games.
After this, simply run toh_games from terminal.





Game state information:

In my program, the poles are represented as:

[ [left-pole], [middle-pole], [right-pole] ]

The pieces are represented as ints from 0 to n-1 where n = number of discs.
The smaller the int, the smaller the piece.

For instance, if we have 5 pieces, the game starts off like this:
[ [0, 1, 2, 3, 4], [ ], [ ] ]

A move is represented as (startPoleIndex, targetPoleIndex).

A legal move from the initial polition is (0, 1):
[ [1, 2, 3, 4], [0], [ ] ]

An illegal move from this position is (0, 1):
[ [2, 3, 4], [1, 0], [ ] ] because 1 > 0.





Data Structures:

All of my data structures are, as you would expect, in data_structures.py.
In this, I reimplemented node, double linked list, stack and queue. The stack uses
the linked list which uses the node, same as queue. I use the stack in depth first
search and queue in breadth first search.



Depth First Search:

Imagine the game as a tree where gameStates are nodes and actions are edges.
Everytime dfs considers a new node, it puts it into a lifo (last in, first out)
stack. As a result, instead of traversing the tree by level like breadth first
search does, it goes as deep into the tree it can everytime an element is pop'd.
By utilizing lifo, depth first search can be faster than breadth first search if
 the solution to the problem is expected to take many moves. Because the number o
 f moves grows by an exponential amount in relation to the number of pieces there
 are, depth first search is fasterr than breadth first search when there are many
pieces. I find both take a very long time when numPieces >= 10. Also, both search
algorithms have space issues. I have 8 gbs of ram and DFS ran out of space for
when numPieces = 10. I had a bunch of other stuff running on my pc though, too.




Breadth First Search:

BFS uses a (first in, first out) queue. As a result, this traverses the tree by
level/breadth instead of shooting down the tree. Although this may take longer as
the number of pieces grows, it is garunteed to be optimal (provided the branching
factor is finite, which it is) and complete (provided the state space is finite)

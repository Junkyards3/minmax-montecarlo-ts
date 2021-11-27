# minmax-montecarlo-ts
A basic implementation of min-max with alpha-beta pruning and monte carlo tree search algorithm together with a basic game interface. Basic games are Power Four and TicTacToe.

# How to use
You need to run the main.py file. In order to change the used algorithm, comment and uncomment the corresponding lines. Note that each turn of the MCTS takes 5 seconds to complete
(This can be changed in the corresponding class). You can change the game by changing the type of game used. TicTacToeGameN is a variation of TicTacToeGame where you can choose the 
size of the grid.
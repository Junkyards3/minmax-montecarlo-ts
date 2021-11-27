import numpy as np
import random as rd
import math

import TicTacToeGame as gm
import TicTacToeGameN as gmn
import PowerFour as p4
import alpha_beta_node as nd
import monte_carlo_node as mc
		
if __name__ == '__main__' :
	t = gmn.tic_tac_toe_game_n(4)
	print(str(t))
	human = False
	while not t.ended_game() :
		if human:
			t = t.human_input()
			# n = nd.alpha_beta_node(t)
			# t = n.get_move(depth = 7)
		else : 
			# n = nd.alpha_beta_node(t)
			# t = n.get_move()
			n = mc.monte_carlo_node(t)
			t = n.get_move()
		human = not human
		print("Turn ended\n" + str(t))
	print(t.score())
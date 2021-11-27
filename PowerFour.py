import numpy as np

class connect_four : 

	def __init__(self, grid = np.zeros((6,7),dtype=int), player = 1) :
		self.player = player 
		self.grid = grid 
		
	def copy(self) :
		grid = self.grid.copy()
		return connect_four(grid,self.player)
		
	def play(self,c) :
		grid = self.grid.copy()
		if c < 0 or c > 6 :
			raise IndexError("Position hors du plateau")
		if grid[0,c] != 0 :
			raise IndexError("Colonne pleine")
		i = 0
		while i < 5 and grid[i+1,c] == 0:
			i += 1
		grid[i,c] = self.player 
		return connect_four(grid,3 - self.player)	
		
	def get_actions(self) :
		r = [i for i in range(7) if self.grid[0,i] == 0]
		return r 
		
	def __str__(self) :
		s = "Player : " + str(self.player) + "\n"
		s += str(self.grid)
		return s 
		
	def given_player_wins(self,player) :
		d = player
		g = self.grid
		i = np.array([d,d,d,d])
		s = []
		#lignes
		for l in range(6) :
			for c in range(4) :
				if g[l,c] == d and g[l,c+1] == d and g[l,c+2] == d and g[l,c+3] == d :
					return True
		#colonnes
		for c in range(7) :
			for l in range(3) :
				if g[l,c] == d and g[l+1,c] == d and g[l+2,c] == d and g[l+3,c] == d :
					return True
		#diagonales
		for l in range(3) :
			for c in range(4) :
				if g[l,c] == d and g[l+1,c+1] == d and g[l+2,c+2] == d and g[l+3,c+3] == d :
					return True
		#antidiagonales
		for l in range(3) :
			for c in range(3,7) :
				if g[l,c] == d and g[l+1,c-1] == d and g[l+2,c-2] == d and g[l+3,c-3] == d :
					return True
		return False
		
	def curr_player_wins(self) :
		return self.given_player_wins(self.player)
		
	def other_player_wins(self) :
		return self.given_player_wins(3 - self.player)
		
	def score(self) :
		if self.given_player_wins(2) :
			return -1
		elif self.given_player_wins(1) :
			return 1
		else :
			return 0
			
	def ended_game(self) :
		return len(self.get_actions()) == 0 or self.curr_player_wins() or self.other_player_wins()
		
	def human_input(self) :
		y = int(input("Colonne : "))-1
		return self.play(y)
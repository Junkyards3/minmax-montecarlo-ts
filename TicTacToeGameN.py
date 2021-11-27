import numpy as np

class tic_tac_toe_game_n :
	
	def __init__(self, n, grid = None, player = 1) :
		self.player = player
		if not grid is None:
			self.grid = grid 
		else :
			self.grid = np.full((n,n),0)
		self.n = n

	
	def copy(self) :
		grid = self.grid.copy()
		return tic_tac_toe_game_n(self.n,grid,self.player)
		
	def play(self,c) :
		x,y = c
		grid = self.grid.copy()
		if x < 0 or x > self.n-1 or y < 0 or y > self.n-1 :
			raise IndexError("Position hors du plateau")
		if grid[x,y] != 0 :
			raise IndexError("Position déjà jouée")
		grid[x,y] = self.player 
		return tic_tac_toe_game_n(self.n,grid,3 - self.player)
	
	def get_actions(self) :
		r = [(x,y) for x in range(self.n) for y in range(self.n) if self.grid[x,y] == 0]
		return r 
		
	def __str__(self) :
		s = "Player : " + str(self.player) + "\n"
		s += str(self.grid)
		return s 
		
	def given_player_wins(self,player) :
		d = player
		g = self.grid
		i = np.full(self.n,d)
		s = []
		#lignes
		s += [g[i,:] for i in range(self.n)]
		#colonnes
		s += [g[:,i] for i in range(self.n)]
		#diagonales
		s.append(g.diagonal())
		s.append(g[::-1,...].diagonal())
		return any(np.array_equal(i, x) for x in s)
		
	def curr_player_wins(self) :
		return self.given_player_wins(self.player)
		
	def other_player_wins(self) :
		return self.given_player_wins(3 - self.player)
		
	def score(self) :
		if self.given_player_wins(2) :
			return -1
		elif self.given_player_wins(1) :
			return 1
		elif not (0 in self.grid) :
			return 0
			
	def ended_game(self) :
		return len(self.get_actions()) == 0 or self.curr_player_wins() or self.other_player_wins()
		
	def human_input(self) :
		x = int(input("Ligne : "))-1
		y = int(input("Colonne : "))-1
		return self.play((x,y))
class alpha_beta_node :
	def __init__(self,game) :
		self.game = game 

	def is_terminal(self) :
		return self.game.ended_game()
		
	def compute_value(self,alpha,beta,max_player,depth) :
		if self.is_terminal() or depth == 0 :
			v = self.game.score()
			return (v,self.game)
		elif max_player :
			v = -10000
			g = None
			for action in self.game.get_actions() :
				child = alpha_beta_node(self.game.play(action))
				w,h = child.compute_value(alpha,beta,False,depth-1)
				if w > v : 
					v = w 
					g = child.game
				alpha = max(alpha,v)
				if v >= beta : 
					break 
			return (v,g)
		else :
			v = 10000
			g = None
			for action in self.game.get_actions() :
				child = alpha_beta_node(self.game.play(action))
				w,h = child.compute_value(alpha,beta,True,depth-1)
				if w < v :
					v = w 
					g = child.game
				beta = min(beta,v)
				if alpha >= v : 
					break 
			self.value = v
			return (v,g)

	def get_move(self,depth = -1) :
		v,g = self.compute_value(-10000,10000,True,depth)
		return g
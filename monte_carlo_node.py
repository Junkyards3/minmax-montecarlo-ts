import math as mt
import random as rd
import time 

class monte_carlo_node :
	def __init__(self,game,parent = None) :
		self.game = game
		self.n = 0
		self.score = 0
		self.children = []
		self.parent = parent
	
	def ucb(self,c = mt.sqrt(2)) :
		if self.n == 0 :
			return float('inf')
		else :
			return self.score/self.n + c*mt.sqrt(mt.log(self.parent.n)/self.n)

	def best_ucb_child(self,c = mt.sqrt(2)) :
		ch = None 
		v = -float('inf')
		for child in self.children :
			w = child.ucb(c)
			if w > v :
				ch = child 
				v = w
		return ch

	def select(self) :
		node = self 
		while len(node.children) > 0 :
			node = node.best_ucb_child()
		return node 

	def rollout(self) :
		g = self.game.copy()
		while not g.ended_game() :
			action = rd.choice(g.get_actions())
			g = g.play(action)
		return g.score()

	def expand(self) :
		for action in self.game.get_actions() :
			self.children.append(monte_carlo_node(self.game.play(action),self))

	def backprop(self,value) :
		self.score += value*(-1 if self.game.player == 1 else 1)
		self.n += 1
		if self.parent != None :
			self.parent.backprop(value)

	def step(self) :
		leaf = self.select()
		v = 0 
		if leaf.game.ended_game() :
			v = leaf.game.score()
			chosen_node = leaf
		else :
			leaf.expand()
			chosen_node = rd.choice(leaf.children)
			v = chosen_node.rollout()
		chosen_node.backprop(v)

	def get_move(self, allowed_time = 5) :
		begin_time = time.time()
		while time.time() - begin_time < allowed_time :
			self.step()
		return self.best_ucb_child(c = 0).game

	def __str__(self) :
		s = "----------------------\nChildren :\n"
		for child in self.children :
			s += str(child.game) + "\n" + str(child.score) + "/" + str(child.n) +"\n-------"
		return s + "\n----------------------"
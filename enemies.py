import random, os, time
from pathFinder import mazeShortestPath
from typing import List

# checks whether the given coordinates are in bound
def inBound(board: List[List[int]], i: int, j: int) -> bool:
	return 0 <= i and i < int(len(board)) and 0 <= j and j < int(len(board[0]))

def distance(x1, y1, x2, y2):
	# manhattan distance
	return abs(x1 - x2) + abs(y1 - y2);

class Enemy:
	def __init__(self,x,y,enemy_type = "Einfacher Fiend"):
		self.x=x
		self.y=y
		self.lives=0
		self.enemy_type=enemy_type
		self.enemy_symbol= self.get_symbol()
		self.movement = random.choice(["w", "s", "a","d"])
		

		self.path = [];
		self.pathIndex = 0;

	# the enemy will slowly approach this position
	def findPathTo(self, lvl, destX, destY):
		# if distance is too little, the enemy will make an educated guess, since pathfinding takes too long

		# if distance(self.x, self.y, destX, destY) <= 3:
		if self.path == []:
			self.path=[];
			print("finding optimal path....");
			self.path = mazeShortestPath(lvl, [self.y, self.x], [destY, destX]);
			for coord in self.path:
				lvl[coord[0]][coord[1]] = '10';
		# else:

		# 	minDist = None;
		# 	minX = None;
		# 	minY = None;
		# 	dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]];
		# 	for dir in dirs:
		# 		nx = self.x + dir[0];
		# 		ny = self.y + dir[1];

		# 		dis = distance(nx, ny, destX, destY);
		# 		if inBound(lvl, ny, nx):
		# 			if (minDist == None or dis < minDist):
		# 				minDist = dis;
		# 				minX = nx;
		# 				minY = ny;

		# 	self.path = [[minY, minX]];
		# 	self.pathIndex = 0;
			





	def move(self):
		# enemy only finds its path if it has a path to follow, 
		# otherwise it uses the patrol algorithm
		if (self.path != []):
			self.x = self.path[self.pathIndex][1];
			self.y = self.path[self.pathIndex][0];
			self.pathIndex += 1;
			if (self.pathIndex == len(self.path)):
				self.path = [];
				self.pathIndex = 0;
				

		# patrol algorithm: the enemy patrols a certain area
		else:
			if self.movement == "w":
				self.y+=1
			if self.movement == "s":
				self.y-=1
			if self.movement == "a":
				self.x-=1
			if self.movement == "d":
				self.x+=1
	#if x y cords are "not in" lvl_1 move, else, pick antoher cord
  #def patrol(self):



	def attack(self, lvl):
		os.system("clear")
		print("A "+self.enemy_type+" is engaging you in battle")
		time.sleep(1)
		rolls = input("how many times do you want to roll the dice(1-10 times)? (the average between 2-6 is taken)")
		try:
			int(rolls)
		except TypeError:
			rolls = input("please enter a number")
		rolls=int(rolls)
		roll_total=0
		for i in range(rolls):
			roll_total += random.randint(2,6)
		roll_average= roll_total/rolls
		roll_average = round(roll_average)
		print("You rolled "+str(roll_average))
		enemy_roll=random.randint(1,4) + 1*self.atk
		time.sleep(0.5)
		print("The enemy rolled " + str(enemy_roll))
		time.sleep(0.5)
		if enemy_roll>roll_average:
			print("Oh No, You lost "+enemy_roll-roll_average+" lives!")
			return enemy_roll-roll_average
		elif enemy_roll<roll_average:
			print("The enemy lost "+str(abs(enemy_roll-roll_average))+" live(s)!")
			self.lives+= enemy_roll-roll_average
			print(self.lives)
			if self.lives<=0:
				print("Yay you killed the enemy")

				return 0
				
			return 0
		else:
			print("yall tied!")
			return 0
		
		
		

	def get_symbol(self):

		# if self.enemy_type=="Einfacher Fiend":
		self.lives=2 
		self.atk = 1 
		return "☿"
		

		#This enemy's info is: health=2/2 and attack=1 and speed=moves 1 space when the player moves 1 space.
		if self.enemy_type=="schneller Junge":
			self.lives = 1 
			self.atk = 1  
			return "👿" 
		#This enemy's info is: health=1/1 and attack=1 and speed=moves 2 spaces when the player moves 1 space.
		if self.enemy_type=="Der Fels der Fels hält den Fels nicht auf":
			self.lives = 3
			self.atk = 2 
			return "👹"
		#This enemy's info is: health=3/3 and attack=2 and speed=moves 1 space when the player moves 2 spaces.
		if self.enemy_type=="Bismark":
			self.lives = 10
			self.atk = 4 
			return "🚢"
		#This enemy's info is: health=10/10 and attack=4 and speed=moves 1 space when the player moves 3 spaces.
		if self.enemy_type=="Cher Ami":
			self.lives = 2
			self.atk = 2
			return "🕊️"
		#This enemy's info is: health=2/2 and attack=2 and speed=moves 1 space when the player moves 1 space.
		if self.enemy_type=="Wir sehen uns im großen Jenseits,Dummkopf":
			self.lives = 2
			self.atk = 5
			return "💣"
		#This enemy's info is: health=2/2 and attack=5 and speed=moves 2 spaces when the player moves 1 space.

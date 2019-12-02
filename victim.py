import namegenerator
from googletrans import Translator
import time
from random import randint as rd
from typing import List

trans = Translator();

# checks whether the given coordinates are in bound
def inBound(board: List[List[int]], i: int, j: int) -> bool:
	return 0 <= i and i < int(len(board)) and 0 <= j and j < int(len(board[0]));

class Victim():
	def __init__(self, x = None, y = None):
		self.x = x;
		self.y = y;
		self.name = trans.translate(namegenerator.gen(), dest='de').text.replace("-", ' ');
		print(self.name);
	def catchDisease(self, victimList, lvl):
		print(self.name + " has caught the disease! cough cough. uurrrrghhh💀 💀 💀 💀")
		time.sleep(0.5)
		print(self.name + " has died")
		#This is the healthy/non-diseased victim:😃
        #This is the dead/diseased victim:💀
		time.sleep(0.5)
		victimList.remove(self);
		lvl[self.y][self.x] = '0';
	
	# random generates a position for the victim
	def generatePos(self, lvl):
		while (True):
			randX = rd(0, len(lvl[0]));
			randY = rd(0, len(lvl));
			if (inBound(lvl, randY, randX) and lvl[randY][randX] == '0'):
				self.x = randX;
				self.y = randY;
				break;


			#Opfermann
			#nononononononoononononnonon, are you making it so its a random location?
			# cant you just make a list of all the cordinates, and then tell it to put it at a ranom location? ah ok
			# but we might be making more levels
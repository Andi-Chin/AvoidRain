from readchar import readkey
import sys
from sys import stdout
import os
import time
import termcolor
import namegenerator
import random

from pathFinder import mazeShortestPath
from enemies import Enemy
from victim import Victim

time


termcolor.cprint("JackLesher, Andi, Kobe, and BenjaminNamika1 present...", "green")
#time.sleep(3)
termcolor.cprint("Blatherskite!", "red")
termcolor.cprint("Welcome to our game!", "yellow")
#time.sleep(2);
s = """You have created a disease and you must share it with the world! \n
This is how it works:
'█' represents a wall. 'o' represents you, the player. '☿ ,👿 ,👹 ,🚢 ,🕊️ , and💣' represent enemys who think the world should stay around a for little longer. \n
Have fun! Go destroy the world like there's no tomorrow
(Because there won't after you infect everyone)! 
This is a WASD maze game. This is a very fragile program. Move slowly so you won't break it. Based on how fast you move your character, you may experience extreme lagging.\n \nThis game is cooler if you play this in the background: https://www.youtube.com/watch?v=pQHbFsZbEcg&t=453s
Here are your victims:""" 
# hey we could use termcolor
disease=input("What will you name your disease?")
print("Look out world! Here comes the ",disease," disease!")
termcolor.cprint(s, "magenta");
#time.sleep(20); #change back to 15 when done 


lvl_1 = [
    list("11111111111111111111111111111111111111111111111111"),
    list("11000000550000000000000000000000000000000000006611"),
    list("11001100110000111111001111110011111111111111000011"),
    list("11001100001100000000110001100000000000000000110011"),
    list("11000000111111111100110011000116611111110011110011"),
    list("11001100011000011000110011000001100110001111000011"),
    list("11001100011001111100110011110000000110001100110011"),
    list("11001100110011000000110000011110000110001100000011"),
    list("11000000110011001111111110000111100000001100110011"),
    list("11111100110011000000110000011110000110000000110011"),
    list("77000000110011111100110001110006600111111100110011"),
    list("11111100110011001100110000000100000110001100110011"),
    list("11000000110000111100111100011111111110001100110011"),
    list("11001111110000001100100000000000000000001100110011"),
    list("11001100000011000000111000011111111111111100110011"),
    list("11001100001111110000111001111000000000000000110011"),
    list("11000000110011111111000000001100111111111100110011"),
    list("11000000000000110001100111111100110000000000000011"),
    list("11001101111100111100011000000000110011001111110011"),
    list("11001100000000001100000011111111001100110000110011"),
    list("11001100110011110011000000000000100000001100110011"),
    list("11000000001100000000110011111100111100550000550011"),
    list("11006600550000001100000000001100000000001100110011"),
    list("11111111111111111111111111801111111111111111111111")
];


victimList = [];
for i in range(5):
    v = Victim();
    v.generatePos(lvl_1);
    victimList.append(v);

class Player():
    def __init__(self):
        self.x=1
        self.y=10
        self.oldx=1
        self.oldy=10
        self.move_dir=""
        self.health=4
        self.name = namegenerator.gen();
    def move(self,lvl):
        if self.move_dir=="w":
            if lvl[self.y-1][self.x]!="1" and self.y!=0:
                self.y-=1
        if self.move_dir=="a":
            if lvl[self.y][self.x-1]!="1"and self.x!=0:
                self.x-=1
        if self.move_dir=="s":
            if lvl[self.y+1][self.x]!="1":
                self.y+=1
            elif lvl[self.y][self.x]=="8" or lvl[self.y][self.x-1] =="8":
                print("You Won!")
                print("The disease was so effective, that you wiped out the entire human race! Gut gemacht.")
                sys.exit()
        if self.move_dir=="d":
            if lvl[self.y][self.x+1]!="1":
                self.x+=1    
        if lvl[self.y][self.x]=="6":
            if (self.x==4 and self.y==22) or (self.x==5 and self.y==22):
                self.x+=27
                self.y=4
            elif (self.x==31 and self.y==4) or (self.x==32 and self.y==4):
                self.x-=27
                self.y=22
            elif (self.x==len(lvl[1])-4 and self.y==1) or (self.x==len(lvl[1])-3 and self.y==1):
                self.y+=9
                self.x-=15

            elif (self.x==len(lvl[1])-18 and self.y==10) or (self.x==len(lvl[1])-19 and self.y==10):
                self.y-=9
                self.x+=15
player = Player()


def random_enemy():
    list_of_enemies = ["Einfacher Fiend","schneller Junge","Der Fels der Fels hält den Fels nicht auf","Bismark","Cher Ami","Wir sehen uns im großen Jenseits,Dummkopf"]
    random.shuffle(list_of_enemies)
    return list_of_enemies[0]

def random_x_y(lvl):
    x=random.randint(0,len(lvl[0])-1)
    y=random.randint(0,len(lvl)-1)
    while lvl[y][x]!="0":
        x=random.randint(0,len(lvl[0])-1)
        y=random.randint(0,len(lvl)-1)
    return x,y

def print_maze(lvl, enemyList):
	t=-1
	dead=[]
	for vic in victimList:
		lvl[vic.y][vic.x] = '11';
		if vic.x == player.x and vic.y == player.y:
			vic.catchDisease(victimList, lvl);
			if victimList==[]:
				os.system("clear")
				print("Congraduations!!")
				time.sleep(0.5)
				print("You Shared your disease with everybody!")

	for enemy in enemyList:
		t+=1
		enemy.findPathTo(lvl, player.x, player.y);
		lvl[enemy.y][enemy.x] = '3';
		enemy.move();
		if enemy.x==player.x and enemy.y==player.y:
			player.health-=enemy.attack(lvl_1)
		if enemy.lives<=0:
			dead.append(t)
	for i in dead:
		del enemyList[i]
	
	if len(enemyList)<=1:
		enemy = (random_x_y(lvl_1),random_enemy())
	

	for y in range(len(lvl)):
		for x in range(len(lvl[0])):
			if y == player.y and x == player.x:
				print("o" , end = "");
			if lvl[y][x] == '0':
				print(" ",end="")
			elif lvl[y][x] == '1':
				print("█",end="")#termcolor.colored("█","grey"),end="")
			elif lvl[y][x] == '3':  #enemy
				for i in range(len(enemyList)):
					if y==enemyList[i].y and x == enemyList[i].x:
						print(enemyList[i].enemy_symbol,end="")
				lvl[y][x] = '0'; #clearing them from the screen after drawing
			elif lvl[y][x] == '5':
				termcolor.cprint("█","grey",end="") #secret entrances
			elif lvl[y][x] == '6':
				termcolor.cprint("█","cyan",end="") # teleportation pads
			elif lvl[y][x] == '7':
				termcolor.cprint("█","red",end="") # start pad
			elif lvl[y][x] == '8':
				print("█",end="") # end pad
			elif lvl[y][x] == '10':
				termcolor.cprint("*", "blue", end = "");
			elif lvl[y][x] == '11':
				print("😃", end = "");
            

		print();
        

#print_maze(lvl_1, []);


def newinput(): 
    stdout.write("\u001b[31mDisease Name: " + disease + " || health: " + str(player.health) + "/4\u001b[37m")
    
    #\u001b[31m
    #\u001b[37m


    stdout.flush()
    player.move_dir = str(readkey())

enemyList = [];
# xx,yy=random_x_y(lvl_1)
# e1 = Enemy(xx,yy, "Einfacher Fiend")
# xx,yy=random_x_y(lvl_1) # 2 different enemies
# e2 = Enemy(xx,yy, random_enemy())
# # e1.findPathTo(lvl_1, player.x, player.y);
# enemyList.append(e1);
# enemyList.append(e2)
e1 = Enemy(2, 2);
enemyList.append(e1);

while True:
    os.system("clear")
    print_maze(lvl_1,enemyList)
    newinput()
    player.move(lvl_1)


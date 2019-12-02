from typing import List
from math import inf
from copy import deepcopy
# I first protoyped this program in C++, check our repl profile for orginal program

# for debugging purposes-turns a matrix into formatted string 
def strMt(m):
	res = "";
	for row in m:
		for d in row:
			res += str(d) + " ";
		res += "\n";
	res += "\n";
	return res;
	
# checks whether a given tile is passable
def validTile(tile):
	return tile != '1' and tile != '6' and tile != '5';

# vertices
class Vert():
	def __init__(self: 'Vert', i: int, j: int) -> None:
		self.cost: int = inf;
		self.parent: int = -1;
		self.i = i;
		self.j = j;
	def __repr__(self: 'Vert') -> str:
		return "%s:%s" % (self.i, self.j);

# returns a shortest path tree using dijsktra's algorithm
def dijsktra(mG: List[List[int]], altvts: List[Vert]) -> List[Vert]:
	vts: List[Vert] = deepcopy(altvts);

	sptSet: List[int] = [];
	outSet: List[int] = [];
	for c in range(len(mG)):
		outSet.append(c);
	while (True):
		minInd: int = 0;
		for i in range(len(outSet)):
			if (vts[outSet[i]].cost < vts[outSet[minInd]].cost):
				minInd = i;
		minV: int = outSet[minInd];
		for j in range(len(mG)):
			if (mG[minV][j] != 0):
				inOutSet: bool = False;
				for v in outSet:
					if v == j:
						inOutSet = True;
				if inOutSet:
					newCost: int = vts[minV].cost + mG[minV][j];
					if (newCost < vts[j].cost):
						vts[j].cost = newCost;
						vts[j].parent = minV;
				
		sptSet.append(minV);
		outSet.remove(outSet[minInd]);
				
		if (len(outSet) == 0):
			break;
	return vts;

# returns a list of vertices in the shortest path
def shortestPath(vts: List[Vert], src: int, dest: int) -> List[int]:
	res: List[int] = [];
	res.append(dest);
	cur: int = dest;

	while (cur != src):
		cur = vts[cur].parent;
		res.append(cur);
	
	return res[::-1];

# add undirected edge
def addUndir(mG: List[List[int]], v1: int, v2: int, w: int) -> None:
	mG[v1][v2] = w;
	mG[v2][v1] = w;

# counts number of vertices in the maze
def countV(board: List[List[int]]) -> int:
	numV: int = 0;
	for i in range(len(board)):
		for j in range(len(board[0])):
			if (validTile(board[i][j])):
				numV += 1;
	return numV;

# checks whether the given coordinates are in bound
def inBound(board: List[List[int]], i: int, j: int) -> bool:
	return 0 <= i and i < int(len(board)) and 0 <= j and j < int(len(board[0]));

# creates an adjacency matrix given a maze
def makeMg(mG: List[List[int]], vts: List[Vert], board: List[List[int]]) -> None:
	vG: List[List[int]] = [];
	numV: int = 0;
	for i in range(len(board)):
		row: List[List[int]] = [];
		for j in range(len(board[0])):
			if (validTile(board[i][j])):
				vts.append(Vert(i, j));
				row.append(numV);
				numV += 1;
			else:
				row.append(0);
		vG.append(row);
	dirs: List[List[int]] = [[0, 1], [1, 0], [-1, 0], [0, -1]];
	for i in range(len(board)):
		for j in range(len(board[0])):
			if (validTile(board[i][j])):
				for dir in dirs:
					ni: int = i + dir[0];
					nj: int = j + dir[1];
					if (inBound(board, ni, nj)):
						if (validTile(board[ni][nj])):
							addUndir(mG, vG[i][j], vG[ni][nj], 1);
			
# finds the shortest path given a maze/board
def mazeShortestPath(board: List[List[int]], src: List[int], dest: List[int]) -> List[List[int]]:

	mG: List[List[int]] = [];
	for i in range(countV(board)):
		row: List[int] = [];
		for j in range(countV(board)):
			row.append(0);
		mG.append(row);
	vts: List[Vert] = [];
	makeMg(mG, vts, board);
	srcV: int = None;
	destV: int = None;


	for k in range(len(vts)):
		if (vts[k].i == src[0] and vts[k].j == src[1]):
			srcV = k;
		if (vts[k].i == dest[0] and vts[k].j == dest[1]):
			destV = k;
	if (srcV == None or destV == None):
		# xD I can't fix this so the enemy just will have to stay still for one turn lol
		return [];

	
	vts[srcV].cost = 0;
	dij: List[Vert] = dijsktra(mG, vts);
	pathh: List[int] = shortestPath(dij, srcV, destV);

	coords: List[List[int]] = [];

	for v in pathh:
		coords.append([vts[v].i, vts[v].j]);
  
	return coords

# # 0 meaning air, 1 means object
# board: List[List[int]] = [
# 	list("01111"),
# 	list("00111"),
# 	list("10001"),
# 	list("11011"),
# 	list("10000"),
# ];

# coords = mazeShortestPath(board, [1, 1], [4, 1]);
# for coord in coords:
# 	board[coord[0]][coord[1]] = 9


# print(strMt(board));

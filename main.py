import time
import heapq
num = 0

class State:
    """
    Class to represent the tiles in the 3*3 puzzle. 
    The class contains

    Each state has:
    board <- each index represents a tile's coordinate. index 0<- tile 1...index 8 <- tile 0
    h <- Int: Manhattan distance
    g <- Int: distance from start to current
    x, y <- Int, Int: coordinate of the blank tile(0)
    d <- Int: cost bound
    """

    def __init__(self, puzzle):
        self._board = []
        self.ltoco(puzzle)
        self._x = self._board[8][0]
        self._y = self._board[8][1]
        self._g = 0
        self._h = 0
        self._d = 0
        self._cost = 0
    
    def __repr__(self):
        """
        for print instruction to State
        print the current board with tiles
        """
        state_str = ""
        for i in range(3):
            for j in range(3):
                co = [i, j]
                tile = self._board.index(co) + 1
                if tile == 9:   tile = 0
                state_str += str(tile) + " "
            state_str += "\n"
        return state_str


    def ltoco(self, puzzle):
        """
        convert the list to the coordinate in tile order (1-8,0) and save in self._board
        """
        for i in range(9):
            index = puzzle.index(i) 
            # print("i, index, board: ", i, index, [index // 3, index % 3])
            if i == 0:
                temp = index
                continue
            self._board.append([index // 3, index % 3])
        self._board.append([temp // 3, temp % 3])
    

    def cotol(self, coordinate):
        """
        convert the coordinate to the puzzle list
        """
        puzzle = []
        for i in range(9):
            puzzle.append([])
        for i in range(3):
            for j in range(3):
                index = coordinate.index([i, j])
                if index == 8:
                    index = 0
                else:
                    index += 1
                puzzle[i*3+j] = index
        return puzzle



    def successors(self):
        """
        receives a state and returns a list with the tile could move in current state
        """
        children = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) == abs(j):
                    # pass diagonal moving or no moving
                    continue
                if self.is_valid_pair(self._x + i, self._y + j):
                    temp = self._board.index([self._x + i, self._y + j])
                    coordinate = self._board.copy()
                    coordinate[temp] = [self._x, self._y]
                    coordinate[8] = [self._x + i, self._y + j]
                    puzzle = self.cotol(coordinate)
                    s = State(puzzle)
                    s._g += 1
                    children.append(s)
        return children

    def is_valid_pair(self, x, y):
        """
        Verifies if an x-y pair is valid for the board.
        """
        if x < 0 or y < 0:
            return False
        if x >= 3 or y >= 3:
            return False
        return True
        
    


class IDAStar:

    def h_value(self, state):
        """
        calculate the ideal (Manhattan) distance from current state to goal.
        The distance only includes the 8 number tiles.
        The blank tile(0) is excluded.
        """
        d = 0
        for i in range(3):
            for j in range(3):
                tile = state._board[i*3+j]
                if tile == [2, 2]:
                    continue
                d += abs(tile[0] - i) + abs(tile[1] - j)
                # print("m: ", i*3+j+1, state._board[i*3+j], d)
        return d

    
    def dfs(self, n, goal, d, max_bound):
        """
        dfs algorithm
        receive the current state, goal state and the 
        """
        n._g = d
        n._cost = d + self.h_value(n)
        if n._board == goal._board:
            return "FINISH"
        if n._cost > max_bound:
            return n._cost
        min = float("inf")
        for n_i in n.successors():
            if n_i not in self.PATH:
                self.PATH.append(n_i)
                d = self.dfs(n_i, goal, d+1, max_bound)
                if d == "FINISH":
                    return d
                if d < min:
                    min = d
                self.PATH.pop(-1)
        return min

        


    def search(self, start, goal):
        """
        IDA* Algorithm
        """
        flag = 0 # flag for if the search is done
        max_bound = self.h_value(start)
        self.PATH = [start]

        while True:
            d = self.dfs(start, goal, 0, max_bound)
            if d == "FINISH":
                return (self.PATH, max_bound)
            if d == float("inf"):
                return ([], None)
            max_bound = d
                




def main():
    start = State([1,2,3,4,6,0,7,5,8])
    # start = State([1, 2, 3, 4, 5, 6, 7, 0, 8])
    goal = State([1, 2, 3, 4, 5, 6, 7, 8, 0])
    a = IDAStar()
    path, step = a.search(start, goal)
    if step != None:
        print("The step of solution is shown below: \n")
        for state in path:
            print(state)
            print()
    else:
        print("Didn't find solution.")
    return

if __name__ == "__main__":
    main()
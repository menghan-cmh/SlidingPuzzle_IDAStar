import time
import heapq


class State:
    """
    Class to represent the tiles in the 3*3 puzzle. 
    The class contains

    Each state has:
    board <- each index represents a tile's coordinate. index 0<- tile 1...index 8 <- tile 0
    h <- Int: Manhattan distance
    x, y <- Int, Int: coordinate of the blank tile(00)
    """

    def __init__(self, puzzle):
        self._board = []
        self.ltoco(puzzle)
        self._x = self._board[8][0]
        self._y = self._board[8][1]
        self._g = 0
        self._h = 0
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
                    s = State(self._x + i, self._y + j)
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

    
    def dfs(self):
        return
        


    def search(self, start, goal):
        """
        IDA* Algorithm
        """
        self.OPEN = []
        start.set_h(self.h_value(start))
        heapq.heappush(self.OPEN, start)
        node_expanded = 0

        flag = 0 # flag for if the search is done
        while flag == 0:
            n = heapq.heappop(self.OPEN)
            node_expanded += 1
            if n == goal:
                return n.get_cost(), node_expanded
            for n_i in n.successors():
                self.dfs()
                




def main():
    start = State([5, 2, 7, 8, 4, 0, 1, 3, 6])
    goal = State([1, 2, 3, 4, 5, 6, 7, 8, 0])
    a = IDAStar()

    print("Manhattan: ", a.h_value(start))
    #IDAStar.search(start, goal)
    return

if __name__ == "__main__":
    main()
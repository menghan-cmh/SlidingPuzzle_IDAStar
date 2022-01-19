def is_solvable(state):
    """
    parameter: the list number in puzzle order
    return: True if solvable(even inversions)
    """
    sum = 0
    for i in range(9):
        num = 0
        if state[i] == 0: continue
        for j in range(i+1, 9):
            if state[j] == 0: continue
            if state[i] > state[j]:
                num += 1
        sum += num
    return (sum%2 == 0)



def manhatton(state):
    """
    parameter: the list number in puzzle order
    return: the manhatton distance
    """
    sum = 0
    goal = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]] # index is the num
    for i in range(3):
        for j in range(3):
            tile = state[i*3+j]
            if tile == 0: continue
            sum += abs(goal[tile][0] - i) + abs(goal[tile][1] - j)
    return sum



def show(state):
    for i in range(3):
        string = ""
        for j in range(3):
            string += str(state[i*3+j]) + " "
        print(string+"\n")


flag = 0
def idaStar(puzzle, track, x, y, lastd, step, max):
    """
    parameter:
    return: 
    """
    flag = 0
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    if flag: return True
    for i in range(4):
        if flag: return True

        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x>2 or next_y>2 or next_x<0 or next_y<0: continue # out of board
        if lastd + i == 3: continue # opposite direction

        #swap
        temp = puzzle[x*3+y]
        puzzle[x*3+y] = puzzle[next_x*3+next_y]
        puzzle[next_x*3+next_y] = temp

        mht = manhatton(puzzle)
        if mht == 0:
            track[step] = (dx[i], dy[i])
            flag = 1
            print("The least step to solve the maze is", step+1)
            print(track)
            exit(0)
        if mht+step <= max:
            if flag: return True
            track[step] = (dx[i], dy[i])
            idaStar(puzzle, track, next_x, next_y, i, step+1, max)
        
        #swap
        temp = puzzle[x*3+y]
        puzzle[x*3+y] = puzzle[next_x*3+next_y]
        puzzle[next_x*3+next_y] = temp
    return False




def main():
    start = list(map(int, input().split()))
    
    for i in range(9):
        if start[i] == 0:
            # the blank tile's position
            x = i//3
            y = i%3

    if not is_solvable(start):
        print("unsolvable\n")
        exit(0)
    
    h = manhatton(start)
    if h == 0:
        print("The maze is solved")
        return
    d = 0
    track = dict()
    while(1):
        done = idaStar(start, track, x, y, -1, 0, d)
        if done:
            break
        d += 1
    
    return

if __name__ == '__main__':
    main()
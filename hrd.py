COLUMNS = 4


import sys
import heapq as hq

def read(path):
    f = open(path, 'r')
    contents = f.readlines()
    f.close()
    # contents = ["1234\n", ]
    grid = []
    for i in range(len(contents)):
        grid.append([int(contents[i][0]), int(contents[i][1]), int(contents[i][2]), int(contents[i][3])])
    return grid

def edit_grid(solution):
    sol = []
    for array_orriginal in solution:
        array = helper_copy(array_orriginal)
        for i in range(len(array)):
            for n in range(len(array[i])):
                if array_orriginal[i][n] != 7 and array_orriginal[i][n] != 1 and array_orriginal[i][n] != 0:
                    num = array_orriginal[i][n]
                    if i + 1 < len(array) and array_orriginal[i+1][n] == num:
                        array[i][n] = 3
                        array[i+1][n] = 3
                    elif n + 1 < len(array[i]) and array_orriginal[i][n+1] == num: 
                        array[i][n] = 2
                        array[i][n+1] = 2
                elif array_orriginal[i][n] == 7:
                    array[i][n] = 4
        sol.append(array)
    return sol
    

def is_goal_state(array):
    if array == []:
        return False
    return array[3][1] == array[3][2] == array[4][1] == array[4][2] == 1


def helper_copy(lst):
    a = []
    for i in range(len(lst)):
        if type(lst[i]) == list or type(lst[i]) == tuple:
            a.append(helper_copy(lst[i]))
        else:
            a.append(lst[i])
    return a

def successors(array):
    lst = []
    for i in range(len(array)):
        for n in range(len(array[i])):
           
            if array[i][n] == 0:
                if i - 1 >= 0:
                    if array[i - 1][n] == 7:
                        cpy = helper_copy(array)
                        cpy[i - 1][n] = 0
                        cpy[i][n] = 7

                        if cpy not in lst:
                            lst.append(cpy)
                    if i - 2 >= 0 and 7 > array[i - 1][n] == array[i-2][n] > 1:
                        
                        assert(i - 2 >= 0)
                        cpy = helper_copy(array)
                        cpy[i - 2][n] = 0
                        cpy[i][n] = array[i - 1][n]
                        if cpy not in lst:
                            lst.append(cpy)
                    if n-1 >= 0 and 7 > array[i - 1][n] == array[i - 1][n -1] > 1 and array[i][n -1] == 0:
                        cpy = helper_copy(array)
                        cpy[i - 1][n] = 0
                        cpy[i-1][n-1] = 0
                        cpy[i][n] = array[i - 1][n]
                        cpy[i][n - 1] = array[i - 1][n]
                        if cpy not in lst:
                            lst.append(cpy)
                    if n + 1 < len(array[i]) and array[i][n+1] == 0 and 7 > array[i-1][n+1] == array[1-1][n] > 1:
                            cpy = helper_copy(array)
                            cpy[i - 1][n] = 0
                            cpy[i-1][n+1] = 0
                            cpy[i][n] = array[i-1][n+1]
                            cpy[i][n + 1] = array[i-1][n+1]
                            if cpy not in lst:
                                lst.append(cpy)
                    if array[i - 1][n] == 1:
                        assert(i - 2 >= 0)
                        if n-1 >= 0 and array[i][n -1] == 0 and array[i - 1][n -1] == 1: 
                            cpy = helper_copy(array)
                            cpy[i - 2][n] = 0
                            cpy[i-2][n-1] = 0
                            cpy[i][n] = 1
                            cpy[i][n - 1] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                        elif n + 1 < len(array[i]) and array[i][n+1] == 0 and array[i-1][n+1] == 1:
                            cpy = helper_copy(array)
                            cpy[i - 2][n] = 0
                            cpy[i-2][n+1] = 0
                            cpy[i][n] = 1
                            cpy[i][n + 1] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                if i + 1 < len(array):
                    if array[i + 1][n] == 7:
                        cpy = helper_copy(array)
                        cpy[i + 1][n] = 0
                        cpy[i][n] = 7
                        if cpy not in lst:
                            lst.append(cpy)
                    if i + 2 < len(array) and 7 > array[i + 1][n] == array[i+2][n] > 1:
                        assert(i + 2 < len(array))
                        cpy = helper_copy(array)
                        cpy[i + 2][n] = 0
                        cpy[i][n] = array[i + 1][n]
                        if cpy not in lst:
                            lst.append(cpy)
                    if n-1 >= 0 and 7 > array[i + 1][n] == array[i + 1][n -1] > 1 and array[i][n -1] == 0:
                        cpy = helper_copy(array)
                        cpy[i + 1][n] = 0
                        cpy[i+1][n-1] = 0
                        cpy[i][n] = array[i + 1][n]
                        cpy[i][n - 1] = array[i + 1][n]
                        if cpy not in lst:
                            lst.append(cpy)
                    if n + 1 < len(array[i]) and array[i][n+1] == 0 and 7 > array[i+1][n+1] == array[i + 1][n] > 1:
                        cpy = helper_copy(array)
                        cpy[i + 1][n] = 0
                        cpy[i+1][n+1] = 0
                        cpy[i][n] = array[i + 1][n]
                        cpy[i][n + 1] = array[i + 1][n]
                        if cpy not in lst:
                            lst.append(cpy)
                    if array[i + 1][n] == 1:
                        assert(i + 2 < len(array))
                        if n-1 >= 0 and array[i][n - 1] == 0 and array[i + 1][n -1] == 1: 
                            cpy = helper_copy(array)
                            cpy[i + 2][n] = 0
                            cpy[i+2][n-1] = 0
                            cpy[i][n] = 1
                            cpy[i][n - 1] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                        elif n + 1 < len(array[i]) and array[i][n+1] == 0 and array[i+1][n+1] == 1:
                            cpy = helper_copy(array)
                            cpy[i + 2][n] = 0
                            cpy[i+2][n+1] = 0
                            cpy[i][n] = 1
                            cpy[i][n + 1] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                if n - 1 >= 0:
                    if array[i][n - 1] == 7:
                        cpy = helper_copy(array)
                        cpy[i][n - 1] = 0
                        cpy[i][n] = 7
                        if cpy not in lst:
                            lst.append(cpy)
                    if n - 2 >= 0 and 7 > array[i][n - 1] == array[i][n-2] > 1:
                        assert(n - 2 >= 0)
                        cpy = helper_copy(array)
                        cpy[i][n - 2] = 0
                        cpy[i][n] = array[i][n - 1]
                        if cpy not in lst:
                            lst.append(cpy)
                    if i-1 >= 0 and 7 > array[i][n - 1] == array[i - 1][n -1] > 1 and array[i - 1][n] == 0:
                        cpy = helper_copy(array)
                        cpy[i][n - 1] = 0
                        cpy[i-1][n-1] = 0
                        cpy[i][n] = array[i][n - 1]
                        cpy[i - 1][n] = array[i][n - 1]
                        if cpy not in lst:
                            lst.append(cpy)
                    elif i + 1 < len(array) and array[i + 1][n] == 0 and 7 > array[i][n - 1] == array[i+1][n-1] > 1:
                        cpy = helper_copy(array)
                        cpy[i][n - 1] = 0
                        cpy[i+1][n - 1] = 0
                        cpy[i][n] = array[i][n - 1]
                        cpy[i + 1][n] = array[i][n - 1]
                        if cpy not in lst:
                            lst.append(cpy)
                    if array[i][n - 1] == 1:
                        assert(n - 2 >= 0)
                        if i-1 >= 0 and array[i - 1][n] == 0 and array[i - 1][n -1] == 1: 
                            cpy = helper_copy(array)
                            cpy[i][n - 2] = 0
                            cpy[i-1][n-2] = 0
                            cpy[i][n] = 1
                            cpy[i - 1][n] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                        elif i + 1 < len(array) and array[i + 1][n] == 0 and array[i+1][n-1] == 1:
                            cpy = helper_copy(array)
                            cpy[i][n - 2] = 0
                            cpy[i+1][n-2] = 0
                            cpy[i][n] = 1
                            cpy[i + 1][n] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                if n + 1 < len(array[i]):
                    if array[i][n + 1] == 7:
                        cpy = helper_copy(array)
                        cpy[i][n + 1] = 0
                        cpy[i][n] = 7
                        if cpy not in lst:
                            lst.append(cpy)
                    if n + 2 < len(array[i]) and 7 > array[i][n + 1] == array[i][n + 2] > 1:
                        assert(n + 2 < len(array[i]))
                        cpy = helper_copy(array)
                        cpy[i][n + 2] = 0
                        cpy[i][n] = array[i][n + 1]
                        if cpy not in lst:
                            lst.append(cpy)
                    if i-1 >= 0 and array[i - 1][n] == 0 and 7 > array[i][n + 1] == array[i - 1][n + 1] > 1: 
                        cpy = helper_copy(array)
                        cpy[i][n + 1] = 0
                        cpy[i-1][n+1] = 0
                        cpy[i][n] = array[i][n + 1]
                        cpy[i - 1][n] = array[i][n + 1]
                        if cpy not in lst:
                            lst.append(cpy)
                    if i + 1 < len(array) and array[i + 1][n] == 0 and 7 > array[i+1][n+1] == array[i][n + 1] > 1:
                        cpy = helper_copy(array)
                        cpy[i][n + 1] = 0
                        cpy[i+1][n + 1] = 0
                        cpy[i][n] = array[i][n + 1]
                        cpy[i + 1][n] = array[i][n + 1]
                        if cpy not in lst:
                            lst.append(cpy)
                    if array[i][n + 1] == 1:
                        assert(n + 2 < len(array[i]))
                        if i-1 >= 0 and array[i - 1][n] == 0 and array[i - 1][n + 1] == 1: 
                            cpy = helper_copy(array)
                            cpy[i][n + 2] = 0
                            cpy[i-1][n+2] = 0
                            cpy[i][n] = 1
                            cpy[i - 1][n] = 1
                            if cpy not in lst:
                                lst.append(cpy)
                        elif i + 1 < len(array) and array[i + 1][n] == 0 and array[i+1][n+1] == 1:
                            cpy = helper_copy(array)
                            cpy[i][n + 2] = 0
                            cpy[i+1][n+2] = 0
                            cpy[i][n] = 1
                            cpy[i + 1][n] = 1
                            if cpy not in lst:
                                lst.append(cpy)

    return lst
 
def get_cost(solution):
    return len(solution) - 1

def get_heuristic(state):
    for i in range(len(state)):
        for n in range(len(state[i])):
            if state[i][n] == 1:
                # print(state)
                assert(state[i][n+1] == state[i+1][n+1] == state[i+1][n] == 1)
                dist = abs(i - 3) + abs(n - 1)
                return dist

def original_heuristic(state):
    ones = []
    zeros = []
    for i in range(len(state)):
        for n in range(len(state[i])):
            if state[i][n] == 1:
                if ones == []:
                    dist = abs(i - 3) + abs(n - 1)
                ones.append((i,n))
            elif state[i][n] == 0:
                zeros.append((i,n))
    min_dist = 99
    for k in ones:
        for j in zeros:
            d = abs(k[0] - j[0]) + abs(k[1] - j[1])
            if d < min_dist:
                min_dist = d
    
    return dist + min_dist - 1
                

def tuplify(lst):
    
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = tuplify(lst[i])
    tup = tuple(lst)
    return tup
        

def a_star(initial_state):
    
    frontier = []
    start = (get_heuristic(initial_state), initial_state)
    hq.heappush(frontier, start)
    came_from = {}
    came_from[tuplify(initial_state)] = None
    cost = 0
    while frontier != []:
        curr = hq.heappop(frontier)
        if is_goal_state(curr[1]):
            break
        cost += 1
        for state in successors(curr[1]):
            tup_state =  tuplify(state)
            if tup_state not in came_from:
                next = (get_heuristic(state) + cost, state)
                hq.heappush(frontier, next)
                came_from[tup_state] = curr[1]
    
    if is_goal_state(curr[1]):
        current = curr[1]
        path = []
        while current != initial_state:
            path.append(current)
            current = came_from[tuplify(current)]
            # print(current)
        path.append(initial_state)
        path.reverse()
        return path

def dfs(initial_state):

    came_from = {}
    came_from[tuplify(initial_state)] = None
    stack = [initial_state]
    
    while stack != []:
        curr = stack.pop()
        if is_goal_state(curr):
            break
       
        for state in successors(curr):
            tup_state =  tuplify(state)
            if tup_state not in came_from:
                stack.append(state)
                came_from[tup_state] = curr
    
    if is_goal_state(curr):
        
        path = []
        while curr != initial_state:
            path.append(curr)
            curr = came_from[tuplify(curr)]
            
        path.append(initial_state)
        path.reverse()
        return path        
    

if __name__ == "__main__":
    array = read(sys.argv[1])
    # print(array)
    
    sol = a_star(array)
    # print(sol)
    sol = edit_grid(sol)

    # print(sol)
    # print(len(sol) - 1)

    sol2 = dfs(array)
    sol2 = edit_grid(sol2)
    # print(sol2)
    # print(len(sol2) - 1)

    f = open(sys.argv[2], "w")

    final = "Cost of the solution: {}\n".format(len(sol2) - 1)
    for state in sol2:
        sta = ""
        for line in state:
            li = ""
            for num in line:
                li = li + str(num)
            sta = sta + li + '\n'
        final = final + sta + '\n'
    f.write(final)

    f.close()

    f = open(sys.argv[3], "w")

    final = "Cost of the solution: {}\n".format(len(sol) - 1)
    for state in sol:
        sta = ""
        for line in state:
            li = ""
            for num in line:
                li = li + str(num)
            sta = sta + li + '\n'
        final = final + sta + '\n'
    f.write(final)

    f.close()

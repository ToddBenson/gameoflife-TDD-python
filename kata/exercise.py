"""
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it. The universe is infinite in both the x and y dimensions
and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array
cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively. You can take advantage of the
htmlize function to get a text representation of the universe: eg:

print htmlize(cells)

"""


def get_generation(cells, generation):
    print(cells)

    lgth = len(cells[0]) + 2
    arr = [0 for x in range(lgth)]
    for y in range(len(cells)):
        arr.extend([0])
        arr.extend([cells[y][x] for x in range(lgth - 2)])
        arr.extend([0])
    arr.extend([0 for x in range(len(cells[0]) + 2)])

    def check_neighbors(arr):
        answer = list([])
        for y in range(lgth + 1, len(arr)):
            neighbor = 0
            if arr[y - lgth + 1] == 1:
                neighbor += 1
            if arr[y - lgth] == 1:
                neighbor += 1
            if arr[y - lgth - 1 ] == 1:
                neighbor += 1
            if arr[y - 1] == 1:
                neighbor += 1
            if y < len(arr) - 1:
                if arr[y + 1] == 1:
                    neighbor += 1
            if y < len(arr) - lgth:
                if arr[y + lgth] == 1:
                    neighbor += 1
            if y < len(arr) - 1 - lgth:
                if arr[y + 1 + lgth] == 1:
                    neighbor += 1
            if y < len(arr) + 1 - lgth:
                if arr[y - 1 + lgth] == 1:
                    neighbor += 1
            answer.extend([neighbor])
        return answer

    def new_state(arr):
        answer = list([])
        for y in range(len(arr)):
            if arr[y] < 2 or arr[y] > 3:
                answer.extend([0])
            if arr[y] == 3:
                answer.extend([1])
            if arr[y] == 2:
                answer.extend([2])
        return answer

    test = check_neighbors(arr)
    print(test)

    test2 = new_state(test)
    print(test2)

    new_test = [test2[x:x + lgth] for x in range(0, len(test2), lgth)]

    print(new_test)

    # another_test = [new_test[list] for list in new_test if new_test[list] == 2 else new_test[list] = cells[list]]
    #
    # print(another_test)

    return cells

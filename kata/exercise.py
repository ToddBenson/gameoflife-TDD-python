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
    def cell_exists(r, c):
        return True if 0 <= r < len(cells) and 0 <= c < len(cells[r]) else False

    def get_active_neighbors(r, c):
        n = 0
        if cell_exists(r - 1, c - 1):
            n += cells[r - 1][c - 1]
        if cell_exists(r - 1, c):
            n += cells[r - 1][c]
        if cell_exists(r - 1, c + 1):
            n += cells[r - 1][c + 1]
        if cell_exists(r, c - 1):
            n += cells[r][c - 1]
        if cell_exists(r, c + 1):
            n += cells[r][c + 1]
        if cell_exists(r + 1, c - 1):
            n += cells[r + 1][c - 1]
        if cell_exists(r + 1, c):
            n += cells[r + 1][c]
        if cell_exists(r + 1, c + 1):
            n += cells[r + 1][c + 1]
        return n

    def set_value(neighbors, current):
        if neighbors == 3:
            return 1
        if neighbors == 2:
            return current
        return 0

    def add_bottom_row(add_bottom_row_array):
        add_bottom_row_array.append(
            [set_value(get_active_neighbors((len(add_bottom_row_array) + 1), cell), 0) for cell in
             range(len(add_bottom_row_array[0]))])
        return add_bottom_row_array

    def clean_up(clean_up_array):
        if sum(clean_up_array[0]) == 0:
            clean_up_array = clean_up_array[1:]
        if sum(clean_up_array[-1]) == 0:
            clean_up_array = clean_up_array[:-1]
        return clean_up_array

    def add_columns(add_column_array):
        n = 0
        for x in add_column_array:
            if x[-1] > 0:
                n += 1
                if n >= 3:
                    add_column_array = [x + [0] for x in add_column_array]
        for x in add_column_array:
            if x[-1] > 0:
                n += 1
                if n >= 3:
                    add_column_array = [x[1:] for x in add_column_array]
        return add_column_array

    def generate(generate_array):
        generate_array = add_bottom_row(generate_array)

        # OFFENDING CODE!
        generate_array = [[set_value(get_active_neighbors(row, cell), generate_array[row][cell])
                           for cell in range(len(generate_array[row]))
                           if cell_exists(row, cell)]
                          for row in range(len(generate_array))]
        return clean_up(generate_array)
    cells = add_columns(cells)
    print(cells)
    return cells if generation < 1 else get_generation(generate(cells), generation - 1)

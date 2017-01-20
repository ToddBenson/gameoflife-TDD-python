def get_generation(current_generation, generation):

    for counter in range(0, generation):

        def cell_exists(r, c):
            return True if 0 <= r < len(current_generation) and 0 <= c < len(current_generation[r]) else False

        def get_active_neighbors(row, column):
            neighbors = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
            return sum([current_generation[row + x[0]][column + x[1]] for x in neighbors if cell_exists(row + x[0], column + x[1])])

        def set_alive_or_dead(alive_neighbors, current_value):
            return 1 if alive_neighbors == 3 else current_value if alive_neighbors == 2 else 0

        def clean_up(array):
            while not any(array[0]): del array[0]
            while not any(array[-1]): del array[-1]
            while not any([row[0] for row in array]): map(lambda x: x.pop(0), array)
            while not any([row[-1] for row in array]): map(lambda x: x.pop(), array)
            return array

        def expand(array):
            array = [[0] + column + [0] for column in array]
            array.append([0 for column in range(len(array[0]))])
            array.insert(0, [0 for column in range(len(array[0]))])
            return array

        def create_next_generation(array):
            array = [[set_alive_or_dead(get_active_neighbors(row, column), array[row][column])
                      for column in range(len(array[row]))
                      if cell_exists(row, column)]
                     for row in range(len(array))]
            return clean_up(array)

        current_generation = expand(current_generation)
        current_generation = create_next_generation(current_generation)

    return current_generation

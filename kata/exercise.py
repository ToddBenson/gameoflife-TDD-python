def cell_exists(row, column, array):
    return True if 0 <= row < len(array) and 0 <= column < len(array[row]) else False


def get_number_of_active_neighbors(row, column, array):
    neighbors = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
    return sum([array[row + offset[0]][column + offset[1]] for offset in neighbors if
                cell_exists(row + offset[0], column + offset[1], array)])


def set_cell_status(alive_neighbors, current_value):
    return 1 if alive_neighbors == 3 else current_value if alive_neighbors == 2 else 0


def remove_empty_boarders(array):
    while not any(array[0]): del array[0]
    while not any(array[-1]): del array[-1]
    while not any([row[0] for row in array]): map(lambda x: x.pop(0), array)
    while not any([row[-1] for row in array]): map(lambda x: x.pop(), array)
    return array


def add_empty_boarders(array):
    expanded_array = [[0] + column + [0] for column in array]
    expanded_array.append([0 for column in range(len(expanded_array[0]))])
    expanded_array.insert(0, [0 for column in range(len(expanded_array[0]))])
    return expanded_array


def create_next_generation(array):
    next_generation = [[set_cell_status(get_number_of_active_neighbors(row, column, array), array[row][column])
                       for column in range(len(array[row]))
                       if cell_exists(row, column, array)]
                       for row in range(len(array))]
    return next_generation


def get_generation(cells, generation):
    current_generation = remove_empty_boarders(create_next_generation(add_empty_boarders(cells)))
    return current_generation if generation <= 1 else get_generation(current_generation, generation - 1)

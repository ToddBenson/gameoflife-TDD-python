def cell_exists(r, c, array):
    return True if 0 <= r < len(array) and 0 <= c < len(array[r]) else False


def get_number_of_active_neighbors(row, column, array):
    neighbors = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
    return sum([array[row + x[0]][column + x[1]] for x in neighbors if
                cell_exists(row + x[0], column + x[1], array)])


def set_cell_status(alive_neighbors, current_value):
    return 1 if alive_neighbors == 3 else current_value if alive_neighbors == 2 else 0


def print_generation(array):
    for row in array:
        print(row)


def remove_empty_boarders(array):
    while not any(array[0]): del array[0]
    while not any(array[-1]): del array[-1]
    while not any([row[0] for row in array]): map(lambda x: x.pop(0), array)
    while not any([row[-1] for row in array]): map(lambda x: x.pop(), array)
    return array


def add_empty_boarders(array):
    array = [[0] + column + [0] for column in array]
    array.append([0 for column in range(len(array[0]))])
    array.insert(0, [0 for column in range(len(array[0]))])
    return array


def create_next_generation(array):
    array = [[set_cell_status(get_number_of_active_neighbors(row, column, array), array[row][column])
              for column in range(len(array[row]))
              if cell_exists(row, column, array)]
             for row in range(len(array))]
    return array


def get_generation(current_generation, generation):
    current_generation = add_empty_boarders(current_generation)
    current_generation = create_next_generation(current_generation)
    current_generation = remove_empty_boarders(current_generation)
    # print_generation(current_generation)

    return current_generation if generation <= 1 else get_generation(current_generation, generation - 1)

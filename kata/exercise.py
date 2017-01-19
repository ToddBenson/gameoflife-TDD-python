def get_generation(cells, generation):
    def cell_exists(r, c):
        return True if 0 <= r < len(cells) and 0 <= c < len(cells[r]) else False

    def get_active_neighbors(r, c):
        neighbors = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
        n = 0
        for x in neighbors:
            if cell_exists(r + x[0], c + x[1]):
                n += cells[r + x[0]][c + x[1]]
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
        if sum([x[0] for x in clean_up_array]) == 0:
            clean_up_array = [x[1:] for x in clean_up_array]
        return clean_up_array

    def add_columns(add_column_array):
        if sum([x[-1] for x in add_column_array]) >= 3 and generation > 0:
            add_column_array = [x + [0] for x in add_column_array]
        return add_column_array

    def generate(generate_array):
        generate_array = add_bottom_row(generate_array)
        generate_array = [[set_value(get_active_neighbors(row, cell), generate_array[row][cell])
                           for cell in range(len(generate_array[row]))
                           if cell_exists(row, cell)]
                          for row in range(len(generate_array))]
        return clean_up(generate_array)

    cells = add_columns(cells)
    cells = clean_up(cells)
    print("")
    print(cells)
    return cells if generation < 1 else get_generation(generate(cells), generation - 1)

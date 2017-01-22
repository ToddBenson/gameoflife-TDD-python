def remove_empty_first_row(new_generation):
    return new_generation if sum(new_generation[0]) != 0 else remove_empty_first_row(new_generation[1:])


def remove_empty_last_row(new_generation):
    return new_generation if sum(new_generation[-1]) != 0 else remove_empty_last_row(new_generation[:-1])


def remove_empty_left_column(new_generation):
    return new_generation if sum(map(lambda x: int(x[0]), new_generation)) != 0 else remove_empty_left_column(
        map(lambda x: x[1:], new_generation))


def remove_empty_right_column(new_generation):
    return new_generation if sum(map(lambda x: int(x[-1]), new_generation)) != 0 else remove_empty_right_column(
        map(lambda x: x[:-1], new_generation))


def remove_empty_boarders(new_generation):
    return remove_empty_left_column(
        remove_empty_right_column(remove_empty_last_row(remove_empty_first_row(new_generation))))


def add_empty_boarders(new_generation):
    return add_empty_right_column(add_empty_left_column(add_empty_last_row(add_empty_first_row(new_generation))))


def add_empty_left_column(new_generation):
    return map(lambda x: [0] + x, new_generation)


def add_empty_right_column(new_generation):
    return map(lambda x: x + [0], new_generation)


def add_empty_first_row(new_generation):
    return [[0] * len(new_generation[0])] + new_generation


def add_empty_last_row(new_generation):
    return new_generation + [[0] * len(new_generation[0])]
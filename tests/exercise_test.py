"""test the kata task"""
import game_of_life


def test11():
    assert game_of_life.set_cell_status(1, 1) == 0


def test12():
    assert game_of_life.set_cell_status(2, 1) == 1


def test13():
    assert game_of_life.set_cell_status(3, 0) == 1


def test14():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert game_of_life.get_number_of_active_neighbors(1, 1, start) == 3


def test15():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert game_of_life.get_number_of_active_neighbors(4, 4, start) == 1


def test16():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert game_of_life.cell_exists(5, 5, start) is False


def test17():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert game_of_life.cell_exists(4, 4, start) is True


def test19():
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    end = [[0, 1, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 1, 1]]
    assert game_of_life.add_empty_left_column(start) == end


def test20():
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    end = [[1, 1, 1, 0],
           [1, 1, 1, 0],
           [1, 1, 1, 0]]
    assert game_of_life.add_empty_right_column(start) == end


def test9():
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    end = [[0, 0, 0],
           [1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    assert game_of_life.add_empty_first_row(start) == end


def test10():
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1],
           [0, 0, 0]]
    assert game_of_life.add_empty_last_row(start) == end


def test21():
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [0, 0, 0]]
    assert game_of_life.remove_empty_last_row(start) == end


def test22():
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    start = [[0, 0, 0, ],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    assert game_of_life.remove_empty_first_row(start) == end


def test24():
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    start = [[0, 1, 1, 1],
             [0, 1, 1, 1],
             [0, 1, 1, 1]]
    assert game_of_life.remove_empty_left_column(start) == end


def test25():
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    start = [[1, 1, 1, 0],
             [1, 1, 1, 0],
             [1, 1, 1, 0]]
    assert game_of_life.remove_empty_right_column(start) == end


def test18():
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert game_of_life.remove_empty_boarders(start) == end


def test23():
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    end = [[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0]]
    assert game_of_life.add_empty_boarders(start) == end


def test1():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[0, 1, 0],
           [0, 0, 1],
           [1, 1, 1]]
    assert game_of_life.get_generation(start, 1) == end


def test2():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[1, 0, 1],
           [0, 1, 1],
           [0, 1, 0]]
    assert game_of_life.get_generation(start, 2) == end


def test3():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[0, 0, 1],
           [1, 0, 1],
           [0, 1, 1]]
    assert game_of_life.get_generation(start, 3) == end


def test4():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[1, 0, 0],
           [0, 1, 1],
           [1, 1, 0]]
    assert game_of_life.get_generation(start, 40) == end


def test5():
    start = [[1, 1, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 1, 1, 1]]
    end = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
    assert game_of_life.get_generation(start, 10) == end


def test6():
    start = [[1],
             [1],
             [1]]
    end = [[1, 1, 1]]
    assert game_of_life.get_generation(start, 5) == end


def test7():
    start = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    end = [[1, 1, 1]]
    assert game_of_life.get_generation(start, 911) == end


def test8():
    start = [[1, 1, 1, 1]]
    end = [[0, 1, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 1, 0]]
    assert game_of_life.get_generation(start, 40) == end


def test26():
    start = [[1, 1, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 1, 1, 1]]
    end = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
    assert game_of_life.main([start, 10]) == end

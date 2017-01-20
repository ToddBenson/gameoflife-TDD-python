"""test the kata task"""
from exercise import add_empty_boarders
from exercise import cell_exists
from exercise import get_generation
from exercise import get_number_of_active_neighbors
from exercise import remove_empty_boarders
from exercise import set_cell_status


def test1():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[0, 1, 0],
           [0, 0, 1],
           [1, 1, 1]]
    assert get_generation(start, 1) == end


def test2():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[1, 0, 1],
           [0, 1, 1],
           [0, 1, 0]]
    assert get_generation(start, 2) == end


def test3():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[0, 0, 1],
           [1, 0, 1],
           [0, 1, 1]]
    assert get_generation(start, 3) == end


def test4():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[1, 0, 0],
           [0, 1, 1],
           [1, 1, 0]]
    assert get_generation(start, 40) == end


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
    assert get_generation(start, 10) == end


def test6():
    start = [[1],
             [1],
             [1]]
    end = [[1, 1, 1]]
    assert get_generation(start, 5) == end


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
    assert get_generation(start, 1) == end


def test8():
    start = [[1, 1, 1, 1]]
    end = [[0, 1, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 1, 0]]
    assert get_generation(start, 40) == end


def test9():
    start = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    end = [[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0]]
    assert add_empty_boarders(start) == end


def test10():
    end = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert remove_empty_boarders(start) == end


def test11():
    assert set_cell_status(1, 1) == 0


def test12():
    assert set_cell_status(2, 1) == 1


def test13():
    assert set_cell_status(3, 0) == 1


def test14():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert get_number_of_active_neighbors(1, 1, start) == 3


def test15():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert get_number_of_active_neighbors(4, 4, start) == 1


def test16():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert cell_exists(5, 5, start) is False


def test17():
    start = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    assert cell_exists(4, 4, start) is True

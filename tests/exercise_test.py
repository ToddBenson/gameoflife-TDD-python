
"""test the kata task"""
from exercise import get_generation


def test1():
    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
    end = [[0,1,0],
           [0,0,1],
           [1,1,1]]
    assert get_generation(start, 1) == end


def test2():
    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
    end = [[1,0,1],
           [0,1,1],
           [0,1,0]]
    assert get_generation(start, 2) == end


def test3():
    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
    end = [[0,0,1],
           [1,0,1],
           [0,1,1]]
    assert get_generation(start, 3) == end


def test4():
    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
    end = [[1,0,0],
           [0,1,1],
           [1,1,0],
           [0,0,0],
           [0,0,0],
           [0,0,0],
           [0,0,0]]
    assert get_generation(start, 40) == end
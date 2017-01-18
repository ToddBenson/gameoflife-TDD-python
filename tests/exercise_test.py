
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



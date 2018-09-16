import pytest
from pprint import pprint

from piece import *

# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

def test_canMove_Fail_noMove():
    piece = Bishop(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
        piece.canMove(Pos(0,0))

def test_canMove_move1():
    piece = Bishop(0,0,0)
    assert piece.canMove(Pos(1,1))

def test_canMove_move5():
    piece = Bishop(0,1,2)
    assert piece.canMove(Pos(6,7))

def test_canMove_moveNegativeYPositiveX():
    piece = Bishop(0,3,5)
    assert piece.canMove(Pos(4,4))

def test_canMove_movePositiveYNegativeX():
    piece = Bishop(0,3,5)
    assert piece.canMove(Pos(2,6))

def test_canMove_moveNegativeX():
    piece = Bishop(0,3,4)
    assert piece.canMove(Pos(2,3))

def test_canMove_Fail_straight():
    piece = Bishop(0,0,0)
    assert not piece.canMove(Pos(1,0))

def test_canMove_Fail_straight_3():
    piece = Bishop(0,4,3)
    assert not piece.canMove(Pos(7,3))

def test_canMove_Fail_straightNegativeY():
    piece = Bishop(0,4,3)
    assert not piece.canMove(Pos(4,1))

def test_canMove_Fail_2Forwards1Sideways():
    piece = Bishop(0,4,3)
    assert not piece.canMove(Pos(6,4))

def test_canMove_Fail_random():
    piece = Bishop(0,4,3)
    assert not piece.canMove(Pos(6,8))

def test_canMove_Fail_random2():
    piece = Bishop(0,2,2)
    assert not piece.canMove(Pos(7,4))
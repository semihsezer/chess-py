import pytest
from pprint import pprint

from chess.piece import *

# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

def test_canMove_Fail_move0():
    piece = Rook(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
        piece.canMove(Pos(0,0))

def test_canMove_move1():
    piece = Rook(0,0,0)
    assert piece.canMove(Pos(0,1))

def test_canMove_move5():
    piece = Rook(0,0,0)
    assert piece.canMove(Pos(0,5))

def test_canMove_moveNegativeY():
    piece = Rook(0,0,5)
    assert piece.canMove(Pos(0,3))

def test_canMove_moveX_move1():
    piece = Rook(0,2,2)
    assert piece.canMove(Pos(3,2))

def test_canMove_moveX_move2():
    piece = Rook(0,5,4)
    assert piece.canMove(Pos(7,4))

def test_canMove_moveX_move5():
    piece = Rook(0,2,1)
    assert piece.canMove(Pos(7,1))

def test_canMove_moveNegativeX():
    piece = Rook(0,5,6)
    assert piece.canMove(Pos(4,6))

def test_canMove_Fail_crossways():
    piece = Rook(0,0,0)
    assert not piece.canMove(Pos(1,1))

def test_canMove_Fail_crossways():
    piece = Rook(0,5,3)
    assert not piece.canMove(Pos(6,4))

def test_canMove_Fail_crosswaysNegative():
    piece = Rook(0,4,3)
    assert not piece.canMove(Pos(3,2))

def test_canMove_Fail_random():
    piece = Rook(0,4,3)
    assert not piece.canMove(Pos(6,1))

def test_canMove_Fail_random2():
    piece = Rook(0,2,2)
    assert not piece.canMove(Pos(7,4))

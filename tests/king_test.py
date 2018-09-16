import pytest
from pprint import pprint

from chess.piece import *

# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

def test_canMove_Fail_move0():
    piece = King(0,2,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
        piece.canMove(Pos(2,0))

def test_canMove_move1():
    piece = King(0,0,0)
    assert piece.canMove(Pos(1,1))

def test_canMove_moveNegativeYPositiveX():
    piece = King(0,3,5)
    assert piece.canMove(Pos(4,4))

def test_canMove_movePositiveYNegativeX():
    piece = King(0,3,5)
    assert piece.canMove(Pos(2,6))

def test_canMove_moveNegativeX():
    piece = King(0,3,4)
    assert piece.canMove(Pos(2,3))

# Rook
def test_canMove_move1():
    piece = King(0,0,0)
    assert piece.canMove(Pos(0,1))

def test_canMove_moveNegativeY():
    piece = King(0,0,5)
    assert piece.canMove(Pos(0,4))

def test_canMove_moveX_move1():
    piece = King(0,2,2)
    assert piece.canMove(Pos(3,2))

def test_canMove_LikeRook_moveNegativeX():
    piece = King(0,5,6)
    assert piece.canMove(Pos(4,6))

# Fails
def test_canMove_Fail_LikeRook_move5():
    piece = King(0,0,0)
    assert not piece.canMove(Pos(0,5))

def test_canMove_Fail_move2X():
    piece = King(0,1,2)
    assert not piece.canMove(Pos(3,2))

def test_canMove_Fail_move2XNegative():
    piece = King(0,3,2)
    assert not piece.canMove(Pos(1,2))

def test_canMove_Fail_move2Y():
    piece = King(0,1,2)
    assert not piece.canMove(Pos(1,4))

def test_canMove_Fail_move2YNegative():
    piece = King(0,3,2)
    assert not piece.canMove(Pos(3,0))

def test_canMove_Fail_move5():
    piece = King(0,1,2)
    assert not piece.canMove(Pos(6,7))

def test_canMove_Fail_LikeRook_moveNegativeY():
    piece = King(0,0,5)
    assert not piece.canMove(Pos(0,3))

def test_canMove_Fail_2Forwards1Left():
    piece = King(0,6,0)
    assert not piece.canMove(Pos(5,2))

def test_canMove_Fail_1Backward2Right():
    piece = King(0,3,7)
    assert not piece.canMove(Pos(5,6))

def test_canMove_Fail_random():
    piece = King(0,4,3)
    assert not piece.canMove(Pos(6,7))

def test_canMove_Fail_random2():
    piece = King(0,2,2)
    assert not piece.canMove(Pos(7,4))
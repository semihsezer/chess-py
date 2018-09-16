import pytest
from pprint import pprint

from piece import *

# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

# From Rook
def test_canMove_Fail_move0():
    piece = Queen(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
        piece.canMove(Pos(0,0))

def test_canMove_LikeRook_move1():
    piece = Queen(0,0,0)
    assert piece.canMove(Pos(0,1))

def test_canMove_LikeRook_move5():
    piece = Queen(0,0,0)
    assert piece.canMove(Pos(0,5))

def test_canMove_LikeRook_moveNegativeY():
    piece = Queen(0,0,5)
    assert piece.canMove(Pos(0,3))

def test_canMove_LikeRook_moveX_move1():
    piece = Queen(0,2,2)
    assert piece.canMove(Pos(3,2))

def test_canMove_LikeRook_moveX_move2():
    piece = Queen(0,5,4)
    assert piece.canMove(Pos(7,4))

def test_canMove_LikeRook_moveX_move5():
    piece = Queen(0,2,1)
    assert piece.canMove(Pos(7,1))

def test_canMove_LikeRook_moveNegativeX():
    piece = Queen(0,5,6)
    assert piece.canMove(Pos(4,6))

# From Bishop
def test_canMove_LikeBishop_move1():
    piece = Queen(0,0,0)
    assert piece.canMove(Pos(1,1))

def test_canMove_LikeBishop_move5():
    piece = Queen(0,1,2)
    assert piece.canMove(Pos(6,7))

def test_canMove__LikeBishopmoveNegativeYPositiveX():
    piece = Queen(0,3,5)
    assert piece.canMove(Pos(4,4))

def test_canMove__LikeBishopmovePositiveYNegativeX():
    piece = Queen(0,3,5)
    assert piece.canMove(Pos(2,6))

def test_canMove__LikeBishopmoveNegative():
    piece = Queen(0,3,4)
    assert piece.canMove(Pos(2,3))

# Fails:
def test_canMove_Fail_random():
    piece = Bishop(0,4,3)
    assert not piece.canMove(Pos(6,7))

def test_canMove_Fail_random2():
    piece = Bishop(0,2,2)
    assert not piece.canMove(Pos(7,4))

def test_canMove_Fail_2Forwards1Sideways():
    piece = Bishop(0,4,3)
    assert not piece.canMove(Pos(6,4))
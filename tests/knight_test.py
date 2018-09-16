import pytest
from pprint import pprint

from chess.piece import *

# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

def test_canMove_Fail_samePosition():
    piece = Knight(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
        piece.canMove(Pos(0,0))

def test_canMove_2Forwards1Right():
    piece = Knight(0,2,0)
    assert piece.canMove(Pos(3,2))

def test_canMove_2Forwards1Left():
    piece = Knight(0,6,0)
    assert piece.canMove(Pos(5,2))

def test_canMove_1Forward2Left():
    piece = Knight(0,2,5)
    assert piece.canMove(Pos(0,6))

def test_canMove_1Forward2Right():
    piece = Knight(0,4,6)
    assert piece.canMove(Pos(6,7))

def test_canMove_2Backwards1Right():
    piece = Knight(0,4,6)
    assert piece.canMove(Pos(5,4))

def test_canMove_2Backwards1Left():
    piece = Knight(0,3,6)
    assert piece.canMove(Pos(2,4))

def test_canMove_1Backward2Right():
    piece = Knight(0,3,7)
    assert piece.canMove(Pos(5,6))

def test_canMove_1Backward2Left():
    piece = Knight(0,6,6)
    assert piece.canMove(Pos(4,5))

def test_canMove_Fail_1Forward():
    piece = Knight(0,0,0)
    assert not piece.canMove(Pos(0,1))

def test_canMove_Fail_2Forward():
    piece = Knight(0,1,2)
    assert not piece.canMove(Pos(1,4))

def test_canMove_Fail_3Forward():
    piece = Knight(0,1,2)
    assert not piece.canMove(Pos(1,5))

def test_canMove_Fail_1Right():
    piece = Knight(0,3,5)
    assert not piece.canMove(Pos(4,5))

def test_canMove_Fail_3Left():
    piece = Knight(0,4,5)
    assert not piece.canMove(Pos(1,5))

def test_canMove_Fail_1Backward():
    piece = Knight(0,5,5)
    assert not piece.canMove(Pos(5,4))

def test_canMove_Fail_5Forward():
    piece = Knight(0,4,2)
    assert not piece.canMove(Pos(4,7))

def test_canMove_Fail_2Right():
    piece = Knight(0,1,3)
    assert not piece.canMove(Pos(3,3))

def test_canMove_Fail_2Left():
    piece = Knight(0,4,2)
    assert not piece.canMove(Pos(2,2))

def test_canMove_Fail_1crosswaysPositiveY():
    piece = Knight(0,1,1)
    assert not piece.canMove(Pos(2,2))

def test_canMove_Fail_3crosswaysNegativeY():
    piece = Knight(0,4,6)
    assert not piece.canMove(Pos(3,5))

# getTrajectoryTo
def test_getTrajectoryTo_noMove():
    piece = Knight(0,4,6)
    with pytest.raises(piece.CantMoveToSamePositionException):
        result = piece.getTrajectoryTo(Pos(4,6))

def test_getTrajectoryTo_InvalidMove():
    piece = Knight(0,4,6)
    expected = []
    result = piece.getTrajectoryTo(Pos(4,7))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

def test_getTrajectoryTo_1Forward2Right():
    piece = Knight(0,4,6)
    expected = [Pos(6,7)]
    result = piece.getTrajectoryTo(Pos(6,7))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

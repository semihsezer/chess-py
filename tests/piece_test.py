import pytest
from pprint import pprint

from chess.piece import *


# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

def test_createPiece():
    piece = Rook(0,0,0)
    assert piece.player_id == 0
    assert piece.x == 0
    assert piece.y == 0

def test_canMove_Fail_SamePosition():
    piece = Rook(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
    	piece.canMove(Pos(0,0))

def test_canKill_Fail_SamePosition():
    piece = Rook(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
	    piece.canKill(Pos(0,0))
    
def test_move():
    piece = Rook(0,0,0)
    piece.move(Pos(2,2))
    assert piece.x == 2
    assert piece.y == 2

def test_getTrajectoryTo_MoveOne():
    piece = Rook(0,0,0)
    expected = [Pos(0,1)]
    result = piece.getTrajectoryTo(Pos(0,1))
    
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])
    
def test_getTrajectoryTo_NoMove():
    piece = Rook(0,0,0)
    with pytest.raises(piece.CantMoveToSamePositionException):
        result = piece.getTrajectoryTo(Pos(0,0))

def test_getTrajectoryTo_InvalidMove():
    piece = Rook(0,0,0)
    expected = []
    result = piece.getTrajectoryTo(Pos(4,6))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

def test_getTrajectoryTo_MoveTwo():
    piece = Rook(0,0,0)
    expected = [Pos(0,1), Pos(0,2)]
    result = piece.getTrajectoryTo(Pos(0,2))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

def test_getTrajectoryTo_MoveNegativeY():
    piece = Rook(0,3,5)
    expected = [Pos(3,4), Pos(3,3), Pos(3,2)]
    result = piece.getTrajectoryTo(Pos(0,2))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

def test_getTrajectoryTo_MoveX():
    piece = Rook(0,0,0)
    expected = [Pos(0,1), Pos(0,2), Pos(0,3), Pos(0,4)]
    result = piece.getTrajectoryTo(Pos(0,4))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

def test_getTrajectoryTo_MoveNegativeX():
    piece = Rook(0,5,1)
    expected = [Pos(4,1), Pos(3,1), Pos(2,1)]
    result = piece.getTrajectoryTo(Pos(2,1))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])


def test_getTrajectoryTo_MoveCrossDirection():
    piece = Rook(0,3,4)
    expected = [Pos(4,5), Pos(5,6), Pos(6,7)]
    result = piece.getTrajectoryTo(Pos(3,3))
    assert all([ posEquals(p1,p2) for p1, p2 in zip(expected, result)])

def test_getTrajectoryTo_MoveCrossDirectionNegativeY():
    piece = Rook(0,5,8)
    expected = [Pos(4,7), Pos(3,6), Pos(2,5)]
    result = piece.getTrajectoryTo(Pos(2,5))




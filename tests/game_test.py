import pytest
from pprint import pprint

from chess.piece import *
from chess.player import *
from chess.game import *

# returns true if two positions are the same
def posEquals(p1, p2):
    return p1.x==p2.x and p1.y==p2.y

#           0    1    2    3    4    5    6    7
#Board = [['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R']  0
#         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']  1
#         ['0', '0', '0', '0', '0', '0', '0', '0']  2
#         ['0', '0', '0', '0', '0', '0', '0', '0']  3
#         ['0', '0', '0', '0', '0', '0', '0', '0']  4
#         ['0', '0', '0', '0', '0', '0', '0', '0']  5
#         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']  6
#         ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R']  7
#        ]


def test_createGame():
    game = Game()

    # check for board length
    assert len(game.board) == 8

    for i in range(0, 8):
        assert len(game.board[i]) == 8
    
    # check y=0 && y=1 has black's pieces && y==7 && y==6 has white's pieces and the rest is empty
    for x in range(0,8):
        for y in range(0,8):
            if (y == 0 or y == 1):
                assert game.board[y][x].player_id == 0 # black
            elif (y==6 or y ==7):
                assert game.board[y][x].player_id == 1 # white
            else:
                assert game.board[y][x] == None # empty

    # check pawns
    for x in range(0,8):
        assert game.board[1][x]._symbol == "P"
        assert game.board[6][x]._symbol == "P"

    # check rooks
    assert game.board[0][0]._symbol == "R"
    assert game.board[0][7]._symbol == "R"
    assert game.board[7][0]._symbol == "R"
    assert game.board[7][7]._symbol == "R"

    # check Knights
    assert game.board[0][1]._symbol == "H"
    assert game.board[0][6]._symbol == "H"
    assert game.board[7][1]._symbol == "H"
    assert game.board[7][6]._symbol == "H"

    # check Bishops
    assert game.board[0][2]._symbol == "B"
    assert game.board[0][5]._symbol == "B"
    assert game.board[7][2]._symbol == "B"
    assert game.board[7][5]._symbol == "B"

    # check Queens
    assert game.board[0][3]._symbol == "Q"
    assert game.board[7][3]._symbol == "Q"

    # check Kings
    assert game.board[0][4]._symbol == "K"
    assert game.board[7][4]._symbol == "K"

    assert game.currentPlayer == Player.WHITE

def test_makeMove_Opening_White_Pawn_e2_e3():
    game = Game()

    game.move(Player.WHITE, Pos(4, 6), Pos(4, 5))

    assert game.board[5][4] != None and game.board[5][4]._symbol == "P" and game.board[5][4].player_id == 1
    assert game.board[6][4] == None
    assert game.currentPlayer == 0
    assert game.gameOver == False

def test_makeMove_Opening_White_Pawn_e2_e4():
    game = Game()

    game.move(Player.WHITE, Pos(4, 6), Pos(4, 4))

    game.printBoard()
    assert game.board[4][4] != None and game.board[4][4]._symbol == "P" and game.board[4][4].player_id == 1
    assert game.board[6][4] == None
    assert game.currentPlayer == 0
    assert game.gameOver == False

def test_makeMove_wrongPlayer():
    game = Game()

    with pytest.raises(OtherPlayersTurnException):
        game.move(Player.BLACK, Pos(4, 1), Pos(4, 3)) # black tries to start the game
    
    game.move(Player.WHITE, Pos(4, 6), Pos(4, 4)) # white's first move

    with pytest.raises(OtherPlayersTurnException):
        game.move(Player.WHITE, Pos(5, 6), Pos(5, 4)) # white's tries to play again

    game.move(Player.BLACK, Pos(4, 1), Pos(4, 3)) # black's move

def test_makeMove_gameOver():
    game = Game()
    game.gameOver = True
    
    with pytest.raises(GameOverException):
        game.move(Player.WHITE, Pos(4, 6), Pos(4, 4)) # white move

    with pytest.raises(GameOverException):
        game.move(Player.BLACK, Pos(4, 1), Pos(4, 3)) # black move

def test_makeMove_moveFromEmptySpot():
    game = Game()

    with pytest.raises(NoPieceInPositionException):
        game.move(Player.WHITE, Pos(4, 5), Pos(4, 4))

def test_makeMove_otherPlayersPiece():
    game = Game()

    with pytest.raises(OtherPlayersPieceException):
        game.move(Player.WHITE, Pos(4, 1), Pos(4, 3)) # white tries to move black's pawn

    game.currentPlayer = 0

    with pytest.raises(OtherPlayersPieceException):
        game.move(Player.BLACK, Pos(5, 6), Pos(5, 4)) # black tries to move white's pawn


def test_makeMove():
    # TODO:
    return False

def test_isValidMove():
    # TODO:
    return False

def test_isValidEnPassantMove():
    # TODO:
    return False

def test_isValidRokMove():
    # TODO:
    return False

def test_movePiece():
    # TODO:
    return False

def test_movePieceRok():
    # TODO:
    return False

def test_movePieceEnPassant():
    # TODO:
    return False

def test_isPosUnderAttackBy():
    # TODO:
    return False

def test_getAllValidNextGames():
    # TODO:
    return False

def test_getPieces():
    # TODO:
    return False

def test_isGameOver():
    # TODO:
    return False

def test_getOtherPlayer():
    # TODO:
    return False


















#with pytest.raises(piece.CantMoveToSamePositionException):
#        piece.canMove(Pos(0,0))






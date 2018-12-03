import pytest
from pprint import pprint

from chess.piece import *
from chess.player import *
from chess.game import *

# Feed a sequence of moves
    # check validity
    # check all possible moves
# Paste this game to https://www.chess.com/analysis-board-editor

#1. e4 e5 2. d3 Nc6 3. Nf3 Nf6 4. Bg5 Be7 5. Nc3 Nd4 6. Nxd4 exd4 7. Nd5 Nxd5 8. exd5 Bb4+ 9. c3 dxc3 10. bxc3 Bxc3+ 11. Ke2 Bxa1 12. Bxd8 Kxd8 13. Qxa1 f6 14. Qc3 Re8+ 15. Kd2 c6 16. dxc6 dxc6 17. d4 Bf5 18. d5 Kc7 19. Bd3 Rad8 20. dxc6 bxc6 21. a4 Bxd3 22. a5 Bf5+ 23. Qd3 Rxd3+ 24. Kc2 Re2+ 25. Kc1 Re1+ 26. Rxe1 Kb7 27. Kc2 Rd5+ 28. Re4 Bxe4+ 29. Kc3 Rd3+ 30. Kc4 Bxg2 31. Kxd3 Bf1+ 32. Kc3 g5 33. a6+ Kxa6 34. Kb4
game = Game()

def test_move_1():
    #1.
    game.move(Player.WHITE, "e2", "e4")
    game.move(Player.BLACK, "e7", "e5")

def test_move_2():
    #2. d3 Nc6
    game.move(Player.WHITE, "d2", "d3")
    game.move(Player.BLACK, "b8", "c6")

def test_move_3():
    #3. Nf3 Nf6
    game.move(Player.WHITE, "g1", "f3")
    game.move(Player.BLACK, "g8", "f6")

def test_move_4():
    #4. Bg5 Be7
    game.move(Player.WHITE, "c1", "g5")
    game.move(Player.BLACK, "f8", "e7")

def test_move_5():
    #5. Nc3 Nd4
    game.move(Player.WHITE, "b1", "c3")
    game.move(Player.BLACK, "c6", "d4")

def test_move_6():
    #6. Nxd4 exd4
    game.move(Player.WHITE, "f3", "d4")
    game.move(Player.BLACK, "e5", "d4")

def test_move_7():
    #7. Nd5 Nxd5
    game.move(Player.WHITE, "c3", "d5")
    game.move(Player.BLACK, "f6", "d5")

def test_move_8():
    #8. exd5 Bb4+
    game.move(Player.WHITE, "e4", "d5")
    game.move(Player.BLACK, "e7", "b4")

def test_move_9():
    #9. c3 dxc3
    game.move(Player.WHITE, "c2", "c3")
    
    with pytest.raises(PathNotClearException):
        # try to kill king with nonexistent bishop
        game.move(Player.BLACK, "b4", "e1")
    with pytest.raises(Piece.InvalidMoveException):
        # try to kill king with queen via physically impossible jump
        game.move(Player.BLACK, "d8", "e1")

    game.move(Player.BLACK, "d4", "c3")

def test_move_10():
    #10. bxc3 Bxc3+
    game.move(Player.WHITE, "b2", "c3")
    game.move(Player.BLACK, "b4", "c3") # check

    with pytest.raises(KingUnderAttackException):
        # e1 d2 doesn't save the king, king is still under attack by the bishop
        game.move(Player.WHITE, "e1", "d2")
    # ensure the king did not move
    assert game.getPieceAt("e1")._symbol == "K" and game.getPieceAt("e1").player_id == Player.WHITE
    # ensure d2 is still empty
    assert game.getPieceAt("d2") == None

    with pytest.raises(KingUnderAttackException):
        # d1 e2, attempts check but his own check is under attack
        game.move(Player.WHITE, "d1", "e2")
    assert game.getPieceAt("d1")._symbol == "Q" and game.getPieceAt("d1").player_id == Player.WHITE
    assert game.getPieceAt("e2") == None
    
    with pytest.raises(KingUnderAttackException):
        # g5 d8, attempts to kill queen with bishop, but king still under attack
        game.move(Player.WHITE, "g5", "d8")
    assert game.getPieceAt("g5")._symbol == "B" and game.getPieceAt("g5").player_id == Player.WHITE
    assert game.getPieceAt("d8")._symbol == "Q" and game.getPieceAt("d8").player_id == Player.BLACK

    with pytest.raises(PathNotClearException):
        # attempt a move with rook where trajectory is blocked
        game.move(Player.WHITE, "h1", "h8")
    assert game.getPieceAt("h1")._symbol == "R" and game.getPieceAt("h1").player_id == Player.WHITE
    assert game.getPieceAt("h8")._symbol == "R" and game.getPieceAt("h8").player_id == Player.BLACK

    with pytest.raises(PathNotClearException):
        # attempt a move with queen that results in check but trajectory is blocked
        game.move(Player.WHITE, "d1", "d7")
    assert game.getPieceAt("d1")._symbol == "Q" and game.getPieceAt("d1").player_id == Player.WHITE
    assert game.getPieceAt("d7")._symbol == "P" and game.getPieceAt("d7").player_id == Player.BLACK


def test_move_11():
    #11. Ke2 Bxa1
    game.move(Player.WHITE, "e1", "e2")
    
    with pytest.raises(NoPieceInPositionException):
        # try to kill king with nonexistent bishop
        game.move(Player.BLACK, "b4", "e1")

    game.move(Player.BLACK, "c3", "a1")

def test_move_12():
    #12. Bxd8 Kxd8
    game.move(Player.WHITE, "g5", "d8")
    game.move(Player.BLACK, "e8", "d8")

def test_move_13():
    #13. Qxa1 f6
    game.move(Player.WHITE, "d1", "a1")
    game.move(Player.BLACK, "f7", "f6")

def test_move_14():
    #14. Qc3 Re8+
    game.move(Player.WHITE, "a1", "c3")
    game.move(Player.BLACK, "h8", "e8") # check

def test_move_15():
    #15. Kd2 c6
    game.move(Player.WHITE, "e2", "d2")
    game.move(Player.BLACK, "c7", "c6")

def test_move_16():
    #16. dxc6 dxc6
    game.move(Player.WHITE, "d5", "c6")
    game.move(Player.BLACK, "d7", "c6")

def test_move_17():
    #17. d4 Bf5
    game.move(Player.WHITE, "d3", "d4")
    game.move(Player.BLACK, "c8", "f5")

def test_move_18():
    #18. d5 Kc7
    game.move(Player.WHITE, "d4", "d5")
    game.move(Player.BLACK, "d8", "c7")

def test_move_19():
    #19. Bd3 Rad8
    game.move(Player.WHITE, "f1", "d3")
    with pytest.raises(KingUnderAttackException):
        # black shouldn't be able to do c6c5 with the pawn, king exposed
        game.move(Player.BLACK, "c6", "d5")
    game.move(Player.BLACK, "a8", "d8")

def test_move_20():
    #20. dxc6 bxc6
    game.move(Player.WHITE, "d5", "c6")
    game.move(Player.BLACK, "b7", "c6")

def test_move_21():
    #21. a4 Bxd3
    with pytest.raises(KingUnderAttackException):
        # white shouldn't be able to do d3f5 with the bishop, king exposed
        game.move(Player.WHITE, "d3", "f5")
    game.move(Player.WHITE, "a2", "a4")
    game.move(Player.BLACK, "f5", "d3")

def test_move_22():
    #22. a5 Bf5+
    with pytest.raises(KingUnderAttackException):
        # white shouldn't be able to kill protected piece with king
        game.move(Player.WHITE, "d2", "d3")
    game.move(Player.WHITE, "a4", "a5")
    game.move(Player.BLACK, "d3", "f5") # this is an indirect check

def test_move_23():
    #23. Qd3 Rxd3+
    with pytest.raises(KingUnderAttackException):
        # white is under check, shouldn't be able to move anyone else
        game.move(Player.WHITE, "a5", "a6")
    with pytest.raises(KingUnderAttackException):
        # white is under check, shouldn't be able to check with the queen
        game.move(Player.WHITE, "c3", "c6")
    with pytest.raises(KingUnderAttackException):
        # white is under check, but c2 is under attack by Bishop
        game.move(Player.WHITE, "d2", "c2")
    with pytest.raises(KingUnderAttackException):
        # white is under check, but e2 is under attack by Rook
        game.move(Player.WHITE, "d2", "e2")
    with pytest.raises(KingUnderAttackException):
        # white is under check, moving the Rook doesn't protect it
        game.move(Player.WHITE, "h1", "d1")
    game.move(Player.WHITE, "c3", "d3")
    game.move(Player.BLACK, "d8", "d3") # check

def test_move_24():
    #24. Kc2 Re2+
    with pytest.raises(KingUnderAttackException):
        # white King can't kill protected rook
        game.move(Player.WHITE, "d2", "d3")
    with pytest.raises(KingUnderAttackException):
        # white King under attack, e2 attacked by Rook
        game.move(Player.WHITE, "d2", "e2")    
    game.move(Player.WHITE, "d2", "c2")
    game.move(Player.BLACK, "e8", "e2") # check

def test_move_25():
    #25. Kc1 Re1+
    game.move(Player.WHITE, "c2", "c1")
    game.move(Player.BLACK, "e2", "e1") # check

def test_move_26():
    #26. Rxe1 Kb7
    game.move(Player.WHITE, "h1", "e1")
    game.move(Player.BLACK, "c7", "b7")

def test_move_27():
    #27. Kc2 Rd5+
    game.move(Player.WHITE, "c1", "c2")
    game.move(Player.BLACK, "d3", "d5") # check

def test_move_28():
    #28. Re4 Bxe4+
    with pytest.raises(KingUnderAttackException):
        # white King under attack, shouldn't be able to check
        game.move(Player.WHITE, "e1", "b1")
    game.move(Player.WHITE, "e1", "e4")
    game.move(Player.BLACK, "f5", "e4") # check

def test_move_29():
    #29. Kc3 Rd3+
    game.move(Player.WHITE, "c2", "c3")
    game.move(Player.BLACK, "d5", "d3") # check

def test_move_30():
    #30. Kc4 Bxg2
    with pytest.raises(KingUnderAttackException):
        # white King under attack, shouldn't be able to check
        game.move(Player.WHITE, "a5", "a6")
    game.move(Player.WHITE, "c3", "c4")
    game.move(Player.BLACK, "e4", "g2")

def test_move_31():
    #31. Kxd3 Bf1+
    game.move(Player.WHITE, "c4", "d3")
    game.move(Player.BLACK, "g2", "f1") # check

def test_move_32():
    #32. Kc3 g5
    with pytest.raises(KingUnderAttackException):
        # white King still under attack
        game.move(Player.WHITE, "d3", "c4")
    game.move(Player.WHITE, "d3", "c3")
    game.move(Player.BLACK, "g7", "g5")

    #33. a6+ Kxa6
    game.move(Player.WHITE, "a5", "a6") # check
    game.move(Player.BLACK, "b7", "a6")

    #34. Kb4
    game.move(Player.WHITE, "c3", "b4")




















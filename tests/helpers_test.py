import pytest
from pprint import pprint

from chess.piece import *
from chess.player import *
from chess.game import *

def test_mapPos():
    pos = Game.mapPos("a1")
    assert pos.x == 0 and pos.y == 7

    pos = Game.mapPos("e2")
    assert pos.x == 4 and pos.y == 6

    pos = Game.mapPos("c7")
    assert pos.x == 2 and pos.y == 1

    pos = Game.mapPos("h8")
    assert pos.x == 7 and pos.y == 0

    pos = Game.mapPos("h1")
    assert pos.x == 7 and pos.y == 7



class Pos:
    def __init__(self, x=0, y=0):
        # This position x, y is optional and I will delete it later, the source of truth is the board for now
        self.x = x
        self.y = y

class Piece:
    hasMoved = False

    class CantMoveToSamePositionException(Exception):
        pass

    class InvalidMoveException(Exception):
        pass

    def __init__(self, player_id, x=0, y=0):
        self.player_id = player_id
        self.x = x
        self.y = y
        self.hasMoved = False

    # returns true if the piece can physically move to pos
    def canMove(self, p2):
        if (self.x==p2.x and self.y==p2.y):
            raise self.CantMoveToSamePositionException
    
    # returns true if the piece can physically kill the piece in pos
    def canKill(self, p2):
        return self.canMove(p2)
    
    # changes piece's pos to p2
    def move(self, p2):
        self.x = p2.x
        self.y = p2.y

    # returns sequence of positions to move to p2 including p2, it will return empty list if already at p2
    def getTrajectoryTo(self, p2):
        self.canMove(p2)
        #assert self.canMove(p2) # TODO: raise exception
        result = []
        
        vector_x = 0 if (p2.x == self.x) else (p2.x - self.x) / (p2.x - self.x)
        vector_y = 0 if (p2.y == self.y) else (p2.y - self.y) / (p2.y - self.y)
        # direction vector of 1 and 0's (x, y): 1,1 0,0 -1,0 0,-1 etc
        vector = Pos(vector_x, vector_y)
        distance = max((p2.x - self.x), (p2.y - self.y))
        
        for i in range(1, distance+1):
            result.append(Pos(self.x + i*vector.x, self.y + i*vector.y))

        return result
    
# TODO: write tests for Pawn
class Pawn(Piece):
    _type = "Pawn"
    _symbol = "P"
    # direction
    # startPos

    def __init__(self, player_id, direction, x=0, y=0):
        Piece.__init__(self, player_id, x=x, y=y)
        self.direction = direction
        self.startPos = Pos(x,y)
        
    def canMove(self, p2):
        Piece.canMove(self, p2)
        if (abs(self.x - p2.x) != 0):
            print("{} can't go sideways".format(self._type))
            return False # can't go sideways

        if ((p2.y - self.y) / abs(self.y - p2.y) != self.direction):
            print("{} can only move in player's direction!".format(self._type))
            return False
        
        # if pos==startPos, can move 2 or 1
        if self.x==self.startPos.x and self.y==self.startPos.y:
            if abs(self.y - p2.y) == 1 or abs(self.y - p2.y) == 2:
                return True
        else:
            if abs(self.y - p2.y) == 1:
                return True

        return False
    
    def canKill(self, p2):
        Piece.canMove(self, p2)
        if (p2.y - self.y / abs(self.y - p2.y) != self.direction):
            return False # can only move in player's direction

        if abs(self.y - p2.y) == 1 and abs(self.x - p2.x) == 1:
            return True

        return False

    def getTrajectoryTo(self, p2):
        if self.canMove(p2) or self.canKill(p2):
            
            if abs(self.y - p2.y) <= 1:
                return [p2]
            else: # difference = 2
                pos1 = Pos(self.x, self.y + self.direction)
                pos2 = Pos(self.x, self.y + self.direction * 2)
                return [pos1, pos2]
        else:
            return []

    # returns list of positions this player can physically move to or kill to, independent of game logic
    def getAllPossibleMoves(self):
        return [ Pos(self.x, self.y + direction),
                 Pos(self.x, self.y + 2 * direction),
                 Pos(self.x + 1, self.y + direction),
                 Pos(self.x - 1, self.y + direction)
                ]


class Rook(Piece):
    _type = "Rook"
    _symbol = "R"
    
    def canMove(self, p2):
        Piece.canMove(self, p2)
        return self.x == p2.x or self.y == p2.y

    # TODO: add tests for getPossibleMovesFrom to all pieces
    # returns list of positions this player can physically move to or kill to, independent of game logic
    def getAllPossibleMoves(self):
        positions = []

        for i in range(1,9):
            positions.append(Pos(self.x, self.y + i))
            positions.append(Pos(self.x, self.y - i))
            positions.append(Pos(self.x + i, self.y))
            positions.append(Pos(self.x - i, self.y))

        return positions

class Knight(Piece):
    _type = "Knight"
    _symbol = "H"
    
    def canMove(self, p2):
        Piece.canMove(self, p2)
        return abs(self.x - p2.x) <= 2 and abs(self.y - p2.y) <= 2 and ( abs(self.x - p2.x) + abs(self.y - p2.y) ) == 3

    def getTrajectoryTo(self, p2):
        if self.canMove(p2):
            return [p2]
        else:
            return []

    # returns list of positions this player can physically move to or kill to, independent of game logic
    def getAllPossibleMoves(self):
        return [ 
                 Pos(self.x + 2, self.y + 1),
                 Pos(self.x + 2, self.y - 1),
                 Pos(self.x - 2, self.y + 1),
                 Pos(self.x - 2, self.y - 1),

                 Pos(self.x + 1, self.y + 2),
                 Pos(self.x + 1, self.y - 2),
                 Pos(self.x - 1, self.y + 2),
                 Pos(self.x - 1, self.y - 2)
                ]



class Bishop(Piece):
    _type = "Bishop"
    _symbol = "B"
    
    def canMove(self, p2):
        Piece.canMove(self, p2)
        return abs(self.x - p2.x) == abs(self.y - p2.y)

    # returns list of positions this player can physically move to or kill to, independent of game logic
    def getAllPossibleMoves(self):
        positions = []

        for i in range(1,9):
            positions.append(Pos(self.x + i, self.y + i))
            positions.append(Pos(self.x + i, self.y - i))
            positions.append(Pos(self.x - i, self.y + i))
            positions.append(Pos(self.x - i, self.y - i))

        return positions

class Queen(Piece):
    _type = "Queen"
    _symbol = "Q"
    
    def canMove(self, p2):
        Piece.canMove(self, p2)
        return (self.x == p2.x or self.y == p2.y) or ( abs(self.x - p2.x) == abs(self.y - p2.y) ) # rook or bishop

    # returns list of positions this player can physically move to or kill to, independent of game logic
    def getAllPossibleMoves(self):
        positions = []

        for i in range(1,9):
            # Rook
            positions.append(Pos(self.x, self.y + i))
            positions.append(Pos(self.x, self.y - i))
            positions.append(Pos(self.x + i, self.y))
            positions.append(Pos(self.x - i, self.y))

            # Bishop
            positions.append(Pos(self.x + i, self.y + i))
            positions.append(Pos(self.x + i, self.y - i))
            positions.append(Pos(self.x - i, self.y + i))
            positions.append(Pos(self.x - i, self.y - i))

        return positions

class King(Piece):
    _type = "King"
    _symbol = "K"
    
    def canMove(self, p2):
        Piece.canMove(self, p2)
        return ( abs(self.x - p2.x) == 1 or abs(self.y - p2.y) == 1 ) and ( abs(self.x - p2.x) + abs(self.y - p2.y) <= 2 ) 

    def canKill(self, p2):
        # TODO: special case, can only kill if that piece is not protected
        return False

    # returns list of positions this player can physically move to or kill to, independent of game logic
    def getAllPossibleMoves(self):
        return [
                Pos(self.x + 1, self.y),
                Pos(self.x - 1, self.y),
                Pos(self.x, self.y + 1),
                Pos(self.x, self.y - 1),
                Pos(self.x + 1, self.y + 1),
                Pos(self.x + 1, self.y - 1),
                Pos(self.x -1, self.y + 1),
                Pos(self.x - 1, self.y - 1)
                ]

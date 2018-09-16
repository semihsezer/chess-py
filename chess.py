from pprint import pprint
import copy
from piece import *
from player import *

print("Welcome to chess py!")

# Board
# 8 x 8

# Board = [[],
#          [],
#          [],
#          [],
#          [],
#          [],
#          [],
#          [] ]
# makeMove(p1, p2)

# Player

# TODO: board should be a class of its own
board=[[None for i in range(8)] for i in range(8)]


# PLAYERS: 0 is black, 1 is white
# SQUARES: x + y == even => black, odd => white
# DIRECTION: black goes from 0 to 7, white goes from 7 to 0

class OtherPlayersTurnException(Exception):
    pass

class OtherPlayersPieceException(Exception):
    pass

class NoPieceInPositionException(Exception):
    pass

class KingUnderAttackException(Exception):
    pass

class KingCantBeKilledException(Exception):
    pass

class GameOverException(Exception):
    pass


class Game:
    # board
    # players
    # deadPieces
    # currentPlayer
    # gameOver

    class ValidRokMoveException(Exception):
        pass
    class ValidEnPassantMoveException(Exception):
        pass

    # takes list of pieces for an existing game where each piece has a position
    def __init__(self, board=[], currentPlayer=1, gameOver=False, lastMove=None, deadPieces={0: [], 1: []}):
        self.board = [[ None for i in range(8)] for i in range(8)]
        self.players = [Player(0), Player(1)]
        self.deadPieces = deadPieces
        self.currentPlayer = currentPlayer
        self.gameOver = gameOver
        self.lastMove = lastMove # [p1, p2]

        if len(board) > 0:
            print("Creating game from a given board...")
            # TODO: should we check if the board is valid? I don't think we need it...
            self.board = board
            self.currentPlayer = currentPlayer
            # TODO: should fill self.deadPieces of each player
            #self.insertPieces(pieces)
        else:
            print("Creating a new game...")

            self.initializePieces()

    def initializePieces(self):
        ''' 
        initalizes the board with the pieces for each player 
        NOTE: for now, the black player is always at the top, white always at the bottom
        '''
        for i in range(0,2):
            player = self.players[i]
            y = i * 7
            pieces = []
            
            # TODO: y depends on the side of player, white gets one place black gets another

            # create pawns
            for i in range(0,8):
                y_val = 6 if (y+1 > 7) else 1
                p = Pawn(player._id, player.direction, x=i, y=y_val)
                pieces.append(p)

            # create rooks
            pieces.append(Rook(player._id, x=0, y=y))
            pieces.append(Rook(player._id, x=7, y=y))
            
            # create knights
            pieces.append(Knight(player._id, x=1, y=y))
            pieces.append(Knight(player._id, x=6, y=y))
            
            # create bishops
            pieces.append(Bishop(player._id, x=2, y=y))
            pieces.append(Bishop(player._id, x=5, y=y))
            
            # create queen
            pieces.append(Queen(player._id, x=3, y=y))
            #assert ((3+y) % 2) != 0 # white queen on white square
            
            # create king
            pieces.append(King(player._id, x=4, y=y))

            self.insertPieces(pieces)
            player.pieces = pieces


    # moves the piece in p1 to p2, if the move is valid
    def makeMove(self, player, p1, p2, board=None):
        print("inside makeMove")
        if board == None:
            board = self.board

        if self.gameOver:
            raise GameOverException

        if self.currentPlayer != player._id: raise OtherPlayersTurnException 

        try:
            if self.isMoveValid(p1, p2, board, player._id):
                
                # TODO: prepare and propose the board
                newGame = copy.deepcopy(self)
                newGame.movePiece(p1, p2, board)

                # check if king of player is under attack, as long as this is correct no king can be killed
                if newGame.isKingUnderAttack(board, player._id):
                    raise KingUnderAttackException

                # modifies the board
                self.movePiece(p1, p2, board)
        
        # implies p2 is empty, no risk of killing King
        except self.ValidRokMoveException:
            newGame = copy.deepcopy(self)
            newGame.movePieceRok(p1, p2, new_board)

            if newGame.isKingUnderAttack(board, player._id):
                    raise KingUnderAttackException

            # modifies the board
            self.movePieceRok(p1, p2, board)
        
        # implies p2 is empty, no risk of killing King
        except self.ValidEnPassantMoveException:
            newGame = copy.deepcopy(self)
            newGame.movePieceEnPassant(p1, p2, new_board)

            if newGame.isKingUnderAttack(board, player._id):
                    raise KingUnderAttackException

            self.movePieceEnPassant(p1, p2, new_board)

        except:
            raise

        if self.isGameOver(self.getOtherPlayer(), board):
            print("Checkmate! {} wins!".format(self.players[currentPlayer].name))
            self.gameOver = True

        

    # checks whether a piece can
    #    - physically move to p2 from p1 or whether it can kill a piece there and whether the path is free
    #    - legally move to p2 from p1 based on the board (if it can only kill, is there a piece in p2? is the king of player exposed etc)
    # when it is player_id's turn
    # For the concern of this function, a king can be killed
    def isMoveValid(self, p1, p2, board, player_id):
        # TODO: let's move board to another object because we are passing current player and board to every method
        print("inside isMoveValid")
        print("checking if ({},{}) can move to ({},{})".format(p1.x, p1.y, p2.x, p2.y))
        if board[p1.y][p1.x] == None: raise NoPieceInPositionException 
        p = board[p1.y][p1.x]
            
        if player_id != p.player_id: raise OtherPlayersPieceException

        # same spot TODO: this is not needed, p.canMove() throws that exception
        if (p1.x == p2.x and p1.y == p2.y):
            return False

        # check for board range
        if (p1.x < 0 or p1.x > 7 or p1.y < 0 or p1.y > 7 or p2.x < 0 or p2.x > 7 or p2.y < 0 or p2.y > 7):
            print("Move out of range: from ({},{}) to ({},{})".format(p1.x, p1.y, p2.x, p2.y))
            return False

        # make sure p2 doesn't have the player's piece
        if board[p2.y][p2.x] != None and board[p2.y][p2.x].player_id == player_id:
            print("ERROR: Can't move on top of your own piece in ({},{}). There is a {} there!".format(p2.x, p2.y, board[p2.y][p2.x]._type))
            return False
        
        # doesn't check if there is a check at the end
        if self.isValidRokMove(p1, p2, board, player_id):
            raise self.ValidRokMoveException

        # doesn't check if there is a check at the end
        elif self.isValidEnPassantMove(p1, p2, board, player_id):
            raise self.ValidEnPassantMoveException

        if not p.canMove(p2):
            # TODO: we need to check for pawn, it shouldn't be able to move on to another piece
            if p.canKill(p2):
                if board[p2.y][p2.x] == None:
                    print("ERROR: {} {} can only kill to ({},{}) but the spot is empty!".format(p._type, p._symbol, p2.x, p2.y))
                    return False

            else: # can't kill
                print("ERROR: {} {} can't move or kill to ({},{})!".format(p._type, p._symbol, p2.x, p2.y))
                return False

        # check whether path is clear
        trajectory = p.getTrajectoryTo(p2)
        for i in range(0, len(trajectory) - 1):
            pos = trajectory[i]
            if board[pos.y][pos.x] != None:
                print("ERROR: Path from ({},{}) to ({},{}) is not clear for {}! There is a {} at ({},{})".format(p1.x, p1.y, p2.x, p2.y, p._type, board[pos.y][pos.x]._type, pos.x, pos.y))
                return False

        # TODO: check for game rules, what else is there?

        return True



    # returns true if a Rok attempt is valid, independent of other game logic
    # assumes the move itself is valid (player moves his own piece etc)
    def isValidRokMove(self, p1, p2, board, player_id):
        if board[p1.y][p1.x]._symbol == King._symbol and not board[p1.y][p1.x].hasMoved and\
            p1.y == p2.y and abs(p1.x - p2.x) == 2: # attempt to move 2 squares on the same line
            direction = (p1.x - p2.x) / abs(p1.x - p2.x)
            king = board[p1.y][p1.x]
            rook = None
            
            rooks = self.getPieces(board, {player_id: king.player_id, symbol: Rook._symbol})
            
            # get the candidate rook for the rook attempt
            for r in rooks:
                # rook has to be in the direction of the move, has to be on the same line
                if direction == (p1.x - r["pos"].x / abs(p1.x - r["pos"].x) ) and r["pos"].y == p1.y:
                    if r["piece"].hasMoved == True:
                        return False
                    
                    rook = r["piece"]

            if rook == None:
                return False

            # check trajectory
            pos = Pos(p1.x + direction, p1.y)            
            if board[pos.y][pos.x] != None or self.isPosUnderAttackBy(self.getOtherPlayer(king.player_id), pos, board):
                return False

            # whether king is under attack at the end will be checked by isMoveAllowed
            if board[p2.y][p2.x] != None:
                return False

            return True

        return False

    # assumes the move itself is valid (player moves his own piece etc)
    # assumes last move was by the other player
    def isValidEnPassantMove(self, p1, p2, board, player_id):
        
        if board[p1.y][p1.x]._symbol == Pawn._symbol and board[p2.y][p2.x] == None:
            # pawn is making a valid move in the right direction
            if abs(p1.x - p2.x) == 1 and abs(p1.y - p2.y) == 1 and p1.y - p2.y == board[p1.y][p1.x].direction:
                lastPieceMoved = board[self.lastMove[1].y][self.lastMove[1].x]
                # check that the last move was the opponent's pawn making the initial 2 move
                if lastPieceMoved!=None and lastPieceMoved._symbol == Pawn._symbol and lastPieceMoved.player_id != board[p1.y][p1.x].player_id\
                    and abs(self.lastMove[0].y - self.lastMove[1].y) == 2:
                    
                    horizontalDirection = p2.x - p1.x
                    # opponent's pawn must be next to player's pawn in the horizontal direction of the en-passant move 
                    if (p1.x + horizontalDirection) == self.lastMove[1].x and p1.y == self.lastMove[1].y:
                        return True
        
        return False

    # moves piece from p1 to p2, if there is a piece in p2 it will be killed
    # assumes all validity checks have been done
    def movePiece(self, p1, p2, board):
        print("inside movePiece ({}{}) to ({},{})".format(p1.x, p1.y, p2.x, p2.y))
        piece = board[p1.y][p1.x]

        # if there is a piece there, kill it
        if board[p2.y][p2.x] != None:
            assert board[p2.y][p2.x].player_id != piece.player_id
            
            self.deadPieces[board[p2.y][p2.x].player_id].append(board[p2.y][p2.x])
            board[p2.y][p2.x] = None

        board[p2.y][p2.x] = piece
        piece.y = p2.y
        piece.x = p2.x
        piece.hasMoved = True
        self.lastMove = [p1, p2]
        
        board[p1.y][p1.x] = None

        # if a pawn reaches the end of the board, convert it to player's choice of Queen, Rook etc
        if piece._symbol == "P":
            if piece.direction == 1 and p2.y == 7:
                # TODO: convert to player's choice of Queen, Rook etc
                print("Convert Pawn to another piece:")
            elif piece.direction == -1 and p2.y == 0:
                # TODO: convert to player's choice of Queen, Rook etc
                print("Convert Pawn to another piece:")

    # assumes this is a valid rok move and all validity checks have been done + p2 is empty
    def movePieceRok(self, p1, p2, board):
        piece = board[p1.y][p1.x]

        # move the king
        board[p2.y][p2.x] = piece
        piece.y = p2.y
        piece.x = p2.x
        piece.hasMoved = True
        board[p1.y][p1.x] = None
        
        # get the candidate rook for the rook attempt
        rooks = self.getPieces(board, {player_id: piece.player_id, symbol: Rook._symbol})
        for r in rooks:
            # rook has to be in the direction of the move, has to be on the same line
            if direction == (p1.x - r["pos"].x / abs(p1.x - r["pos"].x) ) and r["pos"].y == p1.y:
                if r["piece"].hasMoved == True:
                    return False
                
                rook = r
        
        # move the rook
        assert rook != None
        direction = (p1.x - p2.x) / abs(p1.x - p2.x)
        oldRookPos = rook["pos"]
        newRookPos = Pos(p1.x + direction, p1.y)

        board[newRookPos.y][newRookPos.x] = rook["piece"]
        
        rook["piece"].y = newRookPos.y
        rook["piece"].x = newRookPos.x
        rook["piece"].hasMoved = True
        board[oldRookPos.y][oldRookPos.x] = None

        self.lastMove = [p1, p2]

    # assume this is a valid en passant move and all validity checks have been done + p2 is empty
    def movePieceEnPassant(self, p1, p2, board):
        piece = board[p1.y][p1.x]

        # move the pawn
        self.movePiece(self, p1, p2, board)

        # kill the other pawn
        horizontalDirection = p2.x - p1.x
        opponentPawnPos = Pos(p1.x + horizontalDirection, p1.y)
        opponentPawn = board[opponentPawnPos.y][opponentPawnPos.x]
        assert opponentPawn != None and opponentPawn.player_id != piece.player_id and opponentPawn._symbol == Pawn._symbol
        
        self.deadPieces[opponentPawn.player_id].append(opponentPawn)
        board[opponentPawnPos.y][opponentPawnPos.x] = None

    # checks if the spot is under attack by any of player_id's pieces with a valid move
    # This doesn't mean that the piece can move there (e.g. the piece is pinned)
    def isPosUnderAttackBy(self, player_id, pos, board):
        print("inside isPosUnderAttack: checking {}".format(board[pos.y][pos.x]._type))

        results = self.getPieces(board, {"player_id": player_id})
        assert len(results) > 0

        # check which ones can move to pos
        for piece in results:
            try:
                # TODO: we should ignore if the king is exposed, but right now isMoveValid checks for that
                if self.isMoveValid(piece["pos"], pos, board, player_id):
                    return True
            except:
                continue

        return False

    # isMoveAllowed checks whether a move is allowed in game logic (e.g. attempting moving to move a pawn when your check is under attack)
    # For now, it only checks whether the player's king is under attack in the given board
    def isKingUnderAttack(self, board, player_id):
        # check if current player's king will be defended after this move
        new_board = copy.deepcopy(board)
        new_board[p2.y][p2.x] = new_board[p1.y][p1.x]
        
        result = self.getPieces(new_board, {"player_id": player_id, "symbol": King._symbol})
        assert len(result) == 1
        kingPos = result[0]["pos"]
        if self.isPosUnderAttackBy(self.getOtherPlayer(player_id), kingPos, new_board):
            print("ERROR: Check, King needs to be defended!") # TODO: raise exception
            return False # TODO: raise exception

        return True

    # check if game is over when currentPlayer cannot make a move to save his check
    def isGameOver(self, player_id, board):
        result = self.getPieces(board, {"player_id": player_id, "symbol": King._symbol})
        assert len(result) == 1
        kingPos = result[0]["pos"]

        # TODO for later: check for draw conditions, stale mate etc
        if self.isPosUnderAttackBy(self.getOtherPlayer(player_id), kingPos, board):
            boards = self.getAllValidBoardsFrom(player_id, board)

            for b in boards:
                result = self.getPieces(b, {"player_id": player_id, "symbol": King._symbol})
                assert len(result) == 1
                kingPos = result[0]["pos"]
                if not self.isPosUnderAttackBy(self.getOtherPlayer(player_id), kingPos, b):
                    return False
                else:
                    return True
        else:
            return False

    # return all possible boards from board when player_id will make next move
    def getAllValidBoardsFrom(self, player_id, board):
        validBoards = []
        nextMoves = []
        player = self.players[player_id]

        for p in player.pieces:
            nextPositions = p.getAllPossibleMoves()
            for pos in nextPositions:
                nextMoves.append([Pos(p.x, p.y), pos])
            
        for move in nextMoves:
            try:
                # newGame
                # newGame.makeMove
                # if it succeeds, add to listofGames
                
                # TODO: don't check for valid move here, just do the move anyways
                if self.isMoveValid(move[0], move[1], board, player_id):
                    new_board = copy.deepcopy(board)
                    self.movePiece(p1, p2, new_board)
                    validBoards.append(new_board)
            except:
                continue

        # check if those moves are valid in the game logic

        return validBoards

    # returns the id of other player
    def getOtherPlayer(self, player_id=None):
        if player_id == None:
            player_id = self.currentPlayer
        
        return (player_id + 1) % 2

    # returns pieces on the board with their positions that fit the filters specified in opts
    def getPieces(self, board, opts):
        print("inside getPieces")
        pieces = [] # {"pos": Pos(x,y), "piece": piece}

        for i in range(0,8):
            for j in range(0,8):
                if board[j][i] != None:
                    cond1 = (board[j][i].player_id == opts["player_id"]) if "player_id" in opts else True
                    cond2 = (board[j][i]._symbol == opts["symbol"]) if "symbol" in opts else True

                    if cond1 and cond2:
                        pieces.append({"pos": Pos(i,j), "piece": board[j][i]})

        return pieces
    
    # ----- The methods below are only for setting up the board, not connected to the game -------
    # takes a list of pieces with positions and sets the board to that
    def insertPieces(self, pieces):
        for p in pieces:
            self.insertPiece(p, p.x, p.y)
            
    # insert a piece to the board to the position of the piece
    def insertPiece(self, p, x, y):
        print("inserting {} to x={}, y={}".format(p._type, x, y))

        if self.board[y][x] == None:
            self.board[y][x] = p
        else:
            # TODO: raise exception for this
            print('ERROR while placing a piece')

    def printBoard(self):
        new_list = [["0" for i in range(8)] for i in range(8)]
        
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                obj = self.board[i][j]

                if obj == None:
                    new_list[i][j] = "0"
                else:
                    new_list[i][j] = obj._symbol

        pprint(new_list)

# --------------------------------------------------------------------------------------------------

game = Game()
game.printBoard()
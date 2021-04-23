import random

# players = ["Player 1", "Player 2", "Player 3", "Player 4"]
#
# colors = ["Blue", "Yellow", "Green", "Red"]
#
# blue_pawns = ["Blue 1", "Blue 2", "Blue 3"]
# yellow_pawns = ["Yellow 1", "Yellow 2", "Yellow 3"]
# green_pawns = ["Green 1", "Green 2", "Green 3"]
# red_pawns = ["Red 1", "Red 2", "Red 3"]
#
# card_dict = {"1": 1, "2": 2, "3": 3, "4": -4, "5": 5, "7": seven(), "8": 8, "10": ten(), "11": eleven(), "12": 12,
#              "Sorry!": sorry()}
#
#
# # need to define the space each pawn for each player is on
# pawn_space = 0

deck_cards = ["1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "7",
              "7", "7", "7", "8", "8", "8", "8", "10", "10", "10", "10", "11", "11", "11", "11", "12", "12", "12", "12",
              "Sorry!", "Sorry!", "Sorry!", "Sorry!"]

discard_pile = []


class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.pieces.append(Pieces(color, 1))
        self.pieces.append(Pieces(color, 2))
        self.pieces.append(Pieces(color, 3))

    def __str__(self):
        output = str(self.color) + "Player has ["
        for index, piece in enumerate(self.pieces):
            output = output + str(index) + ": " + str(piece) + ", "
        return output[:-2] + "]"


class Pieces:
    def __init__(self, color, number):
        self.color = color  # blue, yellow, green, or red
        self.number = number  # pawn number
        self.start = None
        self.safety = None
        self.home = None

    def can_swap(self, other):
        # if the player piece and other piece is not in start, the safety zone, or home, can swap
        if self.start is not None and self.safety is not None and self.home is not None:
            if other.start is not None and other.safety is not None and other.home is not None:
                return True
            else:
                return False
        else:
            pass


class Deck:
    def __init__(self, card):
        self.card = card

    def draw_card(self):
        shuffled_deck = random.shuffle(deck_cards)
        card_drawn = shuffled_deck[0]
        return card_drawn

    def discard_card(self, card_drawn):
        deck_cards.remove(card_drawn)
        discard_pile.append(card_drawn)

    def reshuffle(self, card):
        pass


class Board:
    def __init__(self):
        self.game_board = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, "--", None, "--", None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None],
            [None, "--", None, "--", "--", "--", "--", "--", "--", None, None, None, None, None, None, None],
            [None, "--", None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None],
            [None, "--", None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None, None],
            [None, "--", None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None],
            [None, "--", None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None],
            [None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None],
            [None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None],
            [None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None, "--", None],
            [None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None, "--", None],
            [None, None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None, "--", None],
            [None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None, "--", None],
            [None, None, None, None, None, None, None, "--", "--", "--", "--", "--", "--", None, "--", None],
            [None, "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", None, "--", None, "--", None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        ]
        # Blue starts at row[15], col[12]
        # Blue safety zone is row[10-15], col[14]
        # Blue home is row[10], col[14]
        # Yellow starts at row[12], col[2]
        # Yellow safety zone is row[14], col[2-7]
        # Yellow home is row[14], col[7]
        # Green starts at row[2], col[5]
        # Green safety zone is row[2-7], col[2]
        # Green home is row[7], col[2]
        # Red starts at row[5], col[15]
        # Red safety zone is row[2], col[10-15]
        # Red home is row[2], col[10]
        # [Yellow/Blue/Red] Slide Start row[1], col[2]
        # [Yellow/Blue/Red] Slide End row[1], col[5]
        # [Yellow/Blue/Red] Slide Start row[1], col[10]
        # [Yellow/Blue/Red] Slide End row[1], col[14]
        # [Green/Yellow/Blue] Slide Start row[2], col[16]
        # [Green/Yellow/Blue] Slide End row[5], col[16]
        # [Green/Yellow/Blue] Slide Start row[10], col[16]
        # [Green/Yellow/Blue] Slide End row[14], col[16]
        # [Red/Green/Yellow] Slide Start row[16], col[15]
        # [Red/Green/Yellow] Slide End row[16], col[12]
        # [Red/Green/Yellow] Slide Start row[16], col[7]
        # [Red/Green/Yellow] Slide End row[16], col[3]
        # [Blue/Red/Green] Slide Start row[15], col[1]
        # [Blue/Red/Green] Slide End row[12], col[1]
        # [Blue/Red/Green] Slide Start row[7], col[1]
        # [Blue/Red/Green] Slide End row[3], col[1]

    def place(self, piece, row, col):
        self.game_board[row][col] = piece

    def move_piece(self, card_drawn):
        # move piece based on card drawn, card function
        # move piece 50, if that move takes piece off the board rotate 90 and continue
        pass


# def seven():
#     # code
#     seven_decision = input("Would you like to split your move between two of your pawns? Yes/No: ")
#     if seven_decision.lower() == "yes":
#         # ask the player which pawn they would like to move
#         # ask the player how many spaces they would like the pawn they've chosen to move
#         # (if more than two pawns are out of Start), ask the player the second pawn they'd like to move forward
#         # apply remainder of move to second pawn
#         pass
#     else:
#         pawn_space += 7
#     pass
#
#
# def ten():
#     # code
#     if pawn_space + 10 < 60: # if moving forward 10 spaces doesn't take the player past "Home"
#         ten_decision = input("Would you like to move your pawn forward 10 spaces? Yes/No: ")
#         if ten_decision.lower() == "yes":
#             pawn_space += 10
#         else:
#             pawn_space -= 1
#     else:
#         pawn_space -= 1
#     pass
#
#
# def eleven():
#     # code
#     if pawn_space + 11 < 60: # if moving forward 11 spaces doesn't take the player past "Home"
#         eleven_decision = input("Would you like to switch pawns with another player? Yes/No: ")
#         if eleven_decision.lower() == "yes":
#             # ask player what pawn they would like to switch with
#             # check to make sure pawn is not in safety zone, "Home", or Start
#         else:
#             pawn_space += 11
#     else:
#         pawn_space += 0
#     pass
#
#
# def sorry():
#     # code
#     pass
#

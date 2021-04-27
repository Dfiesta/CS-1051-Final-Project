import random
import turtle
import tkinter

turtle.setup(850, 850)

window = turtle.Screen()
window.title("Solitary Sorry!")

canvas = window.getcanvas()
turtle.setworldcoordinates(-425, -425, 425, 425)

game_board_img = tkinter.PhotoImage(file="Sorry!-Board-Background.gif")
canvas.create_image(0, 0, anchor="center", image=game_board_img)

window.register_shape("Blue_pawn.gif")
blue_pawn_1 = turtle.Turtle()
blue_pawn_1.shape("Blue_pawn.gif")
blue_pawn_1.penup()
blue_pawn_1.goto(175, -325)

blue_pawn_2 = turtle.Turtle()
blue_pawn_2.shape("Blue_pawn.gif")
blue_pawn_2.penup()
blue_pawn_2.goto(175, -325)

blue_pawn_3 = turtle.Turtle()
blue_pawn_3.shape("Blue_pawn.gif")
blue_pawn_3.penup()
blue_pawn_3.goto(175, -325)

window.register_shape("Yellow_pawn.gif")
yellow_pawn_1 = turtle.Turtle()
yellow_pawn_1.shape("Yellow_pawn.gif")
yellow_pawn_1.penup()
yellow_pawn_1.goto(-325, -175)

yellow_pawn_2 = turtle.Turtle()
yellow_pawn_2.shape("Yellow_pawn.gif")
yellow_pawn_2.penup()
yellow_pawn_2.goto(-325, -175)

yellow_pawn_3 = turtle.Turtle()
yellow_pawn_3.shape("Yellow_pawn.gif")
yellow_pawn_3.penup()
yellow_pawn_3.goto(-325, -175)

window.register_shape("Green_pawn.gif")
green_pawn_1 = turtle.Turtle()
green_pawn_1.shape("Green_pawn.gif")
green_pawn_1.penup()
green_pawn_1.goto(-175, 325)

green_pawn_2 = turtle.Turtle()
green_pawn_2.shape("Green_pawn.gif")
green_pawn_2.penup()
green_pawn_2.goto(-175, 325)

green_pawn_3 = turtle.Turtle()
green_pawn_3.shape("Green_pawn.gif")
green_pawn_3.penup()
green_pawn_3.goto(-175, 325)

window.register_shape("Red_pawn.gif")
red_pawn_1 = turtle.Turtle()
red_pawn_1.shape("Red_pawn.gif")
red_pawn_1.penup()
red_pawn_1.goto(325, 175)

red_pawn_2 = turtle.Turtle()
red_pawn_2.shape("Red_pawn.gif")
red_pawn_2.penup()
red_pawn_2.goto(325, 175)

red_pawn_3 = turtle.Turtle()
red_pawn_3.shape("Red_pawn.gif")
red_pawn_3.penup()
red_pawn_3.goto(325, 175)

# players = ["Player 1", "Player 2", "Player 3", "Player 4"]
#
# blue_pawns = ["Blue 1", "Blue 2", "Blue 3"]
# yellow_pawns = ["Yellow 1", "Yellow 2", "Yellow 3"]
# green_pawns = ["Green 1", "Green 2", "Green 3"]
# red_pawns = ["Red 1", "Red 2", "Red 3"]
#
# card_dict = {"1": 1, "2": 2, "3": 3, "4": -4, "5": 5, "7": seven(), "8": 8, "10": ten(), "11": eleven(), "12": 12,
#              "Sorry!": sorry()}
#

colors = ["Blue", "Yellow", "Green", "Red"]

DECK_CARDS = ["1", "1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5",
              "7", "7", "7", "7", "8", "8", "8", "8", "10", "10", "10", "10", "11", "11", "11", "11", "12", "12", "12",
              "12", "Sorry!", "Sorry!", "Sorry!", "Sorry!"]


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
        self.start = True
        self.safety = False
        self.home = False

    # Coordinates of starts
        if self.color == "Blue":
            self.coordinates = [175, -325]
        elif self.color == "Yellow":
            self.coordinates = [-325, -175]
        elif self.color == "Green":
            self.coordinates = [-175, 325]
        elif self.color == "Red":
            self.coordinates = [325, 175]

    def can_swap(self, other):
        # if the player piece and other piece is not in start, the safety zone, or home, can swap
        if self.start is False and self.safety is False and self.home is False:
            if other.start is False and other.safety is False and other.home is False:
                return True
            else:
                return False


class Deck:
    def __init__(self, deck_cards):
        self.shuffled_deck = random.shuffle(deck_cards)
        self.discard_pile = []

    def draw_card(self):
        if len(self.shuffled_deck) > 0:
            card_drawn = self.shuffled_deck[0]
            self.shuffled_deck.remove(card_drawn)
        else:
            self.shuffled_deck = self.discard_pile
            self.discard_pile.clear()
            card_drawn = self.shuffled_deck[0]
            self.shuffled_deck.remove(card_drawn)
        return card_drawn

    def discard_card(self, card_drawn):
        self.discard_pile.append(card_drawn)

    def draw_four(self, card_drawn, piece):
        # Move piece backwards 4 spaces
        pass

    def draw_seven(self, card_drawn, piece):
        # Move one pawn forward 7 spaces or split forward move of 7 spaces between two pawns
        # seven_decision = input("Would you like to split your move between two of your pawns? Yes/No: ")
        # if seven_decision.lower() == "yes":
            # ask the player which pawn they would like to move
            # ask the player how many spaces they would like the pawn they've chosen to move
            # (if more than two pawns are out of Start), ask the player the second pawn they'd like to move forward
            # apply remainder of move to second pawn
        #     pass
        # else:
            # pawn_space += 7
        pass

    def draw_ten(self, card_drawn, piece):
        # Move one pawn forward 10 spaces or move one pawn backward 1 space
        # if pawn_space + 10 < 60: # if moving forward 10 spaces doesn't take the player past "Home"
        #     ten_decision = input("Would you like to move your pawn forward 10 spaces? Yes/No: ")
        #     if ten_decision.lower() == "yes":
                # pawn_space += 10
            # else:
                # pawn_space -= 1
        # else:
            # pawn_space -= 1
        pass

    def draw_eleven(self, card_drawn, piece):
        # Move one pawn forward 11 spaces or switch one pawn with an opponent's
        # if pawn_space + 11 < 60: # if moving forward 11 spaces doesn't take the player past "Home"
        #     eleven_decision = input("Would you like to switch pawns with another player? Yes/No: ")
        #     if eleven_decision.lower() == "yes":
                # ask player what pawn they would like to switch with
                # check to make sure pawn is not in safety zone, "Home", or Start
        #     else:
        #         pawn_space += 11
        # else:
        #     pawn_space += 0
        pass

    def draw_sorry(self, card_drawn, piece):
        # Move one pawn from player's start area to take the place of an opponent's pawn, which must return to start
        # or move one pawn forward 4 spaces
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

    # def place(self, piece, row, col):
    #     self.game_board[row][col] = piece

    def move_piece(self, piece, card_drawn):
        # move piece based on card drawn, card function
        # set piece.start = False
        if piece.start is True:
            if piece.color == "Blue":
                # Select pawn to move, and move out of start
                piece.start = False
            if piece.color == "Yellow":
                # Select pawn to move, and move out of start
                piece.start = False
            if piece.color == "Green":
                # Select pawn to move, and move out of start
                piece.start = False
            if piece.color == "Red":
                # Select pawn to move, and move out of start
                piece.start = False
        else:
            # Select pawn to move, and move pawn number of spaces based on card_drawn
            # If move takes pawn off board, rotate 90 and continue
            pass

    def slide(self, piece):
        # Blue slides:
        # Start: [-375, -325]; End: [-375, -175]
        # Start: [-375, 75]; End: [-375, 275]
        # Start: [-325, 375]; End: [-175, 375]
        # Start: [75, 375]; End: [275, 375]
        # Start: [375, 325]; End: [375, 175]
        # Start: [375, -75]; End: [375, -275]
        # Yellow slides:
        # Start: [-325, 375]; End: [-175, 375]
        # Start: [75, 375]; End: [275, 375]
        # Start: [375, 325]; End: [375, 175]
        # Start: [375, -75]; End: [375, -275]
        # Start: [325, -375]; End: [175, -375]
        # Start: [-75, -375]; End: [-275, -375]
        # Green slides:
        # Start: [375, 325]; End: [375, 175]
        # Start: [375, -75]; End: [375, -275]
        # Start: [325, -375]; End: [175, -375]
        # Start: [-75, -375]; End: [-275, -375]
        # Start: [-375, -325]; End: [-375, -175]
        # Start: [-375, 75]; End: [-375, 275]
        # Red slides:
        # Start: [325, -375]; End: [175, -375]
        # Start: [-75, -375]; End: [-275, -375]
        # Start: [-375, -325]; End: [-375, -175]
        # Start: [-375, 75]; End: [-375, 275]
        # Start: [-325, 375]; End: [-175, 375]
        # Start: [75, 375]; End: [275, 375]
        pass


turtle.exitonclick()

green_1 = Pieces("Green", 1)
green_1.start = False

from objects.board import Board
from objects.food import Food
from objects.score import Score
from objects.snake import Snake


if __name__ == "__main__":
    brd = Board(800,600)
    brd.win.title('Worm')
    brd.game()
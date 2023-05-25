from graphics import Window
from maze import Maze

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

LEFT_X = 50
TOP_X = 50

CELL_SIZE = 50

num_rows = (WINDOW_HEIGHT - 2 * TOP_X) // CELL_SIZE
num_cols = (WINDOW_WIDTH - 2 * LEFT_X) // CELL_SIZE


def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    Maze(LEFT_X, TOP_X, num_rows, num_cols, CELL_SIZE, window)
    window.wait_for_close()


main()

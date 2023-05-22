from graphics import Window, Maze

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

LEFT_EDGE = 50
TOP_EDGE = 50

CELL_SIZE = 50

num_rows = (WINDOW_HEIGHT - 2 * TOP_EDGE) // CELL_SIZE
num_cols = (WINDOW_WIDTH - 2 * LEFT_EDGE) // CELL_SIZE


def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    Maze(LEFT_EDGE, TOP_EDGE, num_rows, num_cols, CELL_SIZE, window)

    window.wait_for_close()


main()

from tkinter import Tk, BOTH, Canvas

BG_COLOR = 'white'
WALL_COLOR = 'black'
PATH_COLOR = 'red'
UNDO_PATH_COLOR = 'gray'

LINE_WIDTH = 2


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')

        self.__canvas = Canvas(self.__root, bg=BG_COLOR,
                               width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point, end_point):
        self.__start = start_point
        self.__end = end_point

    def draw(self, canvas, color):
        canvas.create_line(self.__start.x, self.__start.y,
                           self.__end.x, self.__end.y, fill=color, width=LINE_WIDTH)
        canvas.pack(fill=BOTH, expand=True)

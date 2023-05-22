from tkinter import Tk, BOTH, Canvas

BG_COLOR = 'white'
LINE_COLOR = 'black'

LINE_WIDTH = 2

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')

        self.__canvas = Canvas(self.__root, bg=BG_COLOR, width=width, height=height)
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

    def draw_line(self, line):
        line.draw(self.__canvas)


# x = 0: left of window
# y = 0: top of window
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Start and End are Point instances
class Line:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end 
    
    def draw(self, canvas):
        canvas.create_line(self.__start.x, self.__start.y, self.__end.x, self.__end.y, fill=LINE_COLOR, width=LINE_WIDTH)
        canvas.pack(fill=BOTH, expand=True)

# x1, y1: top-left
# x2, y2: bottom-right
class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__window = window

    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)))
        if self.has_right_wall:
            self.__window.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)))
        if self.has_top_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)))
        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)))
        
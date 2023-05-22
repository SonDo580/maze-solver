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

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)


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
    
    def draw(self, canvas, color):
        canvas.create_line(self.__start.x, self.__start.y, self.__end.x, self.__end.y, fill=color, width=LINE_WIDTH)
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
            self.__window.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), WALL_COLOR)
        if self.has_right_wall:
            self.__window.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), WALL_COLOR)
        if self.has_top_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), WALL_COLOR)
        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), WALL_COLOR)
    
    def get_center(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
    
    def draw_move(self, to_cell, undo=False):
        color = PATH_COLOR
        if undo:
            color = UNDO_PATH_COLOR

        self.__window.draw_line(Line(self.get_center(), to_cell.get_center()), color)
        

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
        
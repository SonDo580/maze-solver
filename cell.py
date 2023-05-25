from graphics import *


class Cell:
    def __init__(self, left_x, top_y, right_x, bottom_y, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = left_x
        self.__x2 = right_x
        self.__y1 = top_y
        self.__y2 = bottom_y
        self.__window = window
        self.visited = False

    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        top_right = Point(self.__x2, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)

        if self.has_left_wall:
            self.__window.draw_line(Line(top_left, bottom_left), WALL_COLOR)
        else:
            self.__window.draw_line(Line(top_left, bottom_left), BG_COLOR)

        if self.has_right_wall:
            self.__window.draw_line(Line(top_right, bottom_right), WALL_COLOR)
        else:
            self.__window.draw_line(
                Line(top_right, bottom_right), BG_COLOR)

        if self.has_top_wall:
            self.__window.draw_line(Line(top_left, top_right), WALL_COLOR)
        else:
            self.__window.draw_line(Line(top_left, top_right), BG_COLOR)

        if self.has_bottom_wall:
            self.__window.draw_line(
                Line(bottom_left, bottom_right), WALL_COLOR)
        else:
            self.__window.draw_line(
                Line(bottom_left, bottom_right), BG_COLOR)

    def __get_center(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)

    def draw_move(self, to_cell, undo=False):
        color = PATH_COLOR
        if undo:
            color = UNDO_PATH_COLOR

        self.__window.draw_line(
            Line(self.__get_center(), to_cell.__get_center()), color)

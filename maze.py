import time
import random

from cell import Cell

CREATE_SLEEP_TIME = 0.01
SOLVE_SLEEP_TIME = 0.1


class Maze:
    def __init__(
        self,
        left_x_maze,
        top_y_maze,
        num_rows,
        num_cols,
        cell_size,
        window,
    ):
        self.__x1 = left_x_maze
        self.__y1 = top_y_maze
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size = cell_size
        self.__window = window
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_rows):
            self.__cells.append([])
            top_y = self.__y1 + self.__cell_size * i
            bottom_y = self.__y1 + self.__cell_size * (i + 1)

            for j in range(self.__num_cols):
                left_x = self.__x1 + self.__cell_size * j
                right_x = self.__x1 + self.__cell_size * (j + 1)

                new_cell = Cell(left_x, top_y, right_x,
                                bottom_y, self.__window)
                self.__cells[i].append(new_cell)

        self.__draw_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)
        self.__reset_cells_visited()
        self.__solve(0, 0)

    def __draw_cells(self):
        for row in self.__cells:
            for cell in row:
                self.__draw_cell(cell)

    def __draw_cell(self, cell):
        cell.draw()
        self.__animate(CREATE_SLEEP_TIME)

    def __animate(self, sleep_time):
        self.__window.redraw()
        time.sleep(sleep_time)

    def __break_entrance_and_exit(self):
        entrance_cell = self.__cells[0][0]
        exit_cell = self.__cells[self.__num_rows-1][self.__num_cols-1]

        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False

        self.__draw_cell(entrance_cell)
        self.__draw_cell(exit_cell)

    # row, col: indexes of current cell
    def __break_walls(self, row, col):
        self.__cells[row][col].visited = True
        while True:
            next_indexes = []

            # move left
            if col > 0 and not self.__cells[row][col - 1].visited:
                next_indexes.append((row, col - 1))

            # move right
            if col < self.__num_cols - 1 and not self.__cells[row][col + 1].visited:
                next_indexes.append((row, col + 1))

            # move up
            if row > 0 and not self.__cells[row - 1][col].visited:
                next_indexes.append((row - 1, col))

            # move down
            if row < self.__num_rows - 1 and not self.__cells[row + 1][col].visited:
                next_indexes.append((row + 1, col))

            # no where to go from here
            if len(next_indexes) == 0:
                self.__draw_cell(self.__cells[row][col])
                return

            # randomly choose a direction
            next_index = next_indexes[random.randrange(len(next_indexes))]

            # remove wall between current cell and next cell
            # move left
            if next_index[1] == col - 1:
                self.__cells[row][col].has_left_wall = False
                self.__cells[row][col - 1].has_right_wall = False

            # move right
            if next_index[1] == col + 1:
                self.__cells[row][col].has_right_wall = False
                self.__cells[row][col + 1].has_left_wall = False

            # move up
            if next_index[0] == row - 1:
                self.__cells[row][col].has_top_wall = False
                self.__cells[row - 1][col].has_bottom_wall = False

            # move down
            if next_index[0] == row + 1:
                self.__cells[row][col].has_bottom_wall = False
                self.__cells[row + 1][col].has_top_wall = False

            # move to the next cell and continue breaking walls
            self.__break_walls(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False

    def __solve(self, row, col):
        self.__animate(SOLVE_SLEEP_TIME)

        current_cell = self.__cells[row][col]
        current_cell.visited = True

        # current cell is exit cell
        if row == self.__num_rows - 1 and col == self.__num_cols - 1:
            return True

        # move left
        if col > 0:
            left_cell = self.__cells[row][col - 1]

            if not current_cell.has_left_wall and not left_cell.visited:
                current_cell.draw_move(left_cell)

                if self.__solve(row, col - 1):
                    return True

                current_cell.draw_move(left_cell, undo=True)

        # move right
        if col < self.__num_cols - 1:
            right_cell = self.__cells[row][col + 1]

            if not current_cell.has_right_wall and not right_cell.visited:
                current_cell.draw_move(right_cell)

                if self.__solve(row, col + 1):
                    return True

                current_cell.draw_move(right_cell, undo=True)

        # move up
        if row > 0:
            top_cell = self.__cells[row - 1][col]

            if not current_cell.has_top_wall and not top_cell.visited:
                current_cell.draw_move(top_cell)

                if self.__solve(row - 1, col):
                    return True

                current_cell.draw_move(top_cell, undo=True)

        # move down
        if row < self.__num_rows - 1:
            bottom_cell = self.__cells[row + 1][col]

            if not current_cell.has_bottom_wall and not bottom_cell.visited:
                current_cell.draw_move(bottom_cell)

                if self.__solve(row + 1, col):
                    return True

                current_cell.draw_move(bottom_cell, undo=True)

        # none of the directions worked out
        return False

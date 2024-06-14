from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = None if not seed else random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = [[Cell(self._win) for x in range(self._num_rows)]
                       for y in range(self._num_cols)]
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        # time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -
                                        1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = [
                (i+1, j),  # right
                (i, j+1),  # bottom
            ]
            if (i-1) >= 0:
                to_visit.append((i-1, j)) # left
            if (j-1) >= 0:
                to_visit.append((i, j-1)) # top
            possible_cells = []
            for adjacent in to_visit:
                if (adjacent[0] < self._num_cols
                    and adjacent[1] < self._num_rows
                    and self._cells[adjacent[0]][adjacent[1]].visited == False):
                    possible_cells.append(adjacent)
            if len(possible_cells) == 0:
                self._draw_cell(i, j)
                return
            direction = possible_cells[random.randrange(len(possible_cells))]
            if direction[0] < i:
                self._cells[i][j].has_left_wall = False
            elif direction[0] > i:
                self._cells[i][j].has_right_wall = False
            elif direction[1] > j:
                self._cells[i][j].has_bottom_wall = False
            elif direction[1] < j:
                self._cells[i][j].has_top_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(direction[0], direction[1])

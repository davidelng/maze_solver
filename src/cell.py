from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(left_wall, "black" if self.has_left_wall else "white")
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(top_wall, "black" if self.has_top_wall else "white")
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(right_wall, "black" if self.has_right_wall else "white")
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(bottom_wall, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1
        half_length_2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center_2 = half_length_2 + to_cell._x1
        y_center_2 = half_length_2 + to_cell._y1
        line = Line(Point(x_center, y_center), Point(x_center_2, y_center_2))
        self._win.draw_line(line, "red" if not undo else "gray")

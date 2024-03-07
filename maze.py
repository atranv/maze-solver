import time, random
from cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_columns)] for _ in range(self._num_rows)]

        for i in range(self._num_rows):
            for j in range(self._num_columns):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x_pos = self._x1 + i * self._cell_size_x
        y_pos = self._y1 + j * self._cell_size_y
        x2 = x_pos + self._cell_size_x
        y2 = y_pos + self._cell_size_y

        self._cells[i][j].draw(x_pos, y_pos, x2, y2)
        self._animate()

        #call animate

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_rows - 1][self._num_columns - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_columns- 1)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            list_possible = []

            if i - 1 >= 0:
                up = self._cells[i-1][j]
                if up.visited == False:
                    list_possible.append((i-1, j))
            if i + 1 <= self._num_rows - 1:
                down = self._cells[i+1][j]
                if down.visited == False:
                    list_possible.append((i+1, j))
            if j - 1 >= 0:
                left = self._cells[i][j-1]
                if left.visited == False:
                    list_possible.append((i, j-1))
            if j + 1 <= self._num_columns - 1:
                right = self._cells[i][j+1]
                if right.visited == False:
                    list_possible.append((i, j+1))

            if len(list_possible) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction_index = random.randrange(len(list_possible))
                next_index = list_possible[direction_index]

                if next_index[0] == i + 1:  #chosen cell right
                    self._cells[i][j].has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                if next_index[0] == i - 1:  #chosen cell left
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                if next_index[1] == j + 1:  #chosen cell down
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                if next_index[1] == j - 1:  #chosen cell up
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False

                # recursively visit next
                self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

         # if we are at the end cell, we are done!
        if i == self._num_columns - 1 and j == self._num_rows - 1:
            return True
        
       # move left if no wall and hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if no wall and hasn't been visited
        if (
            i < self._num_rows - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_columns - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)


        # we went the wrong way let the previous cell know by returning False
        self._cells[i][j].visited = False
        return False
            
    def solve(self):
        self._solve_r(0, 0)

        


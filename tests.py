import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )
    def test_break_walls_r(self):
        # Initialize a 5*5 maze with seed 0
        maze = Maze(0, 0, 5, 5, 1, 1, seed=0)

        # Call _break_walls_r at the top-left corner
        maze._break_walls_r(0, 0)

        # List to keep track of visited cells
        visited = [[False]*5 for _ in range(5)]
        # List of cells to check, starting with the top-left
        to_check = [(0, 0)]

        # Keep going while there are cells to check
        while to_check:
            curr_i, curr_j = to_check.pop()
            visited[curr_i][curr_j] = True
            # Check each direction for cells that have no walls, add it to to_check list if not visited yet
            if curr_i+1 < 5 and not maze._cells[curr_i][curr_j].has_bottom_wall and not visited[curr_i+1][curr_j]:
                to_check.append((curr_i+1, curr_j))
            # Similar checks for other three directions

        # Now ensure that every cell was visited
        for i in range(5):
            for j in range(5):
                assert visited[i][j]


if __name__ == "__main__":
    unittest.main()


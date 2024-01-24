import unittest
from maze import*

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def _test_maze_remove_start(self):
        num_cols = 15
        num_rows = 10
        win = Window(820,620)
        m2 = Maze(0,0,num_rows,num_cols,10,10,win)

if __name__ == "__main__":
    unittest.main()

from cell import Cell
import random
import time

class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_x = cell_size_x
        self.cell_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_walls_r(0,0)
        self._break_entrance_and_exit()
        self._reset_cells()
        random.seed(seed)
    
    def _create_cells(self):
        self._cells = [[] for i in range(self.num_cols)]
        for i in range(len(self._cells)):
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                self._draw_cell(i,j)
    
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        self._cells[i][j].draw(self.x1+(self.cell_x*i),self.y1+(self.cell_y*j),self.x1+(self.cell_x*(i+1)),self.y1+(self.cell_y*(j+1)))
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if j >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                break
            else:
                direction = random.randint(0,len(to_visit)-1)
                moving = to_visit[direction]
                if moving[0] == i - 1:
                    self._cells[i][j].left_wall = False
                    self._cells[i-1][j].right_wall = False
                if moving[0] == i + 1:
                    self._cells[i][j].right_wall = False
                    self._cells[i+1][j].left_wall = False
                if moving[1] == j - 1:
                    self._cells[i][j].top_wall = False
                    self._cells[i][j-1].bottom_wall = False
                if moving[1] == j + 1:
                    self._cells[i][j].bottom_wall = False
                    self._cells[i][j+1].top_wall = False
                self._break_walls_r(moving[0],moving[1])

    def _reset_cells(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if i > 0 and not self._cells[i][j].top_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)
        if i < self.num_cols - 1 and not self._cells[i][j].right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)
        if j < self.num_rows - 1 and not self._cells[i][j].bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)
        if j > 0 and not self._cells[i][j].left_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)
        return False
    
    def solve(self):
        return self._solve_r(0,0)
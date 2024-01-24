from graphics import Line, Point

class Cell:
    def __init__(self,window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False
    
    def draw(self,x1,y1,x2,y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"#d9d9d9")
        if self.left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"#d9d9d9")
        if self.right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"#d9d9d9")
        if self.bottom_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        self_center = Point((self._x2 + self._x1)/2,(self._y2 + self._y1)/2)
        to_center = Point((to_cell._x2 + to_cell._x1)/2,(to_cell._y2 + to_cell._y1)/2)
        if undo == False:
            self._win.draw_line(Line(self_center,to_center),"red")
        else:
            self._win.draw_line(Line(self_center,to_center),"gray")

class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_x = cell_size_x
        self.cell_y = cell_size_y
        self.win = win
        self._create_cells()
        self._reset_cells()
        random.seed(seed)
    
    def _create_cells(self):
        self._cells = [[] for i in range(self.num_cols)]
        for i in range(len(self._cells)):
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                self._draw_cell(i,j)
        self._break_walls_r(self.num_cols-1,self.num_rows-1)
        self._break_entrance_and_exit()
    
    def _draw_cell(self,i,j):
        self._cells[i][j].draw(self.x1+(self.cell_x*i),self.y1+(self.cell_y*j),self.x1+(self.cell_x*(i+1)),self.y1+(self.cell_y*(j+1)))
        self._animate()

    def _animate(self):
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
            coords = []
            if i-1 >= 0:
                coords.append(self._cells[i-1][j])
            if j-1 >= 0:
                coords.append(self._cells[i][j-1])
            if i+1 <= self.num_cols-1:
                coords.append(self._cells[i+1][j])
            if j+1 <= self.num_rows-1:
                coords.append(self._cells[i][j+1])
            to_visit = []
            for check in coords:
                if check.visited == False:
                    to_visit.append(check)
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                break
            else:
                direction = random.randint(0,len(to_visit)-1)
                if to_visit[direction].get_x1() < self._cells[i][j].get_x1():
                    self._cells[i][j].left_wall = False
                    i -= 1
                    self._cells[i][j].right_wall = False
                if to_visit[direction].get_x1() > self._cells[i][j].get_x1():
                    self._cells[i][j].right_wall = False
                    i += 1
                    self._cells[i][j].left_wall = False
                if to_visit[direction].get_y1() < self._cells[i][j].get_y1():
                    self._cells[i][j].top_wall = False
                    j -= 1
                    self._cells[i][j].bottom_wall = False
                if to_visit[direction].get_y1() > self._cells[i][j].get_y1():
                    self.bottom_wall = False
                    j += 1
                    self._cells[i][j].top_wall = False
                self._break_walls_r(i,j)
    
    def _reset_cells(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
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

def main():
    win = Window(820, 620)
    maze = Maze(10,10,6,8,100,100,win,0)
    maze.solve()
    win.wait_for_close()

main()
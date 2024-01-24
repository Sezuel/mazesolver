from tkinter import Tk, BOTH, Canvas
import time
import random

class Window:
    def __init__(self, winWidth, winHeight):
        self._root = Tk()
        self._root.title(f"Maze {winWidth} x {winHeight}")
        self._canvas = Canvas(height=winHeight,width=winWidth)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._running = True
        while self._running == True:
            self.redraw()
    
    def close(self):
        self._running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self._canvas,fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x,self.start.y,self.end.x,self.end.y,fill=fill_color,width=2)
        canvas.pack()

class Cell:
    def __init__(self,window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = window
        self.visited = False
    
    def get_x1(self):
        return self._x1
    
    def get_x2(self):
        return self._x2
    
    def get_y1(self):
        return self._y1
    
    def get_y2(self):
        return self._y2
    
    def draw(self,x1,y1,x2,y2):
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
        self_center = Point((self._x2 - self._x1)/2,(self._y2 - self._y1)/2)
        to_center = Point((to_cell.get_x2() - to_cell.get_x1())/2,(to_cell.get_y2() - to_cell.get_y1())/2)
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
        random.seed(seed)
    
    def _create_cells(self):
        self._cells = [[] for i in range(self.num_cols)]
        for i in range(len(self._cells)):
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                self._draw_cell(i,j)
        self._break_entrance_and_exit()
        self._break_walls_r(self.num_cols-1,self.num_rows-1)
    
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
            print(f"i={i}, j={j}")
            if i-1 >= 0:
                coords.append(self._cells[i-1][j])
            if j-1 >= 0:
                coords.append(self._cells[i][j-1])
            if i+1 <= self.num_rows:
                coords.append(self._cells[i+1][j])
            if j+1 <= self.num_cols:
                coords.append(self._cells[i][j+1])
            """to_visit = []
            for check in coords:
                if check.visited == False:
                    to_visit.append(check)
            if len(to_visit) == 0:
                self.draw(self._x1,self._y1,self._x2,self._y2)
                break
            else:
                direction = random.randint(0,len(to_visit))
                if to_visit[direction][0] < i:
                    self.left_wall = False
                if to_visit[direction][0] > i:
                    self.right_wall = False
                if to_visit[direction][1] < j:
                    self.top_wall = False
                if to_visit[direction][1] > j:
                    self.bottom_wall = False
                self._break_walls_r(to_visit[direction][0],to_visit[direction][1])"""
        
def main():
    win = Window(820, 620)
    Maze(10,10,6,8,100,100,win,0)
    win.wait_for_close()

main()
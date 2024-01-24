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
        x_mid = (self._x2 + self._x1)/2
        y_mid = (self._y2 + self._y1)/2
        to_x_mid = (to_cell._x2 + to_cell._x1)/2
        to_y_mid = (to_cell._y2 + to_cell._y1)/2
        fill_color = "red"
        if undo:
            fill_color = "gray"
        if self._x1 > to_cell._x1:
            self._win.draw_line(Line(Point(self._x1,y_mid),Point(x_mid,y_mid)),fill_color)
            self._win.draw_line(Line(Point(to_x_mid,to_y_mid),Point(to_cell._x2,to_y_mid)),fill_color)
        if self._x1 < to_cell._x1:
            self._win.draw_line(Line(Point(x_mid,y_mid),Point(self._x2,y_mid)),fill_color)
            self._win.draw_line(Line(Point(to_cell._x1,to_y_mid),Point(to_x_mid,to_y_mid)),fill_color)
        if self._y1 > to_cell._y1:
            self._win.draw_line(Line(Point(x_mid,y_mid),Point(x_mid,self._y1)),fill_color)
            self._win.draw_line(Line(Point(to_x_mid,to_cell._y2),Point(to_x_mid,to_y_mid)),fill_color)
        if self._y1 < to_cell._y1:
            self._win.draw_line(Line(Point(x_mid,y_mid),Point(x_mid,self._y2)),fill_color)
            self._win.draw_line(Line(Point(to_x_mid,to_y_mid),Point(to_x_mid,to_cell._y1)),fill_color)
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, winWidth, winHeight):
        self._root = Tk()
        self._root.title(f"Maze {winWidth} x {winHeight}")
        self._canvas = Canvas(height=winHeight,width=winWidth)
        self._canvas.pack(fill=BOTH, expand=1)
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
    
    def draw_line(self, line, fill_color="black"):
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
        canvas.pack(fill=BOTH, expand=1)
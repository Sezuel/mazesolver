def main():
    win = Window(820, 620)
    maze = Maze(10,10,6,8,100,100,win,0)
    maze.solve()
    win.wait_for_close()

main()
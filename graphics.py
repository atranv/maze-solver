from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()   # This creates a root widget
        self.__root.title("Al's Amazing Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height) # this creates a Canvas
        self.__canvas.pack(fill=BOTH, expand=1)
        self.window_is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self): 
        self.__root.update_idletasks() 
        self.__root.update()

    def wait_for_close(self):
       self.window_is_running = True
       while self.window_is_running:
           self.redraw()
       print("window closed")
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.window_is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


from tkinter import Tk, BOTH, Canvas

class Window:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()  # Notice the double underscore for private members
        self.__root.title('Maze Game')  # You can use any title
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # This is missing in yours
        
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        
        self.__running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        self.__running = True
        while self.__running:
             self.redraw()



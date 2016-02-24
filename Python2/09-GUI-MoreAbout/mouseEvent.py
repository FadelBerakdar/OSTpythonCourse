from tkinter import *


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=TRUE)
        self.create_widgets()


    def create_widgets(self):
        self.canvas = Canvas(self, width=640, height=480, background="gray")
        self.canvas.bind("<ButtonPress>", self.mouse_press)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.pack()

    def draw(self, event):
        global prev
        self.canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
        prev = event


    def mouse_press(self, event):
        global prev
        prev = event

        print("type: {}".format(event.type))
        print("widget: {}".format(event.widget))
        print("num: {}".format(event.num))
        print("X: {}".format(event.x))
        print("Y: {}".format(event.y))
        print("X_Root: {}".format(event.x_root))
        print("Y_Root: {}".format(event.y_root))


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()

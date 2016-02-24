#!/usr/bin/env python3
#                        GUI-based module
#                            finalWay2.py
# By: Fadel Berakdar
# Date: 27/7/2015


"""
Here are your instructions:


Write a GUI-based program to build a window layout as shown below.
When the frame is resized, the buttons should stay the same height and
expand sideways. Frame 1 and Frame 2 should always be the same height and
width as each other, and Frame 3 should be half as wide again as they
are (i.e. 150% wider, as shown below).  Labeling each Frame is optional /
good exercise.
+---------------------+--------------------------------+
|                     |                                |
|                     |                                |
|                     |                                |
|      Frame 1        |                                |
|                     |                                |
|                     |                                |
|                     |                                |
+---------------------+               Frame 3          |
|                     |                                |
|                     |                                |
|                     |                                |
|     Frame 2         |                                |
|                     |                                |
|                     |                                |
+----------+----------+----------+----------+----------+
| Button 1 | Button 2 | Button 3 | Button 4 | Button 5 |
+----------+----------+----------+----------+----------+
Your Comment:
Hi Pat,

here is my project for GUI Layout... I hope its perfect :)
have a nice weekend.

Items Handed In
Open s Handed In

Overall Comments:
Hi Fadel,

Very slick!

You have done a terrific job on this assignment. Your GUI has great
"curb appeal" and maintains its geometry under all conditions.

Here's some advice for s 3:

-It's actually fine to use a pack and grid manager together as long as they
aren't put in control of the same widgets.  So packing a Label into a Frame
that was stretched to a grid is straightforward.

-Grids take more work in that each row and column should be configured.
You actually got self.rowconfigure(0, weight=1) twice, but because  default
weight is 0,  our button row 2 stays thin and trim, as it should.

-I recommend with experimenting with a pack manager for placement of widgets
in Frame3. Those widgets would be Entry and Text widgets respectively. The
first should stay thin and trim across the bottom or top while the Text
object should balloon to fill the rest of the frame, no real estate wasted.

For your inspection and viewing pleasure, here's an alternative solution to
this objective:

"""
from tkinter import *


ALL = W+E+N+S


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1, minsize=500)
        self.master.columnconfigure(0, weight=1, minsize=700)
        self.grid(sticky=ALL)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        frame_1 = Frame(self, width=100, height=200, border=10, relief=RIDGE,
                        bg="red")
        frame_1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)

        frame_2 = Frame(self, height=200, border=10, relief=RIDGE,  bg="blue")
        frame_2.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)

        frame_3 = Frame(self, border=10, relief=RIDGE, bg="green")
        frame_3.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=ALL)

        for r in range(5):
            self.columnconfigure(r, weight=1)
            Button(self, text="Button {0}".format(r+1)).grid(row=4, column=r,
                                                             sticky=E+W)

        label_1 = Label(frame_1, text="FRAME 1", bg="red", fg="white")
        label_1.pack(fill="both", expand=True)

        label_2 = Label(frame_2, text="FRAME 2", bg="blue", fg="white")
        label_2.pack(fill="both", expand=True)

        label_3 = Label(frame_3, text="FRAME 3", bg="green", fg="white")
        label_3.pack(fill="both", expand=True)


root = Tk()
app = Application(master=root)
app.mainloop()




#!/usr/bin/env python3
#                        GUI-based module
#                            final.py
# By: Fadel Berakdar
# Date: 27/7/2015
"""
Write a GUI-based program to build a window layout as shown below.
When the frame is resized, the buttons should stay the same height and expand
sideways. Frame 1 and Frame 2 should always be the same height and width as
each other, and Frame 3 should be half as wide again as they are
(i.e. 150% wider, as shown below).  Labeling each Frame is optional / good
exercise.
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
"""

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N+S+W+E)

        for r in range(6):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row    {0}".format(r)).grid(row=r, column=0,
                                                           sticky=N+S+W+E)

        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=6, column=c,
                                                             sticky=E+W)
        # Frame1:
        self.frame1 = LabelFrame(self, text="Frame 1", relief=SOLID)
        self.frame1.grid(row=0, column=0, rowspan=3, columnspan=2,
                         sticky=N+S+W+E, padx=1, pady=1)
        # Frame2:
        self.frame2 = LabelFrame(self, text="Frame 2", relief=SOLID)
        self.frame2.grid(row=3, column=0, rowspan=3, columnspan=2,
                         sticky=N+S+W+E, padx=1, pady=1)
        # Frame3:
        self.frame3 = LabelFrame(self, text="Frame 3", relief=SOLID)
        self.frame3.grid(row=0, column=2, rowspan=6, columnspan=3,
                         sticky=N+S+W+E, padx=4, pady=1)

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()

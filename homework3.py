from tkinter import *
from random import *
root = Tk()
c = Canvas(root, width=1300, height=800, bg="#2f343f")
c.pack()
def stvorec(x, y):
    c.create_rectangle(x,y,x+200,y-60, fill="#123456")
    c.create_polygon(x, y-60, x+200, y-60, x+150, y-100, x+30, y-100, fill="#654321")
stvorec(150,750)
stvorec(650, 750)
def plot(x,y):
    for i in range(3, 15):
        c.create_line(x+170 + i*20, y-30, x+170+i*20,y,width=5, fill="white")
    c.create_line(x+220, y-20, x+460, y-20, width=5, fill="white")    
plot(150,750)
plot(150, 780)
def strom(x,y):
    c.create_rectangle(x,y, x+70, y+200, fill="#964B00")
    c.create_polygon(x-30, y, x+100, y, x+35,y-40, fill="green")
    c.create_polygon(x-30, y-30, x+100, y-30, x+35,y-70, fill="green")
    c.create_polygon(x-30, y-60, x+100, y-60, x+35,y-100, fill="green")
    c.create_polygon(x-30, y-90, x+100, y-90, x+35,y-130, fill="green")
strom(600, 300)

root.mainloop()
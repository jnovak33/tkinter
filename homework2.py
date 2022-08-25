from tkinter import *
from random import *
root = Tk()
c = Canvas(root, width=1300, height=800, bg="#2f343f")
c.pack()
for i in range(6):
	radius=25+i*20 #upravuje sa zaoblenie
	x1 = 75 + i*200
	y1 = 1 
	x2 = 175 + i*200
	y2 = 1
	if i%2 == 1:
		y1 = 300+i*40
		y2 = 500+i*40
	else:
		y1 = 300-i*40
		y2 = 500-i*40	;
	points = [x1+radius, y1,
         	x2-radius, y1,
        	x2, y1,
         	x2, y1+radius,
         	x2, y2-radius,
         	x2, y2,
         	x2-radius, y2,
         	x1+radius, y2,
         	x1, y2,
         	x1, y2-radius,
         	x1, y1+radius,
         	x1, y1]
			# v tkinteri sa "oficialne" neda vytvorit obdlznik zo zaoblenymi rohmi, tak som si tie rohy
			# musel zaoblit sam... :)
	colour1 = choice(("#bf616a", "#d08770", "#ebcb8b", "#a3be8c", "#b48ead"))
	colour2 = choice(("#bf616a", "#d08770", "#ebcb8b", "#a3be8c", "#b48ead"))	
	while colour1 == colour2:
			colour1 = colour1 = choice(("#bf616a", "#d08770", "#ebcb8b", "#a3be8c", "#b48ead")) #aby neboli 2 rovnake farby
	c.create_polygon(points, fill = colour2, smooth=True)
	c.create_text((x1+x2)/2, (y1+y2)/2, text=i+1, fill=colour1, font="Roboto 20")
c.create_line(0,0,1300,0, width=20, fill="#4c566a")
c.create_line(0,801,1300,800, width=20, fill="#4c566a")
c.create_line(0,0,0,800, width=20, fill="#4c566a")
c.create_line(1301,0,1300,800, width=20, fill="#4c566a")
c.create_polygon(0,0,0,40,40,0, fill="#4c566a")
c.create_polygon(0,800,40,800,0,760, fill="#4c566a")
c.create_polygon(1300,800,1300,760,1260,800, fill="#4c566a")
c.create_polygon(1300,0,1260,0,1300,40, fill="#4c566a")
root.mainloop()
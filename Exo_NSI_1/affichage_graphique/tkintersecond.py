
from tkinter import *

def indiquer_pos(event):
    etiquette.config(text=str(event.x)+','+str(event.y))

def creer_point(e):
    zone.create_line(e.x-2,e.y-2,e.x+2,e.y+2,width =2)
    zone.create_line(e.x-2,e.y+2,e.x+2,e.y-2,width =2)
    

gui = Tk()

gui.geometry("500x500+300+300")

zone = Canvas(gui,width=400,height=400,bg="white")
zone.bind("<Motion>",indiquer_pos)
zone.bind("<Button>",creer_point)
zone.pack()

etiquette = Label(gui,text='',font=("arial" ,25),fg="red")
etiquette.pack()


gui.mainloop

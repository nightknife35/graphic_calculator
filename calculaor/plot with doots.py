from tkinter import *
import math


n="2-1*x=2*x-7"
gg=250

a=0.05
b=-0.6
c=36
a2=0
b2=1.5
c2=50
#---------------------------------------------------------functions-------------------------------------------------------------------------------

def f(x,a,b,c):

    return a*x**2+b*x+c


    
#------------------------------------------------------------window--------------------------------------------------------------------------------


w=Tk()
w.title("loooooooool")
w.configure(bg="#444444")
w.geometry(f"{gg*2}x{gg*2}")

my_canvas=Canvas(w,width=gg*2,height=gg*2,bg='white')
my_canvas.pack()

my_canvas.create_line(0,gg*1,gg*2,gg*1,fill='red')
my_canvas.create_line(gg*1,0,gg*1,gg*2,fill='red')




for i in range(gg*(-1),1*gg):
    p=0.01*i
    my_canvas.create_rectangle(i+gg,gg-f(i,a,b,c),gg+i,gg-f(i,a,b,c),fill='green')

for i in range(gg*(-1),gg*1):
    p=0.01*i
    my_canvas.create_rectangle(gg+i,gg-f(i,a2,b2,c2),gg+i,gg-f(i,a2,b2,c2),fill='green')






w.mainloop()

from tkinter import *
import math

aa=input('a=? in ax²+bx+c : ')
bb=input('b=? in ax²+bx+c : ')
cc=input('c=? in ax²+bx+c : ')
dimentions=int(input('Diamentions (suggested 500) : '))

def f(x):
    
    return float(aa)*x**2+float(bb)*x+float(cc)

w=Tk()
w.title("loooooooool")
w.configure(bg="white")
w.geometry(f"{dimentions}x{dimentions}")

c=Canvas(w,width=dimentions,height=dimentions,bg='white')
c.pack(fill=BOTH, expand=1)

A=[]
B=[]
C=[]
D=[]
balance_factor=dimentions/2
l=1000 #l is basicall a number that tells u up to whatt height u want your function to go
#       u want it too be very high (like up to infinity) but u doont like lag so up too 1000 should be good

c.create_line(0,balance_factor,dimentions,balance_factor)
c.create_line(balance_factor,0,balance_factor,dimentions)


for i in range (0,l):

    posittivei=(i+balance_factor,balance_factor-f(i))
    neggattivei=(balance_factor-i,balance_factor-f(-i))
    A.append(posittivei)
    C.append(neggattivei)

for i in range (1,l+1):

    posittivei=(i+balance_factor,balance_factor-f(i))
    neggattivei=(balance_factor-i,balance_factor-f(-i))
    B.append(posittivei)
    D.append(neggattivei)

for i in range (0,l):

    c.create_line(A[i],B[i],fill='red')
    c.create_line(C[i],D[i],fill='red')


w.mainloop()
#my_canvas.create_arc
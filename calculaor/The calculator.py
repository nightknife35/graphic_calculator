from tkinter import *
import math
#https://www.symbolab.com/solver/equation-calculator
#---------------------------------------------------------functions-------------------------------------------------------------------------------

def center():

    n=e.get()
    tb.insert(INSERT,n)
    tb.insert(INSERT,'\n')

    def breakdown(n):# takes n and gives n4
            

            n2=n+"*/sincostanarcsarccarct!|√^ln²}sqrt{,log{"

            A=n2.split("+")
            A2=" +".join(A)
            B=A2.split("-")
            B2=" -".join(B)   
            C=B2.split("*")
            C2=" * ".join(C)
            D=C2.split("/")
            D2=" / ".join(D)
            E=D2.split("sin")
            E2=" sin ".join(E)
            F=E2.split("cos")
            F2=" cos ".join(F)
            G=F2.split("tan")
            G2=" tan ".join(G)
            H=G2.split("arcs")
            H2=" arcs ".join(H)
            I=H2.split("arcc")
            I2=" arcc ".join(I)
            J=I2.split("arct")
            J2=" arct ".join(J)
            K=J2.split("!")#factorial()
            K2=" ! ".join(K)
            L=K2.split("|")
            L2=" | ".join(L)
            M=L2.split("√")
            M2=" √ ".join(M)
            N=M2.split("^")
            N2=" ^ ".join(N)
            O=N2.split("ln")#log(a,Base)
            O2=" ln ".join(O)
            P=O2.split("(")
            P2=" ( ".join(P)
            Q=P2.split(")")
            Q2=" ) ".join(Q)
            R=Q2.split("²")
            R2=" ² ".join(R)
            S=R2.split(",")
            S2=" , ".join(S)
            T=S2.split("}")
            T2=" } ".join(T)
            U=T2.split("log{")
            U2=" log{ ".join(U)
            V=U2.split("sqrt{")
            V2=" sqrt{ ".join(V)
            
            
            
            
            n3=V2.split()
            
            n4=n3[:-18]
            
            return n4 


    def simple_arithmiticks(n):
        #if e.get()contains , direct to equasion solving. if it contains only x direct acordingly ect..

        def opperations(n):#takes n and gives n4

            n4=breakdown(n)
            print(n4)

            while "e" in n4:
                n4[n4.index("e")]=math.e
            while "π" in n4:
                n4[n4.index("π")]=math.pi


            while "sin" in n4:             

                result=str(float(math.sin(float(n4[n4.index("sin")+1]))))
                del n4[n4.index("sin")+1]  
                n4[n4.index("sin")]=result

            while "cos" in n4:             

                result=str(float(math.cos(float(n4[n4.index("cos")+1]))))
                del n4[n4.index("cos")+1]
                n4[n4.index("cos")]=result

            while "tan" in n4:             

                result=str(float(math.tan(float(n4[n4.index("tan")+1]))))
                del n4[n4.index("tan")+1]
                n4[n4.index("tan")]=result

            while "arcs" in n4:             

                result=str(float(math.asin(float(n4[n4.index("arcs")+1]))))
                del n4[n4.index("arcs")+1]
                n4[n4.index("arcs")]=result

            while "arcc" in n4:             

                result=str(float(math.acos(float(n4[n4.index("arcc")+1]))))
                del n4[n4.index("arcc")+1]
                n4[n4.index("arcc")]=result

            while "arct" in n4:             

                result=str(float(math.atan(float(n4[n4.index("arct")+1]))))
                del n4[n4.index("arct")+1]
                n4[n4.index("arct")]=result



            while "!" in n4:             

                result=str(float(math.factorial(int(n4[n4.index("!")-1]))))
                del n4[n4.index("!")-1]
                n4[n4.index("!")]=result


            while "ln" in n4:             

                result=str(float(math.log(float(n4[n4.index("ln")+1]),math.e)))
                del n4[n4.index("ln")+1]
                n4[n4.index("ln")]=result

            while "log{" in n4:             
                
                l=n4.index("log{")
                del n4[n4.index("}",l+1)]
                result=str(math.log(float(n4[n4.index("log{")+3]),float(n4[n4.index("log{")+1])))
                del n4[n4.index("log{")+3]
                del n4[n4.index("log{")+2]
                del n4[n4.index("log{")+1]
                n4[n4.index("log{")]=result


            while "√" in n4:             

                result=str(float(math.sqrt(float(n4[n4.index("√")+1]))))
                del n4[n4.index("√")+1]
                n4[n4.index("√")]=result

            while "sqrt{" in n4:             
                
                l=n4.index("sqrt{")
                del n4[n4.index("}",l+1)]
                result=float(n4[n4.index("sqrt{")+1])**(1.0/float(n4[n4.index("sqrt{")+3]))
                del n4[n4.index("sqrt{")+3]
                del n4[n4.index("sqrt{")+2]
                del n4[n4.index("sqrt{")+1]
                n4[n4.index("sqrt{")]=result
            

            while "^" in n4:             

                if float(n4[n4.index("^")-1])<0 and float(n4[n4.index("^")+1])%2==0:

                    result=str(float(n4[n4.index("^")-1])**float(n4[n4.index("^")+1]))
                    del n4[n4.index("^")+1]
                    del n4[n4.index("^")-1]
                    n4[n4.index("^")]=str(-float(result))
                    tb.insert(INSERT,n4)
                    tb.insert(INSERT,'\n')
                else:
                    result=str(float(n4[n4.index("^")-1])**float(n4[n4.index("^")+1]))
                    del n4[n4.index("^")+1]
                    del n4[n4.index("^")-1]
                    n4[n4.index("^")]=result
                    tb.insert(INSERT,n4)
                    tb.insert(INSERT,'\n')


            while "²" in n4:             

                result=str(float(float(n4[n4.index("²")-1])**2))
                n4[n4.index("²")-1]=result
                del n4[n4.index("²")]
                


            while "/" in n4:             
                result=str(float(n4[n4.index("/")-1])/float(n4[n4.index("/")+1]))
                del n4[n4.index("/")+1]
                del n4[n4.index("/")-1]
                n4[n4.index("/")]=result
                tb.insert(INSERT,n4)
                tb.insert(INSERT,'\n')
            
            while "*" in n4:             
                result=str(float(n4[n4.index("*")-1])*float(n4[n4.index("*")+1]))
                del n4[n4.index("*")+1]
                del n4[n4.index("*")-1]
                n4[n4.index("*")]=result
                tb.insert(INSERT,n4)
                tb.insert(INSERT,'\n')
                

            while len(n4)>1:
                
                if n4[0]=="-":
                    del n4[0]
                    n4[0]=-float(n4[0])
                elif n4[1]=="-":
                    del n4[1]
                    n4[1]=-float(n4[1])
                elif n4[0]=="+":
                    del n4[0]
                elif n4[1]=="+":
                    del n4[1] 
                elif n4[0]=='':
                    del n4[0] 
                else:         
                    n4[0]=float(n4[0])+float(n4[1])
                    del n4[1]




            return n4

        def No_Parenthesis(n):#takes n and gives n
            
            n4=breakdown(n)
            
            if n4.count("(")==n4.count(")"):
            

                
                while "|" in n4:             

                    index1=n4.index("|")
                    index2=n4.index("|",index1+1)
                    n0=n4[0:index1]
                    n3=n4[index2+1:]
                    n2=n4[index1+1:index2]
                    n2="".join(n2)
                    n2=opperations(n2)
                    n2=abs(float(n2[0]))
                    n2=str(n2)
                    print(n2)
                    n3.insert(0,n2)
                    n0="#".join(n0)
                    n3.insert(0,n0)
                    n3="#".join(n3)
                    n4=n3.split("#")

                    tb.insert(INSERT,n4)
                    tb.insert(INSERT,'\n')





                while "(" in n4:
                    
                    n2=n4.index(")")
                    n4.reverse()
                    nn1=n4.index("(",len(n4)-n2)
                    n4.reverse()
                    n1=len(n4)-nn1-1
                    n0=n4[0:n1]
                    n3=n4[n2+1:]
                    n2=n4[n1+1:n2]
                    n2="".join(n2)
                    n2=opperations(n2)
                    n2=str(n2[0])
                    n3.insert(0,n2)
                    n0="#".join(n0)
                    n3.insert(0,n0)
                    n3="#".join(n3)
                    n4=n3.split("#")
                    
                    tb.insert(INSERT,n4)
                    tb.insert(INSERT,'\n')   #loops n4

                
                n="".join(n4)
                return n           #gives n

        n=No_Parenthesis(n)

        n4=opperations(n)

        print(n4)
        

        tb.insert(INSERT,n4)
        tb.insert(INSERT,'\n')
        e.delete(0,END)

    def solve_for_x(n):
        
        A=[]
        n4=n.split("x")
        print(n4)
        i=0
        while i<len(n4):

            A.append(n4[i])
            A.append("p")
            i=i+1

        print(A)
        del A[len(A)-1]
        for i in A:
            try:
                del A[A.index('')]
            except ValueError:
                pass
        print(A)








        #for i in ...
        pass

    def plot():
        

        my_canvas=Canvas(w,width=500,height=500,bg='white')
        my_canvas.pack()

        my_canvas.create_line(0,250,500,250,fill='red')
        my_canvas.create_line(250,0,250,500,fill='red')

        #                  v

        for i in range(-100,100):
            p=i
            my_canvas.create_rectangle(250+p,250-p,250+p,250-p,fill='green')

        #                                ^     ^     ^    ^





    def equasion_solving():
        pass
    

    if  n[0]=="p" and n[1]=="l" and n[2]=="o" and n[3]=="t":
        
        plot()
    elif n[0]=="s" and n[1]=="o" and n[2]=="l" and n[3]=="v" and n[4]=="e" :
        
        solve_for_x()
    elif n[0]=="e" and n[1]=="q" and n[2]=="u" and n[3]=="a" and n[4]=="t" and n[5]=="e" :
        
        equasion_solving()

    else:
        
        simple_arithmiticks(n)


def clicked(n):
    a=e.get()
    e.delete(0,END)
    e.insert(0,n)
    e.insert(0,a)    

#------------------------------------------------------------window--------------------------------------------------------------------------------


w=Tk()
w.title("loooooooool")
w.geometry('1000x500')
w.state('zoomed')
w.configure(bg="#444444")

#----------------------------------------------------------text box-------------------------------------------------------------------------------
f=Frame(w)
f.place(x=0,y=400)

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)

tb=Text(f,width=45,yscrollcommand=s.set)
tb.pack()
s.config(command=tb.yview)
#------------------------------------------------------------Entry---------------------------------------------------------------------------------


e=Entry(w,width=50,font=("",17))#.place()            <--- this wouldnt work
#e.place needs to be in a diferent line for some reason for it to work
e.place(x=400,y=50)




#---------------------------------------creating / diamentions of buttons / placement-------------------------------------------------------------
p=70

b1=Button(w,text="1",pady=9,padx=27,command= lambda:clicked(1)).place(x=283,y=144)
b2=Button(w,text="2",pady=9,padx=27,command= lambda:clicked(2)).place(x=353,y=144)
b3=Button(w,text="3",pady=9,padx=27,command= lambda:clicked(3)).place(x=423,y=144)
b4=Button(w,text="4",pady=9,padx=27,command= lambda:clicked(4)).place(x=493,y=144)
b5=Button(w,text="5",pady=9,padx=30,command= lambda:clicked(5)).place(x=563,y=144)
b6=Button(w,text="6",pady=9,padx=27,command= lambda:clicked(6)).place(x=633,y=144)
b7=Button(w,text="7",pady=9,padx=30,command= lambda:clicked(7)).place(x=703,y=144)
b8=Button(w,text="8",pady=9,padx=27,command= lambda:clicked(8)).place(x=773,y=144)
b9=Button(w,text="9",pady=9,padx=27,command= lambda:clicked(9)).place(x=843,y=144)
b0=Button(w,text="0",pady=9,padx=27,command= lambda:clicked(0)).place(x=913,y=144)
bπ=Button(w,text="π",pady=9,padx=27,command= lambda:clicked("π")).place(x=983,y=144)
be=Button(w,text="e",pady=9,padx=27,command= lambda:clicked("e")).place(x=1053,y=144)
bclose=Button(w,text="(",pady=8,padx=29,command= lambda:clicked("(")).place(x=1123,y=144)
bopen=Button(w,text=")",pady=8,padx=30,command= lambda:clicked(")")).place(x=1193,y=144)


bplus=Button(w,text="+",pady=8,padx=27,command= lambda:clicked("+")).place(x=75+p,y=104)
bminus=Button(w,text="-",pady=8,padx=27,command= lambda:clicked("-")).place(x=145+p,y=104)
btimes=Button(w,text="*",pady=8,padx=27,command= lambda:clicked("*")).place(x=215+p,y=104)
bdivide=Button(w,text="/",pady=8,padx=27,command= lambda:clicked("/")).place(x=285+p,y=104)
broot=Button(w,text="√",pady=8,padx=27,command= lambda:clicked("√")).place(x=355+p,y=104)
b2root=Button(w,text="*√*",pady=8,padx=22,command= lambda:clicked("sqrt{number,power}")).place(x=425+p,y=104)
bpower=Button(w,text="^",pady=8,padx=27,command= lambda:clicked("^")).place(x=495+p,y=104)
bpower2=Button(w,text="x²",pady=8,padx=27,command= lambda:clicked("²")).place(x=565+p,y=104)
blog=Button(w,text="log",pady=8,padx=22,command= lambda:clicked("log{bace,number}")).place(x=635+p,y=104)
bln=Button(w,text="ln",pady=8,padx=27,command= lambda:clicked("ln")).place(x=705+p,y=104)
bfactorial=Button(w,text="!",pady=8,padx=27,command= lambda:clicked("!")).place(x=775+p,y=104)
babsolute=Button(w,text="| |",pady=8,padx=27,command= lambda:clicked("|")).place(x=845+p,y=104)
bsin=Button(w,text="sin()",pady=8,padx=18,command= lambda:clicked("sin(")).place(x=915+p,y=104)
bcos=Button(w,text="cos()",pady=8,padx=18,command= lambda:clicked("cos(")).place(x=985+p,y=104)
btan=Button(w,text="tan()",pady=8,padx=18,command= lambda:clicked("tan(")).place(x=1055+p,y=104)
barcsin=Button(w,text="sin-1()",pady=8,padx=15,command= lambda:clicked("arcs(")).place(x=1125+p,y=104)
barccos=Button(w,text="cos-1()",pady=8,padx=15,command= lambda:clicked("arcc(")).place(x=1195+p,y=104)
barctan=Button(w,text="tan-1()",pady=8,padx=15,command= lambda:clicked("arct(")).place(x=1265+p,y=104)
bcomma=Button(w,text=".",pady=9,padx=27,command= lambda:clicked(".")).place(x=1265,y=144)



benter=Button(w,text="Go 🙂",pady=8,padx=15,command=center).place(x=1100,y=50)


w.mainloop()

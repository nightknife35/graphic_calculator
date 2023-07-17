import math
n="3-x=-6+2*x"
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
                    print(n4)
                else:
                    result=str(float(n4[n4.index("^")-1])**float(n4[n4.index("^")+1]))
                    del n4[n4.index("^")+1]
                    del n4[n4.index("^")-1]
                    n4[n4.index("^")]=result
                    print(n4)

            while "²" in n4:             

                result=str(float(float(n4[n4.index("²")-1])**2))
                n4[n4.index("²")-1]=result
                del n4[n4.index("²")]
                


            while "/" in n4:             
                result=str(float(n4[n4.index("/")-1])/float(n4[n4.index("/")+1]))
                del n4[n4.index("/")+1]
                del n4[n4.index("/")-1]
                n4[n4.index("/")]=result
                print(n4)
            
            while "*" in n4:             
                result=str(float(n4[n4.index("*")-1])*float(n4[n4.index("*")+1]))
                del n4[n4.index("*")+1]
                del n4[n4.index("*")-1]
                n4[n4.index("*")]=result
                print(n4)
                

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

                    print(n4)





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
                    
                    print(n4)   #loops n4

                
                n="".join(n4)
                return n           #gives n



p=1
def solve_4_x(n,p):

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
    n4=A
    print(n4)



    for i in n4:
        try:
            n4[n4.index('p')]=str(p)
        except ValueError:
            pass
    n="".join(n4)
    print(n)
    n4=n.split("=")
    print(n4)
    global n0
    n0=opperations(n4[0])
    global n1
    n1=opperations(n4[1])

solve_4_x(n,p)
n0=n0
n1=n1

while n0!=n1:

    if n0<n1:
        p=p+1
    
    solve_4_x(n,p)




































print('x is equal to '+ str(p))








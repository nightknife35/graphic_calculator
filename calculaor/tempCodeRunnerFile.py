#----------------------------------------------------------text box-------------------------------------------------------------------------------
f=Frame(w)
f.place(x=0,y=400)

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)

tb=Text(f,width=45,yscrollcommand=s.set)
tb.pack()
s.config(command=tb.yview)
#-----------------------------------
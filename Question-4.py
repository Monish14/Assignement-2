from tkinter import *




root = Tk()

text1 = Label(master = root, text = 'Loan Amount:')
text1.grid(row=0,column=0) # widget placed against top boundary of master (default)
#text1.pack(side=LEFT)

field1=Entry(root)
field1.grid(row=0,column=1)
#field1.pack(side=LEFT)
#field1.place(X=50,Y=50)

text2 = Label(master = root, text = 'Intrest Rate:')
text2.grid(row=1,column=0)# widget placed against top boundary of master (default)
#text2.pack(side=LEFT)

field2=Entry(root)
field2.grid(row=1,column=1)
#field2.pack(side=LEFT)

text3 = Label(master = root, text = 'Loan Terms:')
text3.grid(row=2,column=0) # widget placed against top boundary of master (default)
#text3.pack(side=LEFT)

field3=Entry(root)
field3.grid(row=2,column=1)
#field3.pack(side=LEFT)

def compute():
    global field1,field2,field3
    amt=int(field1.get())
    rate=float(field2.get())
    time=float(field3.get())

    mor=(amt*rate*time)/100
    field4.insert(0,mor)

button = Button(root, text='Compute Mortgage', command=compute) 
button.grid(row=3, column=0)
#button.pack(side=LEFT)

field4=Entry(root)
field4.grid(row=3,column=1)
#field4.pack(side=LEFT)

box = Frame(root) 
#box.pack(side=RIGHT)
#box.place(x=100,y=100)
labels = [['1', '2', '3'],     
          ['4', '5', '6'],     
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):
    for c in range(3):
        # create label for row r and column c
        label = Label(root,
                      relief=RAISED,      
                      padx=10,           
                      text=labels[r][c])
        # place label in row r and column c
        label.grid(row=c,column=r)
        


root.mainloop()

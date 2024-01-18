#!/usr/bin/env python
# coding: utf-8

# In[38]:


def mapping():
    print('welcome')
    print('roshani patil')
    print ('at post ghansoli navi mumbai')


def area():
    #area of room
    print('calculate the area of room')

    width=float(input('enter your width'))
    length=float(input('enter your length'))
    area=width * length
    print('area of calculation',area)

def acre():
    #acre 
    print('calaculate the farmer field')
    sqft_per_acre=43560
    width=float(input('enter your width'))
    length=float(input('enter your length'))
    acre=width * length /sqft_per_acre
    print('area of field',acre,"acres")

def bottle_deposits():
    #welcome
    print('welcome to bottle deposits')
    less=0.10
    more=0.25
    a1=int(input('how many container in 1 liter or less do you have'))
    a2=int(input('how many container in 1 liter or more do you have'))
    refund=a1*less+a2*more
    print('final result',round(refund,2))

def tax_tip():  
    #tax and tip
    print('welcome to tax and tip program')
    tax=0.05
    tip=0.18

def cost():
    # display
    cost=int(input('enter the amount '))

    tax1=cost*tax
    tip1=cost*tip

    total=cost+tax1+tip1
    print(f'the meal amount of tax {tax1}\n the meal amount of tip {tip1}\n and total amount is {round(total,2)}')


def sum1():
    #welcome
    print('welcome to sum of prog')
    n=int(input('enter the number'))
    sum1=(n)*(n+1)/2
    print('the result is',sum1)

def widget_Gizmos():    
    #welcome
    print('welcome to widget and Gizmos program')
    # display parameter
    widget=75
    Gizmos=112

    a1=int(input('enter the widget number'))
    a2=int(input('enter the Gizmos number'))

    widget1=a1*widget
    Gizmos1=a2*Gizmos

    total=result+widget1+Gizmos1
    print('the final result',total,"gm")


def comp_intrest():
    #welcome
    initial_deposite=float(input('enter the deposite amount'))
    interest_rate=4.0
    y=3
    #calculate and display

    for y in range(1,y+1):
        interst=initial_deposite*interest_rate/100
        #add interest two number
        initial_deposite+=interst
        print('after year',y,'the saving amount is',round(initial_deposite,2)) 

def even_odd():      
    # welcome
    print('welcome to even or odd prog')
    a1=int(input('enter the number'))
    if (a1%2)==0:
        print( 'even')
    else:
        print('odd')
        
def vowel_constant():
    #welcome
    print('welcome to vowel and constant program')
    a1=input('enter the letters')

    if a1=='i'or a1=='e'or a1=='o'or a1=='u'or a1=='a':
        print('vowel')
    else:
        print('constant')

def traingle():
    #welcome
    print('welcome to trangle program')
    len1=int(input('entet the first length'))
    len2=int(input('entet the first  length'))
    len3=int(input('entet the first  length'))

    if len1==len2==len3:
        print('the side is equilateral')
    elif len1==len2!=len3 or len1!=len2==len3:
        print('the side is isosceles')
    else: 
        print('the triangle is scalene')



# In[ ]:


#importing thinter library
import tkinter as tk

#reating a main window
window=tk.Tk()

#change title
window.title('Roshani patil')

#size
window.geometry('750x550')

#Label
tk.Label(window,text='Python project',font=('Hevetica',21),bg='black',fg='red').place(x=270,y=30)
tk.Label(window,text='made by:Roshani patil',font=('Hevetica',21,'bold'),bg='yellow',fg='red').place(x=220,y=100)

#button
tk.Button(window,text='mapping',command=mapping).place(x=50,y=150,width=200,height=25)
tk.Button(window,text='area',command=area).place(x=270,y=150,width=200,height=25)
tk.Button(window,text='acre',command=acre).place(x=490,y=150,width=200,height=25)
tk.Button(window,text='bottle_deposits',command=bottle_deposits).place(x=50,y=250,width=200,height=25)
tk.Button(window,text=' cost',command= cost).place(x=270,y=250,width=200,height=25)
tk.Button(window,text=' sum1',command= sum1).place(x=490,y=250,width=200,height=25)
tk.Button(window,text=' widget_Gizmos',command=widget_Gizmos).place(x=50,y=350,width=200,height=25)
tk.Button(window,text='comp_intrest',command=comp_intrest).place(x=270,y=350,width=200,height=25)
tk.Button(window,text='even_odd',command=even_odd).place(x=490,y=350,width=200,height=25)
tk.Button(window,text='vowel_constant',command=vowel_constant).place(x=50,y=450,width=200,height=25)
tk.Button(window,text='traingle',command=traingle).place(x=270,y=450,width=200,height=25)


window.mainloop()


# In[ ]:





#import library
from tkinter import *
import random

#initialize window
root = Tk()
root.geometry('400x400')
#root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg ='LightPink2')

#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'LightPink2',fg='Black').pack()

##user choice
user_take = IntVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = 'LightPink2').place(x = 20,y=70)
Radiobutton(root, text="Rock",padx=5,activebackground='LightPink2' ,variable=user_take,value=1,bg='LightPink2',font='arial 15 bold').place(x=20,y=110)
Radiobutton(root, text="Paper",padx=5, variable=user_take,value=2,bg='LightPink2', activebackground='LightPink2',font='arial 15 bold').place(x=110,y=110)
Radiobutton(root, text="scissors",padx=5, variable=user_take,value=3,bg='LightPink2',activebackground='LightPink2', font='arial 15 bold').place(x=200,y=110)

    
##function to play
Result = StringVar()

def play():
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'rock'
    elif comp_pick ==2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissors'
    print(comp_pick)
    if user_take.get() == 1 and  comp_pick == 'rock'  or user_take.get() == 2 and  comp_pick == 'paper' or user_take.get() == 3 and  comp_pick == 'scissors':
        Result.set('tie,you both select same')
    elif user_take.get() == 1 and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_take.get() == 1 and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_take.get() == 2 and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_take.get() == 2 and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_take.get() == 3 and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_take.get() == 3 and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
##to reset
def Reset():
    Result.set("") 
    user_take.set(None)

##to exit
def Exit():
    root.destroy()


###### button
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='White',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', activebackground='LightGoldenrod1',text = 'PLAY'  ,padx =5,bg ='LightGoldenrod1' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', activebackground='LightGoldenrod1',text = 'RESET'  ,padx =5,bg ='light yellow' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', activebackground='LightGoldenrod1',text = 'EXIT'  ,padx =5,bg ='light yellow' ,command = Exit).place(x=230,y=310)

root.mainloop()

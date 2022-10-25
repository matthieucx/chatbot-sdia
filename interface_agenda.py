# INCLUDE

from calendar import week
from tkinter import *
from tkinter import ttk
import numpy as np
import agenda

# INTERFACE

def callback1():
    global week
    week = 42
    gui.destroy()

def callback2():
    global week
    week = 43
    gui.destroy()

def callback3():
    global week
    week = 44
    gui.destroy()

gui = Tk()
v = IntVar
gui.geometry('200x100')  
btn1 = Button(gui, text = "42", command = callback1)
btn1.pack()
btn2 = Button(gui, text = "43", command = callback2)
btn2.pack()
btn3 = Button(gui, text = "44", command = callback3)
btn3.pack()
gui.mainloop()

# tableau qui affiche les données
class Table:

     
    def __init__(self,gui,week): 

        # données utilisées
        cal = agenda.Calendar("calendar")
        lst = np.transpose(cal.get_week(week))
        print(lst)

        # nombre lignes et colonnes tableau affiché
        total_rows = len(lst) + 1
        total_columns = len(lst[0]) + 1
        print(total_rows)
        print(total_columns)

        list_jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        
        # code pour créer la table
        for i in range(total_rows):
            for j in range(total_columns):

                if i == 0 :
                    if j != 0 :
                        self.e = Entry(gui, width = 10, fg = 'blue',
                                font = ('Arial',10,'bold'))
                 
                        self.e.grid(row=i, column = j)
                        self.e.insert(END, list_jours[j-1])
                    else :
                        self.e = Entry(gui, width=10, fg='black',
                                font  =('Arial',10))
                 
                        self.e.grid(row = i, column = j)
                        self.e.insert(END, 'Horaire')

                elif j == 0 :
                    if i != 0 :
                        self.e = Entry(gui, width = 10, fg = 'blue',
                                   font = ('Arial',10,'bold'))
                 
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, str(i-1) + ':00')

                else :
                    self.e = Entry(gui, width=10, fg='black',
                                font=('Arial',10, 'bold'))
                 
                    self.e.grid(row=i, column=j)

                    if (lst[i-2][j-2]) == 0 :
                        self.e.insert(END, ' ')
                    
                    else :
                        self.e.insert(END, '■■■■■■■■■')

  

gui = Tk()
t = Table(gui, week)
gui.mainloop()




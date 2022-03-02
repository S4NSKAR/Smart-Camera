from tkinter import *
from tkinter import messagebox
import os

def dev():
    messagebox.showinfo('Creators : ', 'Developed by : \nSanskar \nPulkit \nRavi \nRakesh')

def mod1():
    os.startfile("dist\\Egg-Catcher\\Mod1.exe")

def mod2():
    os.startfile("dist\\Caterpillar\\Mod2.exe")
    
def mod3():
    os.startfile("dist\\Caterpillar\\Mod3.exe")
    
def mod4():
    os.startfile("dist\\Caterpillar\\Mod4.exe")
    
def mod5():
    os.startfile("dist\\Caterpillar\\Mod5.exe")
    
def mod6():
    os.startfile("dist\\Caterpillar\\Mod6.exe")

top = Tk()
top.geometry("1100x600")
top.title('GAMESON')
c = Canvas(top, height = 600, width = 1100, bg='black', bd=0)
c.create_text(320,5, text='SMART CAMERA BETA',  font=('Megrim', 24, 'bold'), fill='orange',activefill="light blue", anchor=NW)
img = PhotoImage(file  = "Media\\bg.png")
c.create_image(0, 50, image=img, anchor=NW)
Button(text="Photograph", command=mod1, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 120)
Button(text="Video", command=mod2, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 250)
Button(text="Editing", command=mod3, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 380)
Button(text="Object Detector", command=mod4, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 120)
Button(text="Scanner", command=mod5, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 250)
Button(text="CCTV", command=mod6, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 380)
Button(text="Developers", command=dev, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Roboto', 14, 'bold'), relief='raised',height=1, width=15).place(x=430, y = 500)
c.pack()
top.mainloop()
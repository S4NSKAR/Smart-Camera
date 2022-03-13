from tkinter import *
from tkinter import messagebox
import os
import Mod1
import Mod2
import Mod3
import Mod4
import Mod5
import Mod6

def dev():
    messagebox.showinfo('Creators : ', 'Developed by : \nSanskar \nPulkit \nRavi \nRakesh')

top = Tk()
top.geometry("1100x600")
top.title('Smart Camera')
c = Canvas(top, height = 600, width = 1100, bg='black', bd=0)
c.create_text(320,5, text='SMART CAMERA BETA',  font=('Megrim', 24, 'bold'), fill='orange',activefill="light blue", anchor=NW)
img = PhotoImage(file  = "Media\\bg.png")
c.create_image(0, 50, image=img, anchor=NW)
Button(text="Photograph", command=Mod1.Mod1, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 120)
Button(text="Video", command=Mod2.Mod2, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 250)
Button(text="Editing", command=Mod3.Mod3, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 380)
Button(text="Motion Detector", command=Mod4.Mod4, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 120)
Button(text="QR Scanner", command=Mod5.Mod5, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 250)
Button(text="CCTV", command=Mod6.Mod6, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 380)
Button(text="Developers", command=dev, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Roboto', 14, 'bold'), relief='raised',height=1, width=15).place(x=430, y = 500)
c.pack()
top.mainloop()
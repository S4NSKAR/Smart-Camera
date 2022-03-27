from tkinter import *
#import ctypes
from tkinter import messagebox
import Mod1
import Mod2
import Mod3
import Mod4
import Mod5
import Mod6

#ctypes.windll.kernel32.SetDllDirectoryW(None)


def dev():
    messagebox.showinfo('Creators : ', 'Developed by : \nSanskar \nPulkit \nRavi \nRakesh')

top = Tk()
top.geometry("1100x600")
top.title('Smart Camera')
c = Canvas(top, height = 600, width = 1100, bg='black', bd=0)
c.create_text(320,5, text='SMART CAMERA BETA',  font=('Megrim', 24, 'bold'), fill='orange',activefill="light blue", anchor=NW)
img = PhotoImage(file  = "Media\\bg.png")
c.create_image(0, 50, image=img, anchor=NW)
Button(text="Camera", command=Mod1.camera, activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 120)
Button(text="Edit", command=Mod2.edit, activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 250)
Button(text="QR Scanner", command=Mod3.qr_read, activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=28, y = 380)
Button(text="CCTV", command=Mod4.cctv, activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 120)
Button(text="Motion Detector", command=Mod5.mot_det, activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 250)
Button(text="Object Tracker", command=Mod6.obj_tracker, activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=750, y = 380)
Button(text="Developers", command=dev, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Roboto', 14, 'bold'), relief='raised',height=1, width=15).place(x=430, y = 500)
c.pack()
top.mainloop()
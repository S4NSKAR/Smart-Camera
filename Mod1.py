import cv2
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def pic_mod():
    
    cam = cv2.VideoCapture(0)

    while True:
        # debugging
        ret, frame = cam.read()
        if not ret:
            print("Error! Failed to grab frame")
            break
        
        cv2.imshow("Camera", frame)
        
        # wait 1 millisecond for keypress and refresh frame
        k = cv2.waitKey(1)
        
        # print (k) # to find value of any key pressed
        if k== 9:
            messagebox.showinfo('Instructions', 'Press Space to click \nPress Esc to close')
            
        if k == 27:
            # ESC pressed
            print("Closing camera...")
            cam.release()
            cv2.destroyAllWindows()
            break
        
        elif k == 32:
            # SPACE pressed
            cv2.imwrite(f"Camera/IMG_{datetime.now().strftime('%y%m%d-%H%M%S')}.jpg", frame)
            print("{} saved!".format(datetime.now().strftime('%y%m%d-%H%M%S')))
            
    
def vid_mod():
    
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f"Camera/VID_{datetime.now().strftime('%y%m%d-%H%M%S')}.avi", fourcc,20.0,(640,480))

    while True:
        _, frame = cap.read()
        out.write(frame)
        cv2.imshow("Video recording...", frame)
        
        # ESC Pressed
        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break 
        

def camera():
    
    win = Tk()  
    win.geometry("210x90")
    win.title("Mode")
    win.resizable(False, False)
    b1 = Button(win, text = "Picture mode", command=lambda: [win.destroy(), pic_mod()], bd=2, height=2, width=15)
    b1.place(relx=0.5, rely=0.3, anchor=CENTER)
    b2 = Button(win, text = "Video mode", command=lambda: [win.destroy(), vid_mod()], bd=2, height=2, width=15)
    b2.place(relx=0.5, rely=0.7, anchor=CENTER)
    b1.pack()
    b2.pack()
    win.mainloop() 

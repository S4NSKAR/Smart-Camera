import cv2

def Mod1():
    cam = cv2.VideoCapture(0)
    img_counter = 0

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
        if k == 27:
            # ESC pressed
            print("Closing camera...")
            break
        elif k == 32:
            # SPACE pressed
            img_name = "IMG_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} saved!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
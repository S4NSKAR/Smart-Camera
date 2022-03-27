
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def qr_read():
    #decoding barcode
    def decoder(image):
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)

        #processing every barcode in a frame
        for obj in barcode:
            #finding all coordinates of polygon in list
            points = obj.polygon
            #finding top left coordinates x,y for displaying decoded data
            (x,y,w,h) = obj.rect
            #convert list to array
            pts = np.array(points)
            #draw lines of polygons
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)
            
            #convert barcode data from byte to string
            barcodeData = obj.data.decode("utf-8")
            #read barcode type like QR
            barcodeType = obj.type
            string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
            
            #show text on camera interface
            cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
            print("Barcode: "+barcodeData +" | Type: "+barcodeType)

    #read camera frames
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow('Code Reader', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
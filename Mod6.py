import cv2
from datetime import datetime

def Mod6():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'CCTV/{datetime.now().strftime("%y.%m.%d - %H.%M")}.avi', fourcc,20.0,(640,480))

    while True:
        _, frame = cap.read()

        cv2.putText(frame, 'RECORDING...', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (0,0,255), 2)
        cv2.putText(frame, f'{datetime.now().strftime("%y.%m.%d - %H:%M:%S")}', (50,80), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (255,255,255), 2)

        out.write(frame)
        

        cv2.imshow("CCTV", frame)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break 

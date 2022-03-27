import cv2
import imutils

def obj_tracker():

    # Choosing Camera or video file as input
	camera=False
	if camera: 
		video  = cv2.VideoCapture(0)
	else:
		video = cv2.VideoCapture('Media/top.mp4')
    
    # Setting up tracker
	tracker = cv2.TrackerCSRT_create()
	_,frame = video.read()
	# Resizing frame
	frame = imutils.resize(frame, width=720)
	# Selecting Bounding Box and hide crosshair
	BB = cv2.selectROI('Choose object to track', frame, False)
	tracker.init(frame, BB)

	while True:
		_,frame = video.read()
		frame = imutils.resize(frame, width=720)
		# Update tracking frame
		track_success, BB = tracker.update(frame)

		if track_success:
			# Find updated tracker location and draw rectangle
			top_left = (int(BB[0]),int(BB[1]))
			bottom_right = (int(BB[0]+BB[2]), int(BB[1]+BB[3]))
			cv2.rectangle(frame,top_left,bottom_right,(0,255,0),5)

		# Display frame
		cv2.imshow('Tracking...',frame)
		key  =  cv2.waitKey(1)
		if key == 27:
			break

	video.release()
	cv2.destroyAllWindows()
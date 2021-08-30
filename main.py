import cv2

capture=cv2.VideoCapture("/home/pmk/Downloads/WIN_20210826_13_47_05_Pro.mp4")

while cv2.waitKey(33)<0:
  if capture.get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT):
    capture.set(cv2.CAP_PROP_POS_FRAMES,0)

  ret,frame=capture.read()
  cv2.imshow("VideoFrame",frame)

capture.release()
cv2.destroyAllWindows()

import cv2

capture=cv2.VideoCapture("/home/pmk/Downloads/WIN_20210826_13_47_05_Pro.mp4")

cnt=0

while(capture.isOpened()):
  ret,frame=capture.read()

  if(int(capture.get(1))%10==0):
    print('Saved frame number : ' + str(int(capture.get(1))))
    cv2.imwrite("/home/pmk/workspace/frame_drop_tool/images/%05d.png" % cnt, frame)

    cnt+=1

capture.release()
cv2.destroyAllWindows()

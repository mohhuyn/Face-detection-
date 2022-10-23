import cv2
import time
width=640
height=460
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))




Face_O=cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
Left_Eyes=cv2.CascadeClassifier('haar\haarcascade_lefteye_2splits.xml')
Right_Eyes=cv2.CascadeClassifier('haar\haarcascade_righteye_2splits.xml')
TimeN=time.time()

time.sleep(2)
count = 0
while True:
    TimeM=time.time()-TimeN
    TimeN=time.time()
    
    T=int(1/TimeM)
    print(T)
    ignore,  frame = cam.read()
    framG=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=Face_O.detectMultiScale(framG,1.3,5)
  
    cv2.putText(frame,str(T)+'fps',(25,25),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    
    
    for face in faces:
        x,y,z,k=face
        print(x,y,z,k)
    
        cv2.rectangle(frame,(x,y),(z+x,k+y),(0,255,0))

        #t= time.strftime("%Y-%m-%d_%H-%M-%S")
        #img_name = "opencv_frame_{}.png ".format(0)
        file='C:/Users/NsrO/Patient'+str(count)+'.jpg'
        cv2.imwrite(file, frame)
        count=count+1       
        Frm=frame[y:y+k,x:x+z]
        Lefts=Left_Eyes.detectMultiScale(Frm,1.3,5)
        Rights=Right_Eyes.detectMultiScale(Frm,1.3,5)
        for Lef in Lefts:
            x,y,z,k=Lef
            cv2.rectangle(Frm,(x,y),(z+x,k+y),(0,255,0))
        for Rig in Rights:
           x,y,z,k=Rig
           cv2.rectangle(Frm,(x,y),(z+x,k+y),(0,255,0))
    cv2.imshow('my WEBcam', frame)
   


    cv2.moveWindow('my WEBcam',0,0)
    
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyWindow

import cv2

face_classifier = cv2.CascadeClassifier('C:/Users/pulkit/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h)  in faces:
         cropped_face = img[y:y+h,x:x+w]

    return cropped_face


cap = cv2.VideoCapture(0)
count =0


while True:
    ret,frame=cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame),(400,640))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

        file_name = 'D:/faces/person'+str(count)+'.jpg'
        cv2.imwrite(file_name,face)

        Font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(face,str(count),(50,50),Font,1,(0,0,255),2)
        cv2.imshow('face cropped',face)
    else:
        print("not found")
        pass
    if cv2.waitKey(1)==27 or count==100:
        break

cap.release()
cv2.destroyAllWindows()


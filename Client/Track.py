import cv2

class Track:
    def __init__(self) -> None:
        pass

    def face_detection():
        # Enable camera
        cap = cv2.VideoCapture(0)
        cap.set(3, 640) # width
        cap.set(4, 480) # height

        # import cascade file for facial recognition
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # if you want to detect any object for example eyes, use one more layer of classifier as below:
        eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

        while True:
            success, img = cap.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Getting corners around the face
            faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  # 1.3 = scale factor, 5 = minimum neighbor
            # drawing bounding box around face
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                # print(x, y, w, h)
            img_tmp = cv2.rectangle(img, (10, 10), (630, 410), (0, 255, 0), 3)
            
            # # detecting eyes
            # eyes = eyeCascade.detectMultiScale(imgGray)
            # # drawing bounding box for eyes
            # for (ex, ey, ew, eh) in eyes:
            #     img = cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)

            cv2.imshow('face_detect', img)
            cv2.imshow('test', img_tmp)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyWindow('face_detect')

    def track(self, ):
        pass




if __name__ == '__main__':
    pass
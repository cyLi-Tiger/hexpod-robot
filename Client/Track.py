import cv2
from Command import COMMAND as cmd

class Track:
    def __init__(self) -> None:
        pass
    
    def face_detection(self, img):
        """ Detect face and return the direction command for hexapod

        Args:
            img (QImage): The image data comes from server

        Returns:
            commnd: The command for hexpod
        """

        # import cascade file for facial recognition
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Getting corners around the face
        faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  # 1.3 = scale factor, 5 = minimum neighbor
        
        if (len(faces) == 0):
            return None
        # drawing bounding box around face
        else:
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                # print(x, y, w, h)

                mid_point = img.shape[1] / 2
                left_command = cmd.CMD_MOVE+ "#"+str(1)+"#"+str(0)+"#"+str(15)\
                                    +"#"+str(5)+"#"+str(-10) +'\n'
                right_command = cmd.CMD_MOVE+ "#"+str(1)+"#"+str(0)+"#"+str(15)\
                                    +"#"+str(5)+"#"+str(10) +'\n'
                forward_command = cmd.CMD_MOVE+ "#"+str(1)+"#"+str(0)+"#"+str(25)\
                                    +"#"+str(5)+"#"+str(0) +'\n'
                # Generate command
                print(x, x+w, mid_point)
                if (x > mid_point):
                    command = right_command
                    print('turn right')
                elif ((x + w) < mid_point):
                    command = left_command
                    print('turn left')
                else:
                    command = forward_command
                    print('go forward')

                # print(command)
                return command

    def track(self, ):
        pass




if __name__ == '__main__':
    pass
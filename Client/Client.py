# -*- coding: utf-8 -*-
import io
import math
import copy
import socket
import struct
import threading
from PID import *
from Face import *
import numpy as np
from Thread import *
import multiprocessing
from PIL import Image, ImageDraw
from Command import COMMAND as cmd
import time

from Track import *

class Client:
    def __init__(self):
        self.face=Face()
        self.track = Track()
        self.pid=Incremental_PID(1,0,0.0025)
        self.tcp_flag=False
        self.video_flag=True
        self.fece_id=False
        self.fece_recognition_flag = False
        self.image=''
    def turn_on_client(self,ip):
        self.client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print (ip)
    def turn_off_client(self):
        try:
            self.client_socket.shutdown(2)
            self.client_socket1.shutdown(2)
            self.client_socket.close()
            self.client_socket1.close()
        except Exception as e:
            print(e)
    def is_valid_image_4_bytes(self,buf): 
        bValid = True
        if buf[6:10] in (b'JFIF', b'Exif'):     
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                bValid = False
        else:        
            try:  
                Image.open(io.BytesIO(buf)).verify() 
            except:  
                bValid = False
        return bValid
    def receiving_video(self,ip):
        try:
            self.client_socket.connect((ip, 8002))
            self.connection = self.client_socket.makefile('rb')
        except:
            #print ("command port connect failed")
            pass
        while True:
            try:
                stream_bytes= self.connection.read(4)
                leng=struct.unpack('<L', stream_bytes[:4])
                jpg=self.connection.read(leng[0])
                if self.is_valid_image_4_bytes(jpg):
                    if self.video_flag:
                        # command = cmd.CMD_MOVE+ "#"+str(1)+"#"+str(0)+"#"+str(15)\
                        #         +"#"+str(5)+"#"+str(-10) +'\n'
                        # print(command)
                        # self.send_data(command)
                        self.image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                        # data_forward = ['CMD_MOVE', '1', '0', '25', '5', '0']
                        # data_left = ['CMD_MOVE', '1', '0', '15', '5', '-10']
                        # data_right = ['CMD_MOVE', '1', '0', '15', '5', '10']

                        if self.fece_id == False and self.fece_recognition_flag:
                            # self.face.face_detect(self.image)
                            command = self.track.face_detection(self.image)
                            # print('detecting...')
                            # print(command)
                            if command == None:
                                continue
                            else:
                                self.send_data(command)
                        self.video_flag=False
                time.sleep(0.5)
            except BaseException as e:
                print (e)
                break
    def send_data(self,data):
        if self.tcp_flag:
            try:
                self.client_socket1.send(data.encode('utf-8'))
            except Exception as e:
                print(e)
    def receive_data(self):
        data=""
        data=self.client_socket1.recv(1024).decode('utf-8')
        return data

if __name__ == '__main__':
    c=Client()
    c.face_recognition()

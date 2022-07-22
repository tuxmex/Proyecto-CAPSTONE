from deepface import DeepFace
import cv2

url= 'http://192.168.1.69:81/stream'

cv2.namedWindow("Detecta cliente", cv2.WINDOW_AUTOSIZE)
camara = cv2.VideoCapture(url)

DeepFace.stream(db_path='/home/gbarron/capstone/src/my_db/', model_name='VGG-Face', source=url)

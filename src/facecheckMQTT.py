import sys, getopt
from deepface import DeepFace
import paho.mqtt.client as mqtt
import time
import pandas as pd

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def main(argv):
   img_src = ''
   db_src = ''
   try:
      opts, args = getopt.getopt(argv,"hi:j:",["imgsrc=","dbsrc="])
   except getopt.GetoptError:
      print ('test.py -i <img_src> -j <db_src>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <img_src> -j <db_src>')
         sys.exit()
      elif opt in ("-i", "--imgsrc"):
         img_src = arg
      elif opt in ("-j", "--dbsrc"):
         db_src = arg
   #print ('Imagen a analizar ', img_src)
   #print ('Biblioteca de rostros ', db_src)
   df = DeepFace.find(img_path = img_src,db_path= db_src,model_name='VGG-Face',enforce_detection=False)
   #df = DeepFace.stream(db_path= db_src)
   #print ("Resultado ")
   print (df)
   result = df.to_json(orient="index")
   #print ("raw ", df)
   #print ("size of ", df[0].size)
   
   

   client = mqtt.Client()
   client.on_connect = on_connect
   client.connect("localhost", 1883, 60)
   client.publish('capstone/facial', payload=result, qos=0, retain=False)
   #for i in range(3):
      #client.publish('codigoIoT/py', payload=dff.to_string(), qos=0, retain=False)
      #print(f"send {i} to a/b")
      #time.sleep(1)
   return df

if __name__ == "__main__":
   main(sys.argv[1:])
   

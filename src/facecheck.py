from deepface import DeepFace

df = DeepFace.find(img_path = "people/deniro.jpg",db_path= "my_db/", enforce_detection="true")
print ("Resultado ")
print (df)

# coding: utf-8

# In[ ]:

#Algoritmo de deteccion de colores
#Por Glar3
#
#
#Detecta objetos verdes, elimina el ruido y busca su centro
 
import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro
    
    azul_bajos = np.array([110,50,50], dtype=np.uint8)
    azul_altos = np.array([130,255,255], dtype=np.uint8)
 
    #Crear una mascara con solo los pixeles dentro del rango de verdes
  
    maskazul = cv2.inRange(hsv, azul_bajos, azul_altos)
    #Encontrar el area de los objetos que detecta la camara
   
    momentsazul = cv2.moments(maskazul)
    areaazul = momentsazul['m00']
    #Descomentar para ver el area por pantalla
    #print area
    
    if(areaazul > 2000000):
    
    
        #Buscamos el centro x, y del objeto azul
        xr= int(momentsazul['m10']/momentsazul['m00'])
        yr = int(momentsazul['m01']/momentsazul['m00'])
         
  
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (xr-50, yr-50), (xr+50, yr+50),(0,230,255), 2)
    
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('mask', maskazul)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()


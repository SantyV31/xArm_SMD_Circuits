import numpy as np
import cv2
import math

class Detectar:
    def __init__(self,image):
        self.figuras = []
        self.aux = 0
        self.image=image
        self.medicionx=0.026
        self.mediciony=0.020
        self.width=640 
        self.height=480
        self.distancia=[]
    
    def transformaciones_geométricas(self):
        # Realizo la rotación de la imagen
        self.image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        # Cammbio de perspectiva
        pts1 = np.float32([[18.4,47.5],[599.3,44.9],[18.46,908.6],[596.5,915.5]])
        pts2 = np.float32([[0,0],[600,0],[0,800],[600,800]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        self.image = cv2.warpPerspective(self.image,M,(600,800))
    
    def detectar(self,resultado):

    # Dibujar las detecciones en la imagen
        for result in resultado:
            puntos   = result.data[0]
            x1, y1, x2, y2, confianza, tipo = int(puntos[0]), int(puntos[1]), int(puntos[2]), int(puntos[3]), int(puntos[4]), int(puntos[5])

            if (tipo == 0):
                nombre = "Bornera"
                valor  = 2

            if (tipo == 1):
                nombre = "Bornera"
                valor  = 3
            
            if (tipo == 2):
                nombre = "Capacitor"
                valor  = 10

            if (tipo == 3):
                nombre = "Capacitor"
                valor  = 220

            if (tipo == 4):
                nombre = "Led"
                valor  = 1
            
            if (tipo == 5):
                nombre = "Resistencia"
                valor  = 100
            
            if (tipo == 6):
                nombre = "Resistencia"
                valor  = 1000
            
            if (tipo == 7):
                nombre = "Resistencia"
                valor  = 10000
            
            if (tipo == 8):
                nombre = "Resistencia"
                valor  = 120000
            
            if (tipo == 9):
                nombre = "Resistencia"
                valor  = 1

            if (tipo == 10):
                nombre = "Resistencia"
                valor  = 470
            
            if (tipo == 11):
                nombre = "Resistencia"
                valor  = 47

            label = nombre +"_"+str(valor)
            
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Calcular el punto medio como el centroide

            cx_real = round (cx*self.medicionx/self.width,  5)
            cy_real = round (cy*self.mediciony/self.height, 5)
            
            aux = (nombre,cx_real,cy_real,int(valor))
            self.figuras.append(aux)
            cv2.rectangle(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(self.image, f"{label}: {confianza:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


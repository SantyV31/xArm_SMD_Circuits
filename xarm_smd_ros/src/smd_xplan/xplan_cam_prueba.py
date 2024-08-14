#!/usr/bin/env python3

import rospy
import cv2
from xarm_smd_ros.msg import ListaComponentes,Componente
from  Funcion_detección_Obj import Detectar

def cifrar_mensajes(listado):
    aux = []
    mensaje_componente= ListaComponentes()
    for i in range(len(listado)):
        comp = Componente()
        comp.valor  = int(listado[i][3])
        comp.pos_x  = listado[i][1]
        comp.pos_y  = listado[i][2]
        comp.nombre = listado[i][0] 
        aux.append(comp)
    mensaje_componente.listacomponentes = aux
    return mensaje_componente

def EnvioDatos():
    # Inicializar el nodo ROS
    rospy.init_node('prueba_cam', anonymous=True)
    # Topics para publicar 
    pub_figura = rospy.Publisher('Componentes', ListaComponentes, queue_size=1)

    width      = 640
    height     = 480
    medicionx  = 0.026
    mediciony  = 0.020 

    nombres = ["Resistencia","Resistencia","Resistencia","Resistencia","Resistencia","Resistencia","Resistencia",
               "Led","Led","Led","Led","Led","Led","Led",
               "Bornera","Bornera","Bornera","Bornera"]
    valores = [ 1200, 1200, 470, 470, 470, 470, 470,
               1, 1, 1, 1, 1, 1, 1,
               2, 2, 2, 2]

    posx = [ 120, 120, 120, 120 ,120, 120, 
             240, 240, 240, 240 ,240, 240,
             400, 400, 400, 400, 400, 400]
    
    posy = [ 60, 120, 180, 240, 300, 360,
             60, 120, 180, 240, 300, 360,
             60, 120, 180, 240, 300, 360 ]
    
    
    
    rate = rospy.Rate(1)  # 30 Hz
    # Bucle principal

    while not rospy.is_shutdown():
        componentes =[]
        for i in range(len(nombres)):
            nombre = nombres[i]
            valor  = valores[i]
            cx = posx[i]
            cy = posy[i]
            cx_real = round (cx*medicionx/width,  5 )
            cy_real = round (cy*mediciony/height, 5 )

            aux = (nombre,cx_real,cy_real,int(valor))
            componentes.append(aux)
        
        mensaje = cifrar_mensajes(componentes)

        if (len(mensaje.listacomponentes)>0):
                pub_figura.publish(mensaje)
        
        rospy.sleep(5)
        rate.sleep()


if __name__ == '__main__':
    try:
        EnvioDatos()
    except rospy.ROSInterruptException:
        pass

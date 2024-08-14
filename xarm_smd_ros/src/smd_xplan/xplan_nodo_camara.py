#!/usr/bin/env python3

import rospy
import cv2
from xarm_smd_ros.msg import ListaComponentes,Componente
from  Funcion_detección_Obj import Detectar
from ultralytics import YOLO

usb_cam = 2


def modelo_start():
    global model
    # Lectura del Modelo
    # Load the YOLOv8 model
    model = YOLO("/home/santy/xARM6_ws/src/xarm_smd_ros/modelo/best-l.pt")

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

def camera_stream():
    # Inicializar el nodo ROS
    rospy.init_node('camera_stream', anonymous=True)
    # Topics para publicar 
    pub_figura = rospy.Publisher('Componentes', ListaComponentes, queue_size=1)
    cap = cv2.VideoCapture(usb_cam)
    # Comprobar si la cámara se ha abierto correctamente
    if not cap.isOpened():
        rospy.logerr("No se pudo abrir la cámara")
        return

    # Variables para la publicación de datos
    frecuencia = 30
    cont       = 0
    # Definir la frecuencia de publicación del video (en Hz)
    rate = rospy.Rate(30)  # 30 Hz
    # Bucle principal
    while not rospy.is_shutdown():
        # Capturar un fotograma de la cámara
        ret, frame = cap.read()

        # Comprobar si se ha capturado correctamente el fotograma
        if ret:
            # algoritmo de red neurotal (Deteccion de Objetos)
            # Instancia de la clase
            imagen = Detectar(frame)
            # imagen.transformaciones_geométricas()
            # Inference
            results = model(imagen.image)
            # Obtengo los resultados
            resultado = results[0].boxes.cpu()
            resultado = resultado.numpy()
            # Obtener las detecciones
            imagen.detectar(resultado)
            # Cifrado de mensajes del Objetivo
            mensaje = cifrar_mensajes(imagen.figuras)

            if (len(mensaje.listacomponentes)>0 and cont%frecuencia ==0):
                pub_figura.publish(mensaje)

            # Mostrar el fotograma en una ventana llamada "Camera Stream"
            cv2.imshow("Camera", imagen.image)
            cont = cont+1

        # Esperar un tiempo para mantener la frecuencia de publicación
        rate.sleep()

        # Comprobar si se ha pulsado la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar todas las ventanas de OpenCV al salir del bucle
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        modelo_start()
        camera_stream()
    except rospy.ROSInterruptException:
        pass

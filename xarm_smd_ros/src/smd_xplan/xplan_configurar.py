#!/usr/bin/env python3

import rospy
import subprocess
from std_msgs.msg import Bool

def callback(msg):
    call_move_line_service()

def call_move_line_service():
    global pub_respuesta
    respuesta = False
    try:
        rospy.loginfo("Esperando por la activación del servicio de condiguración")
        print("Configurando Ufactory lite 6")
        subprocess.call(["rosservice", "call", "/ufactory/clear_err"])
        subprocess.call(["rosservice", "call", "/ufactory/set_mode", "0"])
        subprocess.call(["rosservice", "call", "/ufactory/set_state", "0"])
        respuesta = True
    except subprocess.CalledProcessError as e:
        rospy.logerr("Error al configurar el Xarm Lite 6: %s", str(e))
    pub_respuesta.publish(respuesta)

def main():
    global pub_respuesta
    rospy.init_node('configurar_xarm')
    rospy.Subscriber("Movimiento/Activar", Bool, callback)
    pub_respuesta = rospy.Publisher("Movimiento/R_Activar", Bool, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    main()

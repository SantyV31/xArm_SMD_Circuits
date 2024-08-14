#!/usr/bin/env python3

import rospy
import subprocess
from std_msgs.msg import Bool,Int16

def callback(msg):
    call_move_line_service(msg.data)

def call_move_line_service(estado):
    global pub_respuesta
    respuesta = False
    try:
        rospy.loginfo("Arrancando servicio de pinza al vacio")
        datos = str(estado)
        output = subprocess.check_output(["rosservice", "call", "/ufactory/vacuum_gripper_set", datos], timeout=10)
        print("Respuesta:", output.decode())
        respuesta = True
    except subprocess.CalledProcessError as e:
        rospy.logerr("Error calling move_line service: %s", str(e))
    except subprocess.TimeoutExpired:
        rospy.logerr("Timeout al llamar al servicio")
    pub_respuesta.publish(respuesta)

def main():
    global pub_respuesta
    rospy.init_node('pinza_vacio')
    rospy.Subscriber("Gripper/Activar", Int16, callback)
    pub_respuesta = rospy.Publisher("Gripper/Respuesta", Bool, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    main()


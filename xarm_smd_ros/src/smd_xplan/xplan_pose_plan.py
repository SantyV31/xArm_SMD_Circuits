#!/usr/bin/env python3

import rospy
import subprocess
from std_msgs.msg import Bool
from xarm_smd_ros.msg import Posicion
import math

def callback(msg):
    pos_x  = msg.pos_x 
    pos_y  = msg.pos_y   
    pos_z  = msg.pos_z  
    giro_x = msg.giro_x 
    giro_y = msg.giro_y 
    giro_z = msg.giro_z 
    call_move_line_service(pos_x,pos_y,pos_z,giro_x,giro_y,giro_z)

def call_move_line_service(pos_x,pos_y,pos_z,ori_x,ori_y,ori_z):
    global pub_respuesta
    respuesta = False
    try:
        rospy.loginfo("Calling xarm_pose_plan service...")
        posicion = [pos_x, pos_y, pos_z]
        giro_x = int(ori_x)
        giro_y = int(ori_y)
        giro_z = int(ori_z)

        if (giro_x != 0):
            w  = math.cos(giro_x/360*math.pi)
            wx = math.sin(giro_x/360*math.pi)
            wy = giro_y
            wz = giro_z
        
        if (giro_y != 0):
            w  = math.cos(giro_y/360*math.pi)
            wx = giro_x
            wy = math.sin(giro_y/360*math.pi)
            wz = giro_z
        
        if (giro_z != 0):
            w  = math.cos(giro_z/360*math.pi)
            wx = giro_x
            wy = giro_y
            wz = math.sin(giro_z/360*math.pi) 

        orientacion  = [wx,wy,wz,w]
        datos = [posicion,orientacion]
        print("La posición enviada es:",datos)
        # Añade un tiempo de espera de 10 segundos
        output = subprocess.check_output(["rosservice", "call", "/xarm_pose_plan", str(datos)], timeout=10)
        print("Respuesta:", output.decode())
        subprocess.call(["rosservice", "call", "xarm_exec_plan", "true"], timeout=10)
        respuesta = True
        
    except subprocess.CalledProcessError as e:
        rospy.logerr("Error calling move_line service: %s", str(e))
    except subprocess.TimeoutExpired:
        rospy.logerr("Timeout al llamar al servicio")
    pub_respuesta.publish(respuesta)

def main():
    global pub_respuesta
    rospy.init_node('move_pose_plan')
    rospy.Subscriber("Movimiento/Posicion", Posicion, callback)
    pub_respuesta = rospy.Publisher("Movimiento/Respuesta", Bool, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    main()


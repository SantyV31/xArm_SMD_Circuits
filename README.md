# xArm_SMD_Circuits
Sistema de montaje de circuito SMD impresos con el robot Ufactory Lite 6.

# xarm_smd_ros
El paquete implementa nodos de ros para realizar montaje superficial de circuitos utilizando un Robot- Ufactory lite 6

# Comandos de ejecución

* Simulador

roslaunch xarm_planner xarm_planner_rviz_sim.launch robot_dof:=6 robot_type:=lite  add_gripper:=false add_vacuum_gripper:=true

* Real

roslaunch xarm_planner xarm_planner_realHW.launch robot_ip:=192.168.1.186 robot_dof:=6 robot_type:=lite add_gripper:=false add_vacuum_gripper:=true


Launcher con Xplan 

roslaunch xarm_smd_ros xarm_smd_ros_xplan.launch

# Archivo de modelo entrenado 

El modelo del entrenamiento YOLOv8 se encuentra en la carpeta modelo con el nombre de best.pt, que contiene el entrenamiento de los elementos electrónicos con 200 épocas.

Este archivo es el principal para reconocer los elementos que se encuentre en el espacio de trabajo, la que activa el archivo xplan_nodo_camara.py.

# Arquitectura

Dentro del archivos de arquitetura se encuentra los códigos que envía al robot para la posición correcta de recoger y colocar el elemento de una forma milimétrica en sus movimientos.

# Nodos xplan

Los archivos que llevan el nombre de xplan son las configuraciones del robot.

1.- El robot se enciende y activa todos sus acrtuadores para el correcto funcionamiento.

2.- El sistema activa la cámara para visualizar los elementos y ser detectados mediante el entrenamiento YOLOv8.

3.- El robot se ubica en posición home para realizar su respectivo trabajo.

4.- El robot activa y descactiva la pinza al vacío para recoger y soltar el elemento.

# Carpeta Launch

En dicha carpeta se encuentra los archivos launch para el funcionamiento del robot mediante el sistema Operativo ROS, para la ejecución del sistema.



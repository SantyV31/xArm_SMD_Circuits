# xarm_smd_ros
El paquete implementa nodos de ros para realizar montaje superficial de circuitos utilizando un Robot- Ufactory lite 6

# Comandos de ejecución

* Simulador

roslaunch xarm_planner xarm_planner_rviz_sim.launch robot_dof:=6 robot_type:=lite  add_gripper:=false add_vacuum_gripper:=true

* Real

roslaunch xarm_planner xarm_planner_realHW.launch robot_ip:=192.168.1.186 robot_dof:=6 robot_type:=lite add_gripper:=false add_vacuum_gripper:=true


Launcher con Xplan 

roslaunch xarm_smd_ros xarm_smd_ros_xplan.launch

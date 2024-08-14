#!/usr/bin/env python3

import rospy
import smach
import numpy as np 
#import smach_ros
from std_msgs.msg import Int16,Bool

from xarm_smd_ros.msg import Componente,ListaComponentes,Posicion
from arquitectura import Base_Datos,controlador_msg

#### Estados  ####

# https://wiki.ros.org/common_msgs

class E_Home(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['activar', ])
    
    def execute(self, userdata):
        rospy.loginfo("E_Home. INICIO DE ESTADO")

        pub_activar.publish(True)
        # Realizo el movimineto del robot al HOME
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/R_Activar" con un tiempo máximo de espera de 30 segundos
            rospy.wait_for_message("Movimiento/R_Activar", Bool, timeout=5)

        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Activar' dentro de los 30 segundos")

        pub_home.publish(True)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/R_Home" con un tiempo máximo de espera de 30 segundos
            rospy.wait_for_message("Movimiento/R_Home", Bool, timeout=5)
            
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Home' dentro de los 30 segundos")
        
        return "activar"
    
class E_Obtener_Datos(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['activar', 'reintentar'])
        self.condicion = 0
        self.circuito  = 4
    
    def execute(self, userdata):
        print("E_Obtener_Datos. INICIO DE ESTADO")

        while B_Datos.b_mensaje == 0:
            print("Esperando detección")
            rospy.sleep(1)

        B_Datos.b_mensaje = 0
        self.condicion = 0

        if B_Datos.t_componentes == 0:
            print("No se han encontrado componentes en el espacio de trabajo")
        else:
            print("Se han encontrado compoentes en el espacio de trabajo")
            # Obtengo las coordenadas de las figuras en el área de trabajo.
            B_Datos.list_componentes.listacomponentes = Contro_Msg.list_componentes.listacomponentes
            # Registro en la base de datos
            B_Datos.Agregar_Almacen(B_Datos.list_componentes)
            print("Seleccione el tipo de circuito")
            print("Divisor de Voltaje: 1")
            print("Circuito Leds: 2")
            self.circuito = 4
            while (self.circuito > 2):
                self.circuito = int(input("Aceptar"))
            B_Datos.Componentes_SMD(self.circuito)
            B_Datos.Imprimir_Dic()
            # Compruebo si existen todos los componentes del circuito dentro del almacen y estàn asignados
            self.condicion = B_Datos.Comprobar_Componentes()
            if (self.condicion == 0):
                B_Datos.EliminarComponentes()
        if (self.condicion == 1):
            return "activar"
        else:
            return "reintentar"

class E_Recoger_Componente(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['activar', 'reintentar'])
        self.condicion         = 0
        self.nombre_componente = []

    # Modificado para la corección de posición -------------------------------------------------
    # Función de compensación
    def compensar_medicion(self, punto_medido):
        # Mediciones (Puntos M)
        M = np.array([[0.21982, -0.30242],[0.21251, -0.30779],[0.20804, -0.30671],[0.21137, -0.302],[0.21532, -0.30471],
                    [0.2036, -0.30404],[0.21495, -0.29867],[0.22035, -0.30708],[0.20735, -0.29971]])

        # Valores reales (Puntos P)
        P = np.array([[0.2099, -0.3167],[0.2029, -0.3099],[0.2059, -0.3052],[0.2089, -0.3082],[0.2069, -0.3119],
                    [0.2037, -0.3171],[0.21, -0.304],[0.2128, -0.3131],[0.2078, -0.301]])

        # Errores
        errores = P - M
        # Encontrar los dos puntos más cercanos en la lista de mediciones (M)
        indice1 = np.argmin(np.linalg.norm(M - punto_medido, axis=1))
        indice2 = np.argsort(np.linalg.norm(M - punto_medido, axis=1))[1]

        # Calcular el factor de interpolación
        distancia_total = np.linalg.norm(M[indice2] - M[indice1])
        distancia_punto1 = np.linalg.norm(punto_medido - M[indice1])
        factor_interpolacion = distancia_punto1 / distancia_total

        # Interpolar los errores
        error_interpolado = errores[indice1] + factor_interpolacion * (errores[indice2] - errores[indice1])

        # Compensar la medición sumando el error interpolado al punto medido
        punto_compensado = punto_medido + error_interpolado

        return punto_compensado
    # Modificado para la corección de posición
        
    def execute(self, userdata):
        rospy.loginfo("E_Recoger_Componente. INICIO DE ESTADO")
        # Obtengo las claves del diccionario para el movimiento 
        self.nombre_componente = []
        for componente, circuito in B_Datos.componentes_circuito_origen.items():
            self.nombre_componente.append(componente)

        rospy.loginfo("Componente actual: %s", self.nombre_componente[B_Datos.orden])
        # Movimiento al área de componentes:
        msg = B_Datos.Go_Area_Componente()
        pub_posicion.publish(msg)

        # Esperar a que termine el movimiento 
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Movimiento/Respuesta", Bool, timeout=80)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Movimiento/R_Posicion'.")
            else:
                print("Se recibió un mensaje False en el tema 'Movimiento/R_Posicion'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Posicion' dentro de los 30 segundos")
        
        # Movimiento al componente 
        x = B_Datos.componentes_circuito_origen[self.nombre_componente[B_Datos.orden]]["pos_x"]
        y = B_Datos.componentes_circuito_origen[self.nombre_componente[B_Datos.orden]]["pos_y"]
        print ("El valor antes de interpolar es", x,y)
        punto_medido = np.array([x, y])
        punto_compensado = self.compensar_medicion(punto_medido)
        pos_x = punto_compensado[0]
        pos_y = punto_compensado[1]
        print ("El valor compensado es :", pos_x, pos_y)

        #Redirigiendo componente

        pos_x, pos_y = B_Datos.Cuadrantes(pos_x,pos_y)
        msg = B_Datos.Go_Componente(pos_x,pos_y)
        # Modificado para la corección de posición 

        pub_posicion.publish(msg)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Movimiento/Respuesta", Bool, timeout=80)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Movimiento/R_Posicion'.")
                self.condicion = 1
            else:
                print("Se recibió un mensaje False en el tema 'Movimiento/RespR_Posicionuesta'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Posicion' dentro de los 30 segundos")

        rospy.sleep(2)

        # Activo el servicio de la pinza 
        pub_pinza.publish(1)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Gripper/Respuesta", Bool, timeout=30)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Gripper/Respuesta'.")
            else:
                print("Se recibió un mensaje False en el tema 'Gripper/Respuesta'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Gripper/Respuesta' dentro de los 30 segundos")

        
        # Movimiento al auxiliar 
        msg = B_Datos.Go_Aux(pos_x,pos_y)
        # Modificado para la corección de posición 

        pub_posicion.publish(msg)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Movimiento/Respuesta", Bool, timeout=80)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Movimiento/R_Posicion'.")
                self.condicion = 1
            else:
                print("Se recibió un mensaje False en el tema 'Movimiento/RespR_Posicionuesta'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Posicion' dentro de los 30 segundos")

        rospy.sleep(2)
        
        if (self.condicion == 1):
            # Asignación de tareas exitosa 
            return "activar"
        else:
            # Fallo en la asignación de tareas
            return "reintentar"

class E_Colocar_Componente(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['activar', 'reintentar'])
        self.condicion = 0 
    
    def execute(self, userdata):
        rospy.loginfo("E_Colocar_Componente. INICIO DE ESTADO")

        # Obtengo las claves del diccionario para el movimiento 
        self.nombre_componente = []
        for componente, circuito in B_Datos.componentes_circuito_destino.items():
            self.nombre_componente.append(componente)

        # Movimiento al área de componentes:
        msg = B_Datos.Go_Area_Circuito()
        pub_posicion.publish(msg)
        # Esperar a que termine el movimiento 
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Movimiento/Respuesta", Bool, timeout=30)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Movimiento/R_Posicion'.")
            else:
                print("Se recibió un mensaje False en el tema 'Movimiento/R_Posicion'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Posicion' dentro de los 30 segundos")

        # Movimiento al componente 
        msg = B_Datos.Go_Circuito(B_Datos.componentes_circuito_destino[self.nombre_componente[B_Datos.orden]]["pos_x"],
                                    B_Datos.componentes_circuito_destino[self.nombre_componente[B_Datos.orden]]["pos_y"])
        pub_posicion.publish(msg)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Movimiento/Respuesta", Bool, timeout=30)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Movimiento/R_Posicion'.")
                self.condicion = 1
            else:
                print("Se recibió un mensaje False en el tema 'Movimiento/RespR_Posicionuesta'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Posicion' dentro de los 30 segundos")

        rospy.sleep(2)

         # Activo el servicio de la pinza 
        pub_pinza.publish(0)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Gripper/Respuesta", Bool, timeout=30)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Gripper/Respuesta'.")
            else:
                print("Se recibió un mensaje False en el tema 'Gripper/Respuesta'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Gripper/Respuesta' dentro de los 30 segundos")

        # Movimiento al auxiliar
        pos_x = B_Datos.componentes_circuito_destino[self.nombre_componente[B_Datos.orden]]["pos_x"]
        pos_y = B_Datos.componentes_circuito_destino[self.nombre_componente[B_Datos.orden]]["pos_y"] 
        msg = B_Datos.Go_Aux(pos_x,pos_y)
        # Modificado para la corección de posición 

        pub_posicion.publish(msg)
        try:
            # Esperar hasta que se reciba un mensaje en el tema "Movimiento/Activar" con un tiempo máximo de espera de 30 segundos
            mensaje = rospy.wait_for_message("Movimiento/Respuesta", Bool, timeout=80)
            # Ahora puedes acceder al campo "data" del mensaje para obtener el valor booleano
            if mensaje.data:
                print("Se recibió un mensaje True en el tema 'Movimiento/R_Posicion'.")
                self.condicion = 1
            else:
                print("Se recibió un mensaje False en el tema 'Movimiento/RespR_Posicionuesta'.")
        except rospy.exceptions.ROSException:
            print("No se recibió ningún mensaje en el tema 'Movimiento/R_Posicion' dentro de los 30 segundos")

        rospy.sleep(2)
        
        if (self.condicion == 1):
            # Asignación de tareas exitosa 
            return "activar"
        else:
            # Fallo en la asignación de tareas
            return "reintentar"

class E_Armar_Circuito(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['activar', 'salir'])
        self.condicion = 0 
    
    def execute(self, userdata):
        rospy.loginfo("E_Armar_Circuito. INICIO DE ESTADO")
        rospy.loginfo("Componente: %s Ubicado", B_Datos.orden)
        B_Datos.orden +=1
        # Evalúo si existen aun componentes
        if (B_Datos.orden < len(B_Datos.componentes_circuito_destino.items())):
            self.condicion  = 1
        else:
            self.condicion  = 0

        if (self.condicion == 1):
            # Movimiento Exitoso
            return "activar"
        else:
            return "salir"
        
class E_Reconfiguracion(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['activar', 'desactivar'])
        self.condicion = 0 
    
    def execute(self, userdata):
        print("E_Reconfiguracion. INICIO DE ESTADO")
        print("Continar ")
        print("Salir:     1")
        print("Continuar: 2")
        # Obtengo las coordenadas de las figuras en el área de trabajo.
        opcion = input()
        if (opcion == str(2)):
            self.condicion = 1
            B_Datos.orden = 0
            B_Datos.EliminarComponentes()
        else:
            self.condicion = 0

        # Registro en la base de datos
        if (self.condicion == 1):
            # Movimiento Exitoso
            return "activar"
        else:
            return "desactivar"

### Callbacks ####
        
def callback_deteccion(msg):
    B_Datos.t_componentes = len(msg.listacomponentes)
    Contro_Msg.list_componentes.listacomponentes = msg.listacomponentes
    B_Datos.b_mensaje = 1

### MAQUINA DE ESTADOS ####
def crear_maquina_estado():
    sm = smach.StateMachine(outcomes=['FINALIZAR'])
    with sm:

        smach.StateMachine.add('HOME', E_Home(),
                               transitions={'activar':'OBTENER_DATOS', })
        
        smach.StateMachine.add('OBTENER_DATOS', E_Obtener_Datos(),
                               transitions={'activar':'RECOGER_COMPONENTE', 'reintentar':'OBTENER_DATOS'})
        
        smach.StateMachine.add('RECOGER_COMPONENTE', E_Recoger_Componente(),
                               transitions={'activar':'COLOCAR_COMPONETE', 'reintentar':'RECOGER_COMPONENTE'})
        
        smach.StateMachine.add('COLOCAR_COMPONETE', E_Colocar_Componente(),
                               transitions={'activar':'ARMAR_CIRCUITO', 'reintentar':'COLOCAR_COMPONETE'})
        
        smach.StateMachine.add('ARMAR_CIRCUITO', E_Armar_Circuito(),
                               transitions={'activar':'RECOGER_COMPONENTE', 'salir':'RECONFIGURACION'})
        
        smach.StateMachine.add('RECONFIGURACION', E_Reconfiguracion(),
                               transitions={'activar':'HOME', 'desactivar':'FINALIZAR'})

    return sm

### FUNCIÓN PRINCIPAL


def main():
    global pub_posicion,pub_home,pub_activar,pub_pinza

    rospy.init_node('nodo_central')
    # Topicos para suscripción
    
    rospy.Subscriber('Componentes', ListaComponentes, callback_deteccion)
    # Topics  para la activacion de servicios 
    pub_home     = rospy.Publisher("Movimiento/Home", Bool, queue_size=1)
    pub_posicion = rospy.Publisher("Movimiento/Posicion", Posicion, queue_size=1)
    pub_activar  = rospy.Publisher("Movimiento/Activar", Bool, queue_size=1)
    pub_pinza    = rospy.Publisher("Gripper/Activar", Int16, queue_size=1)
    # Crear la máquina de estado
    sm = crear_maquina_estado()
    #sis = smach_ros.IntrospectionServer('my_smach_introspection_server', sm, '/SM_ROOT')
    #sis.start()
    # Ejecutar la máquina de estado
    outcome = sm.execute()
    rospy.loginfo("La máquina de estado ha finalizado con resultado: {}".format(outcome))
    # Create and start the introspection server
    

if __name__ == '__main__':
    B_Datos = Base_Datos()
    Contro_Msg  = controlador_msg()
    main()

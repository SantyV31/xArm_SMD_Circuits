#!/usr/bin/env python3
import rospy
from xarm_smd_ros.msg import ListaComponentes,Posicion,Componente
import copy,sys

class Base_Datos():
    def __init__(self):
        # Diccionario - Componentes disponibles 
        self.dic_almacen = {
                                "Resistencias": {},
                                "Borneras": {},
                                "Capacitores":{},
                                "Diodos":{},
                                "Leds":{}
                            }
        # Diccionario - Circuitos diseñados
        self.dic_circuitos         = {}
        # Diccionario -  Espacios de trabajo
        self.dic_area_componentes  = {}
        self.dic_area_circuito     = {}
        # Diccionario - Circuito a armarse 
        self.componentes_circuito_destino = {}
        self.componentes_circuito_origen  = {}
        # Diccionario - Posicion,Orientacion Robot
        self.robot            = {}
        # Banderas 
        self.b_mensaje        = 0
        self.t_componentes    = 0
        self.t_componentes_encontrados = 0
        # Mensajes en formato ROS
        self.list_componentes = ListaComponentes()
        #self.list_posiciones  = ListaPosiciones()
        # Funciones de inicializacion
        self.orden = 0
        self.Agregar_Espacio()
        self.Agregar_circuitos()
        self.Agregar_Robot()

    def Agregar_Espacio(self):
        # Agrego las coordenadas del espacio de trabajo de la baquelita
        self.dic_area_circuito={
            "x_i": 0.20,
            "x_f": 0.28,
            "y_i": 0.20,
            "y_f": 0.28
        }
        # Agrego las coordenadas del espacio de trabajo del almacen
        self.dic_area_componentes={
            "x_i": 0.20,
            "x_f": 0.28,
            "y_i": -0.29,
            "y_f": -0.28
        }

    def Agregar_Robot(self):
        # Posición y Orientación global del robot
        self.robot = {
            "Pos_X":0,
            "Pos_Y":0,
            "Orientacion": 0
        }
    def Agregar_circuitos(self):
        # Datos de los componentes de los diferentes circuitos diseñados
        # Nombre del circuito:
        # - nombre: Identificador del tipo de componente "Bornera, Resistencia, Capacitor, Diodo"
        # - pos_x,pos_y,Orietancion : Datos globales
        # - Orden : Orden del movimiento 0,1,2...n 
        self.dic_circuitos = {

            "Divisor de voltaje":
            {
                "Componente_1":
                {
                    "nombre": "Capacitor",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0048,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0116,
                    "Valor" : 220,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_2":
                {
                    "nombre": "Capacitor",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.007,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.020,
                    "Valor" : 10,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_3":
                {
                    "nombre": "Resistencia",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.017,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.020,
                    "Valor" : 470,
                    "Orientacion": 90,
                    "Orden" : -1
                },

                "Componente_4":
                {
                   "nombre": "Bornera",
                   "pos_x" : self.dic_area_circuito["x_i"]+0.01,
                   "pos_y" : self.dic_area_circuito["y_i"]+0.03,
                   "Valor" : 2,
                   "Orientacion": 90,
                   "Orden" : -1
               },
                "Etiqueta":1
            },
            "Circuito Led":{
                "Componente_1":
                {
                    "nombre": "Resistencia",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0048,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0116,
                    "Valor" : 120000,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_2":
                {
                    "nombre": "Resistencia",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0130,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0036,
                    "Valor" : 470,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_3":
                {
                    "nombre": "Resistencia",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0130,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0068,
                    "Valor" : 470,
                    "Orientacion": 90,
                    "Orden" : -1
                },

                "Componente_4":
                {
                    "nombre": "Resistencia",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0130,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0099,
                    "Valor" : 470,
                    "Orientacion": 90,
                    "Orden" : -1
                },

                "Componente_5":
                {
                    "nombre": "Resistencia",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0130,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0130,
                    "Valor" : 470,
                    "Orientacion": 90,
                    "Orden" : -1
                },

                "Componente_6":
                {
                    "nombre": "Led",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0185,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0036,
                    "Valor" : 1,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_7":
                {
                    "nombre": "Led",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0185,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0068,
                    "Valor" : 1,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_8":
                {
                    "nombre": "Led",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0185,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0099,
                    "Valor" : 1,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Componente_9":
                {
                    "nombre": "Led",
                    "pos_x" : self.dic_area_circuito["x_i"]+0.0185,
                    "pos_y" : self.dic_area_circuito["y_i"]+0.0130,
                    "Valor" : 1,
                    "Orientacion": 90,
                    "Orden" : -1
                },
                "Etiqueta":2
            }


        
        }

    def Agregar_Almacen(self, listado_mensaje):
        # Utilizo el mensaje obtenido desde la cámara y creo un diccionario con las posiciones globales 
        #  de los componentes en el almacen  
        self.t_componentes = len(listado_mensaje.listacomponentes)

        for componente in listado_mensaje.listacomponentes:
            tipo  = componente.nombre
            x = 0.2-componente.pos_y
            y = componente.pos_x
            pos_x = round (self.dic_area_componentes["x_i"] + componente.pos_x, 5)
            pos_y = round (self.dic_area_componentes["y_i"] - componente.pos_y, 5)
            valor = str(int(componente.valor))
            
            if tipo == "Resistencia":
                if valor not in self.dic_almacen["Resistencias"]:
                    self.dic_almacen["Resistencias"][valor] = {}
                num_resistencia = "r_" +valor+"_"+str(len(self.dic_almacen["Resistencias"][valor]) + 1)
                self.dic_almacen["Resistencias"][valor][num_resistencia] = {"pos_x": pos_x, "pos_y": pos_y, "Estado": 0}
            
            elif tipo == "Bornera":
                if valor not in self.dic_almacen["Borneras"]:
                    self.dic_almacen["Borneras"][valor] = {}
                num_bornera = "b_" +valor+"_" + str(len(self.dic_almacen["Borneras"][valor]) + 1)
                self.dic_almacen["Borneras"][valor][num_bornera] = {"pos_x": pos_x, "pos_y": pos_y, "Estado": 0}
            
            elif tipo == "Capacitor":
                if valor not in self.dic_almacen["Capacitores"]:
                    self.dic_almacen["Capacitores"][valor] = {}
                num_bornera = "c_" +valor+"_" + str(len(self.dic_almacen["Capacitores"][valor]) + 1)
                self.dic_almacen["Capacitores"][valor][num_bornera] = {"pos_x": pos_x, "pos_y": pos_y, "Estado": 0}

            elif tipo == "Diodo":
                if valor not in self.dic_almacen["Diodos"]:
                    self.dic_almacen["Diodos"][valor] = {}
                num_bornera = "d_" +valor+"_" + str(len(self.dic_almacen["Diodos"][valor]) + 1)
                self.dic_almacen["Diodos"][valor][num_bornera] = {"pos_x": pos_x, "pos_y": pos_y, "Estado": 0}
            
            elif tipo == "Led":
                if valor not in self.dic_almacen["Leds"]:
                    self.dic_almacen["Leds"][valor] = {}
                num_bornera = "l_" +valor+"_" + str(len(self.dic_almacen["Leds"][valor]) + 1)
                self.dic_almacen["Leds"][valor][num_bornera] = {"pos_x": pos_x, "pos_y": pos_y, "Estado": 0}
        
        print(self.dic_almacen)
    
    def Componentes_SMD(self,circuito):
        circuito_encontrado =  None
        for componentes, circuitos in self.dic_circuitos.items():
            if circuitos["Etiqueta"] == circuito:
                circuito_encontrado = componentes
                break
        
        if (circuito_encontrado!=None):
            self.componentes_circuito = self.dic_circuitos[circuito_encontrado]
            self.componentes_circuito_destino = {clave: valor for clave, valor in self.componentes_circuito.items() if clave != "Etiqueta"}
            self.componentes_circuito_origen  = copy.deepcopy(self.componentes_circuito_destino)

            # Verificar si existen al menos un elemento de cada componente en el circuito
            orden = 0

            for clave, componente in self.componentes_circuito_destino.items():
                if componente["nombre"] == "Resistencia":
                    aux  = {clave: valor for clave, valor in self.dic_almacen["Resistencias"].items() if clave == str(componente["Valor"])}
                    aux2 = aux[str(componente["Valor"])]
                    for comp, dic in aux2.items():
                        if (aux2[comp]["Estado"]== 0):
                            print("Encontrado")
                            self.componentes_circuito_origen[clave]["pos_x"] = aux2[comp]["pos_x"]
                            self.componentes_circuito_origen[clave]["pos_y"] = aux2[comp]["pos_y"]
                            self.componentes_circuito_origen[clave]["Orden"]  = orden
                            self.componentes_circuito_destino[clave]["Orden"]  = orden
                            self.dic_almacen["Resistencias"][str(componente["Valor"])][comp]["Estado"] = 1
                            self.t_componentes_encontrados +=1
                            break

                if componente["nombre"] == "Bornera":
                    aux  = {clave: valor for clave, valor in self.dic_almacen["Borneras"].items() if clave == str(componente["Valor"])}
                    print("Primero Punto",aux)
                    aux2 = aux[str(componente["Valor"])]
                    for comp, dic in aux2.items():
                        if (aux2[comp]["Estado"]== 0):
                            print("Encontrado")
                            self.componentes_circuito_origen[clave]["pos_x"] = aux2[comp]["pos_x"]
                            self.componentes_circuito_origen[clave]["pos_y"] = aux2[comp]["pos_y"]
                            self.componentes_circuito_origen[clave]["Orden"]  = orden
                            self.componentes_circuito_destino[clave]["Orden"]  = orden
                            self.dic_almacen["Borneras"][str(componente["Valor"])][comp]["Estado"] = 1
                            self.t_componentes_encontrados +=1
                            break
                
                if componente["nombre"] == "Capacitor":
                    aux  = {clave: valor for clave, valor in self.dic_almacen["Capacitores"].items() if clave == str(componente["Valor"])}
                    aux2 = aux[str(componente["Valor"])]
                    for comp, dic in aux2.items():
                        if (aux2[comp]["Estado"]== 0):
                            print("Encontrado")
                            self.componentes_circuito_origen[clave]["pos_x"] = aux2[comp]["pos_x"]
                            self.componentes_circuito_origen[clave]["pos_y"] = aux2[comp]["pos_y"]
                            self.componentes_circuito_origen[clave]["Orden"]  = orden
                            self.componentes_circuito_destino[clave]["Orden"]  = orden
                            self.dic_almacen["Capacitores"][str(componente["Valor"])][comp]["Estado"] = 1
                            self.t_componentes_encontrados +=1
                            break
                
                if componente["nombre"] == "Diodo":
                    aux  = {clave: valor for clave, valor in self.dic_almacen["Diodos"].items() if clave == str(componente["Valor"])}
                    aux2 = aux[str(componente["Valor"])]
                    for comp, dic in aux2.items():
                        if (aux2[comp]["Estado"]== 0):
                            print("Encontrado")
                            self.componentes_circuito_origen[clave]["pos_x"] = aux2[comp]["pos_x"]
                            self.componentes_circuito_origen[clave]["pos_y"] = aux2[comp]["pos_y"]
                            self.componentes_circuito_origen[clave]["Orden"]  = orden
                            self.componentes_circuito_destino[clave]["Orden"]  = orden
                            self.dic_almacen["Diodos"][str(componente["Valor"])][comp]["Estado"] = 1
                            self.t_componentes_encontrados +=1
                            break
                
                if componente["nombre"] == "Led":
                    aux  = {clave: valor for clave, valor in self.dic_almacen["Leds"].items() if clave == str(componente["Valor"])}
                    aux2 = aux[str(componente["Valor"])]
                    for comp, dic in aux2.items():
                        if (aux2[comp]["Estado"]== 0):
                            print("Encontrado")
                            self.componentes_circuito_origen[clave]["pos_x"] = aux2[comp]["pos_x"]
                            self.componentes_circuito_origen[clave]["pos_y"] = aux2[comp]["pos_y"]
                            self.componentes_circuito_origen[clave]["Orden"]  = orden
                            self.componentes_circuito_destino[clave]["Orden"]  = orden
                            self.dic_almacen["Leds"][str(componente["Valor"])][comp]["Estado"] = 1
                            self.t_componentes_encontrados +=1
                            break

                orden += 1
            print(self.componentes_circuito_origen)
            print(self.componentes_circuito_destino)
            print(self.dic_almacen)

            # Calcular el tamaño del diccionario en bytes
            tamaño_diccionario_bytes = sys.getsizeof(self.componentes_circuito_destino)
            print("Tamaño del diccionario:", tamaño_diccionario_bytes, "bytes")
    
    def Comprobar_Componentes(self):
        aux = 1
        for componente, circuito in self.componentes_circuito_origen.items():
            if self.componentes_circuito_origen[componente]["Orden"] == -1:
                print("El componente",componente,"no existe")
                aux = 0
        return aux

    def EliminarComponentes(self):
        self.dic_almacen = {
                                "Resistencias": {},
                                "Borneras": {},
                                "Capacitores":{},
                                "Diodos":{},
                                "Leds":{}
                            }
        self.componentes_circuito_destino = {}
        self.componentes_circuito_origen  = {}
        self.t_componentes    = 0
        self.t_componentes_encontrados = 0

    def Imprimir_Dic(self):
        for i in range(len(self.componentes_circuito_destino.items())):
            nombre_componente = f"Componente_{i+1}"
            print(nombre_componente+": ", self.componentes_circuito_destino[nombre_componente]["nombre"])
    
    def Go_Area_Componente(self):
        msg = Posicion()
        msg.pos_x  = self.dic_area_componentes["x_i"]
        msg.pos_y  = self.dic_area_componentes["y_i"]
        msg.pos_z  = 0.09 #altura que no choque
        msg.giro_x = 180
        msg.giro_y = 0
        msg.giro_z = 0
        msg.vel    = 200
        msg.ace    = 2000
        return msg
    
    def Go_Area_Circuito(self):
        msg = Posicion()
        msg.pos_x  = self.dic_area_circuito["x_i"]
        msg.pos_y  = self.dic_area_circuito["y_i"]
        msg.pos_z  = 0.09 #altura que no choque
        msg.giro_x = 180
        msg.giro_y = 0
        msg.giro_z = 0
        msg.vel    = 200
        msg.ace    = 2000
        return msg
    
    def Go_Componente(self,x,y):
        msg = Posicion()
        msg.pos_x  = x
        msg.pos_y  = y
        msg.pos_z  = 0.0092
        msg.giro_x = 180
        msg.giro_y = 0
        msg.giro_z = 0  #Giro para evitar que se golpee con el micro
        msg.vel    = 200
        msg.ace    = 2000
        return msg
    
    def Go_Circuito(self,x,y):
        msg = Posicion()
        msg.pos_x  = x
        msg.pos_y  = y
        msg.pos_z  = 0.02392
        msg.giro_x = 180
        msg.giro_y = 0
        msg.giro_z = 0
        msg.vel    = 200
        msg.ace    = 2000
        return msg
    
    def Go_Aux(self,x,y):
        msg = Posicion()
        msg.pos_x  = x
        msg.pos_y  = y
        msg.pos_z  = 0.03
        msg.giro_x = 180
        msg.giro_y = 0
        msg.giro_z = 0 # Giro para evitar el golpe 
        msg.vel    = 200
        msg.ace    = 2000
        return msg
    def Cuadrantes(self,x,y):

        rect_top_left = (0.2008, -0.2976)
        rect_bottom_right = (0.2214, -0.3248)

        point = (0.2108, -0.307)

        rows = 5  # Número de filas en la cuadrícula
        cols = 3  # Número de columnas en la cuadrícula
        x1, y1 = rect_top_left
        x2, y2 = rect_bottom_right
        x, y = point

        # Asegurar que el rectángulo esté definido correctamente
        if x1 >= x2 or y1 <= y2:
            raise ValueError("Las coordenadas del rectángulo no son válidas")

        # Calcular el ancho y alto de cada celda
        cell_width = (x2 - x1) / cols
        cell_height = (y1 - y2) / rows

        # Generar puntos intermedios 
        filas    = []
        columnas = []
        puntos_x = []
        puntos_y = []

        for i in range(rows):
            aux = rect_top_left[1] + cell_height/2 + cell_height*i
            filas.append(aux)
        
        for i in range(cols):
            aux = rect_top_left[0] + cell_width*(i) + cell_width/2
            columnas.append(aux)
        
        print(filas)
        print(columnas)
        
        for i in range(rows):
            for j in range(cols):
                puntos_x.append(columnas[j])
                puntos_y.append(filas[i])

        # Verificar si el punto está dentro del rectángulo
        if not (x1 <= x <= x2 and y2 <= y <= y1):
            return None  # El punto está fuera del rectángulo

        # Calcular la columna y fila en la que se encuentra el punto
        col = int((x - x1) // cell_width)
        row = int((y1 - y) // cell_height)  # Invertimos la resta porque y decrece

        # Calcular el número de sección, suponiendo numeración por filas (de izquierda a derecha, de arriba hacia abajo)
        section = row * cols + col + 1  # Sumar 1 para numeración 1-based
        print(section)
        return puntos_x[section-1], puntos_y[section-1]


class controlador_msg():
    def __init__(self):
        self.componente = Componente()
        self.list_componentes = ListaComponentes()
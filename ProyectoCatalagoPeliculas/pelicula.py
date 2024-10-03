# En este archivo va la clase pelicula
import re
import os

class Pelicula:
    def __init__(self, nombre, clasificacion, poster):
        self.__nombre = nombre # Nombre es un atributo privado
        self.clasificacion = clasificacion
        self.imagen = poster

    # Metodo getter para obtener el nombre de la pelicula
    def get_nombre(self):
        return self.__nombre
    
    #Permite buscar si existe una película en el cataálogo
    @staticmethod
    def buscar_pelicula(archivo, pelicula):
        try:
            with open(archivo, 'r', encoding="utf-8") as f:
                for linea in f:
                    if pelicula in linea:
                        return True
                return False
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no existe.")
            return False
    
    @staticmethod
    def obtener_nombre_poster(cadena):
        # Utilizar re.split() para dividir en partes usando el delimitador "-"
        partes = re.split(r'(-)', cadena)
        informacion = ""
        # Encontrar el segundo "-"
        contador_guiones = 0
        for idx, parte in enumerate(partes):
            if parte == "-":
                contador_guiones += 1                         
            if contador_guiones == 2:  
                informacion = "".join(partes[:idx + 1])                
                return ("".join(partes[idx + 1:]),informacion)
        
        # Si no hay suficiente guiones, devolver la cadena completa
        datos=(cadena,informacion)
        return datos

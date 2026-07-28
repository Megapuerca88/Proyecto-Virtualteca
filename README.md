                                           ==========Readme===========
                        Para acceder al programa necesitas ingresar el usuario y la contraseña.

Usuario: Carl
Contraseña:1234

                                           ======Listas globales======
personas_sancionadas = [] #Lista de personas que no pueden ser prestador libros.
libros_prestados = [{}] #Matriz donde almacena el título, id, y nombre de quien se lo prestaron
historial_dia = [] #almance los nuevos prestamos para mostrar como un reporte del día.
deudores = [] #Personas que deben por multas
almananque = [{}] #Fecha e ID del libro de quien se lo lleva
===Subsistemas/funciones===
def cargar_biblioteca() #
def guardar_biblioteca(biblioteca) #
def Renovaciones() #Esta función es la que permite renovar una nueva fecha de préstamo. Contiene la función recursiva donde la fecha actual cambiará a una nueva en lo que sería dos semenas después, es decir, 14 días más para devolverlo.
def iniciar_sesion(): #Esta función es la encargada de pedir iniciar sesión para el usuario que desea acceder al sistema.
def gestionar_personas_vetadas():
def gestionar_libros_prestados():
def ver_resumen_hoy():
def limpiar_pantalla():#Función que únicamente sirve para limpiar la pantalla 
def sistema_regreso(devolver) #Esta es la función donde se realiza los cálculos para generar una multa. Hace uso de recursividad, inicia en 20 pesos y cada día se suma el doble del anterior, es decir, el segundo serán 40 pesos de multa más los 20 pesos del primer día.
def buscando_fechas(id): #Esta función es la que se encarga de buscar la fecha del préstamo para la matriz. No solo hace eso pues, necesitamos convertir str a int para calcular la nueva fecha de préstamo al momento de hacer una renovación.
def sistema_renovacion(año, mes, dia, dos_semanas = 13) #Esta función es el calculo que hace el sistema para generar una nueva fecha de devolución; el subsistema tiene un mini calendario con los días del mes.
def multas() #Aquí está el subsistema que pide ingresar datos para la devolución del libro, se llama multas para identificarlo más rápido y diferenciarlo de la función de regreso.
def ejecutar_menu() #
def registrar_libro(biblioteca) #
def mostrar_libros(biblioteca) #
def menu():

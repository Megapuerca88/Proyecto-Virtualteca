import json
import os

# ==========================================
# MEMORIA GLOBAL DEL SISTEMA
# ==========================================
personas_vetadas = []
libros_prestados = []
historial_dia = []
deudores = []
almananque = [
    {"id": "ab123", "año": "2026", "mes": "4", "dia": "21"},
]

# VARIABLE DE CONTROL DE SEGURIDAD
sesion_iniciada = False


def cargar_biblioteca():
  if os.path.exists("Guardado.txt"):
    with open("Guardado.txt", "r", encoding="utf-8") as archivo:
      datos = json.load(archivo)
      # Devuelve las matrices guardadas
      return (
          datos["deudores"],
          datos["fechas"],
          datos["sancionados"],
          datos["prestamos"],
      )


def guardar_biblioteca(deudores, fechas, sancionados, prestamos):
  # Agrupamos todo en un diccionario
  datos = {
      "deudores": deudores,
      "fechas": fechas,
      "sancionados": sancionados,
      "prestamos": prestamos,
  }

  # Guardamos como texto en formato JSON
  with open("Guardado.txt", "w", encoding="utf-8") as guardado:
    json.dump(datos, guardado, ensure_ascii=False, indent=4)


# ==========================================
# SECCIÓN DE MÓDULOS / FUNCIONES
# ==========================================


def iniciar_sesion():
  global sesion_iniciada  # Global variable para modificascion general

  while True:
    print("\n--- PANTALLA DE INICIO DE SESIÓN ---")
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")

    if usuario == "Carl" and contrasena == "1234":
      print("\n[✓] ¡Bienvenido al sistema, Carl!")
      sesion_iniciada = True  # ¡Validado! Se abre el acceso al sistema
      historial_dia.append(
          f"El usuario '{usuario}' inició sesión correctamente."
      )
      input("Presiona Enter para continuar...")
      return True
    else:
      print(
          "\n[X] ERROR: Usuario o contraseña incorrectos. Inténtalo de nuevo."
      )
      historial_dia.append(
          f"Intento de inicio de sesión fallido con el usuario '{usuario}'."
      )
      opcion = input("¿Deseas reintentar? (s/n): ").lower()
      if opcion != "s":
        return False


def gestionar_personas_vetadas():
  print("\n--- SECCIÓN DE PERSONAS VETADAS ---")
  print("[1] Ver lista actual")
  print("[2] Vetar a una nueva persona")
  sub_opcion = input("Selecciona una acción (1-2): ")

  if sub_opcion == "1":
    print("\n-- Lista de Vetados --")
    if len(personas_vetadas) == 0:
      print("Por ahora no hay personas vetadas.")
    else:
      for persona in personas_vetadas:
        print(f"• {persona}")
    historial_dia.append("Se consultó la lista de personas vetadas.")

  elif sub_opcion == "2":
    print("\n-- Registrar Nuevo Veto --")
    nombre = input("Nombre de la persona: ")
    motivo = input("Motivo del veto: ")

    nuevo_vetado = f"{nombre} - Motivo: {motivo}."
    personas_vetadas.append(nuevo_vetado)

    print(f"\n[✓] {nombre} ha sido agregado a la lista de vetados.")
    historial_dia.append(f"Se vetó a: {nombre}.")
  else:
    print("\n[!] Opción incorrecta.")

  print("")
  input("Presiona Enter para regresar al menú...")


# HISTORIAL DE PRESTAMOS Y REGISTRAR UN NUEVO PRESTAMO
def gestionar_libros_prestados():
  global almananque
  global libros_prestados
  global historial_dia

  print("\n--- SECCIÓN DE LIBROS PRESTADOS ---")
  print("[1] Ver libros prestados")
  print("[2] Registrar nuevo préstamo")
  sub_opcion = input("Selecciona una acción (1-2): ")

  if sub_opcion == "1":
    print("\n-- Registro de Préstamos --")
    if len(libros_prestados) == 0:
      print("No hay libros prestados en el registro.")
    else:
      for libro in libros_prestados:
        print(f"• {libro}")
    historial_dia.append("Se consultó la lista de libros prestados.")

  elif sub_opcion == "2":
    print("\n-- Registrar Nuevo Préstamo --")
    titulo = input("Título del libro: ")
    usuario_prestamo = input("¿A quién se le presta?: ")
    id_libro = input("ID del libro: ")

    # Pide la fecha completa del préstamo
    fecha_input = input(
        "Fecha de préstamo (Año Mes Día Ej. 2026 4 21): "
    ).split()
    año = fecha_input[0] if len(fecha_input) > 0 else "2026"
    mes = fecha_input[1] if len(fecha_input) > 1 else "1"
    dia = fecha_input[2] if len(fecha_input) > 2 else "1"

    nuevo_prestamo = (
        f"'{titulo}' (ID: {id_libro}) - Prestado a: {usuario_prestamo}"
    )
    libros_prestados.append(nuevo_prestamo)

    # Guarda la ID y Fecha en almananque para usar en Renovaciones/Devolución
    almananque.append({"id": id_libro, "año": año, "mes": mes, "dia": dia})

    print(f"\n[✓] Préstamo de '{titulo}' registrado con éxito.")
    historial_dia.append(
        f"Se prestó el libro '{titulo}' (ID: {id_libro}) a {usuario_prestamo}."
    )
  else:
    print("\n[!] Opción incorrecta.")

  print("")
  input("Presiona Enter para regresar al menú...")


def ver_resumen_hoy():
  print("\n--- RESUMEN DE HOY ---")
  if len(historial_dia) == 0:
    print("No se ha registrado ninguna actividad el día de hoy.")
  else:
    print("Actividades registradas:")
    for accion in historial_dia:
      print(f"- {accion}")

  print("")
  input("Presiona Enter para regresar al menú...")


def limpiar_pantalla():
  print("\n" * 5)


def Renovaciones():
  global libros_prestados
  global almananque
  global prestamos
  global deudores

  print("\n--- RENOVACIÓN DE LIBRO ---")
  print("[1] Buscar fecha de préstamo por ID")
  print("[2] Ingresar fecha de préstamo manualmente")
  modo = input("Selecciona una opción (1-2): ")

  if modo == "1":
    id_renovado = input("Escriba la ID del libro a renovar: ")
    encontrado = False
    for codigo in almananque:
      if id_renovado == codigo["id"]:
        año, mes, dia = buscando_fechas(id_renovado)
        encontrado = True
        break

    if not encontrado:
      print("[!] ID no encontrada en el registro.")
      return

  elif modo == "2":
    id_renovado = input("Escriba la ID del libro a renovar: ")
    año = int(input("Escriba el Año: "))
    mes = int(input("Escriba el Mes: "))
    dia = int(input("Escriba el Día: "))
  else:
    print("[!] Opción inválida.")
    return

  # Calcula la renovación usando la función del sistema
  renovado = sistema_renovacion(año, mes, dia)
  new_año, new_mes, new_dia = renovado

  # Actualiza la fecha en almananque
  for codigo in list(almananque):
    if id_renovado == codigo["id"]:
      almananque.remove(codigo)
      break

  almananque.append({
      "id": str(id_renovado),
      "año": str(new_año),
      "mes": str(new_mes),
      "dia": str(new_dia),
  })
  print(f"[✓] La nueva fecha de devolución es: {new_año}-{new_mes}-{new_dia}")
  historial_dia.append(f"Se renovó el libro con ID '{id_renovado}'.")


def sistema_regreso(devolver):
  print()
  if devolver == 1:
    multa = 20
  else:
    multa = (20 * (2 ** (devolver - 1))) + sistema_regreso(devolver - 1)
  return multa


def buscando_fechas(id):
  for buscar_fecha in almananque:
    if id == buscar_fecha["id"]:
      año = int(buscar_fecha["año"])
      mes = int(buscar_fecha["mes"])
      dia = int(buscar_fecha["dia"])
      print("La fecha del prestamo es: ", año, "-", mes, "-", dia)
      return año, mes, dia


def sistema_renovacion(año, mes, dia, dos_semanas=13):
  dia += 1
  calendario = {
      1: 31,
      2: 29,
      3: 31,
      4: 30,
      5: 31,
      6: 30,
      7: 31,
      8: 31,
      9: 30,
      10: 31,
      11: 30,
      12: 31,
  }
  if dos_semanas == 0:
    return año, mes, dia
  elif dia > calendario[mes]:
    dia = 1
    mes += 1
    if mes > 12:
      mes = 1
      año += 1
  return sistema_renovacion(año, mes, dia, dos_semanas - 1)


def multas():
  global libros_prestados
  global almananque
  global prestamos
  global deudores

  print("\n--- GESTIÓN DE DEVOLUCIONES Y MULTAS ---")
  print("[1] Registrar devolución de libro")
  print("[2] Quitar / Saldar una multa pendiente")
  modo = input("Selecciona una opción (1-2): ")

  if modo == "1":
    codigo = input("Escriba la ID del libro: ")
    tiempo = input(
        "¿El alumno lo regresó en tiempo y forma? (Escriba en minúsculas): "
    )

    if tiempo == "si":
      print("[✓] Anotado. Se cambió el estado del libro: entregado.")
      for entrego in list(almananque):
        if codigo == entrego["id"]:
          almananque.remove(entrego)
          break

      for libro in list(libros_prestados):
        if isinstance(libro, str) and codigo in libro:
          libros_prestados.remove(libro)
          break

    elif tiempo == "no":
      nombre_vetado = input("Escriba el nombre del estudiante: ")
      dias_pasados = int(input("Escriba los días que no entregó: "))
      resultado = sistema_regreso(dias_pasados)
      print(f"[!] El alumno {nombre_vetado} debe: ${resultado}")

      for entrego in list(almananque):
        if codigo == entrego["id"]:
          almananque.remove(entrego)
          break

      deudores.append({"nombre": nombre_vetado, "deuda": resultado})
      historial_dia.append(
          f"Se registró multa a {nombre_vetado} por ${resultado}."
      )
    else:
      print("[!] Opción no válida. Escriba si o no.")

  elif modo == "2":
    if len(deudores) == 0:
      print("[!] No hay multas ni deudores registrados.")
    else:
      print("\n-- Lista de Deudores --")
      for d in deudores:
        print(f"• {d['nombre']} - Deuda: ${d['deuda']}")

      nombre_quitar = input(
          "\nEscriba el nombre del estudiante al que desea quitar la multa: "
      )
      encontrado = False

      for alumno in list(deudores):
        if alumno["nombre"].lower() == nombre_quitar.lower():
          deudores.remove(alumno)
          encontrado = True
          print(f"[✓] Se ha retirado la multa de '{nombre_quitar}'.")
          historial_dia.append(f"Se quitó la multa a {nombre_quitar}.")
          break

      if not encontrado:
        print(f"[!] No se encontró a '{nombre_quitar}' en la lista.")


def menu():
  biblioteca = cargar_biblioteca()
  while True:
    print("\n--- Biblioteca ---")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
      registrar_libro(biblioteca)
    elif opcion == "2":
      mostrar_libros(biblioteca)
    elif opcion == "3":
      print("Hasta luego.")
      break
    else:
      print("Opción inválida.")


def registrar_libro(biblioteca):
  titulo = input("Título: ")
  autor = input("Autor: ")
  año = input("Año: ")
  libro = {"titulo": titulo, "autor": autor, "año": año}
  if biblioteca is not None:
    biblioteca.append(libro)
    guardar_biblioteca(
        deudores, almananque, personas_vetadas, libros_prestados
    )
  print("Libro registrado con éxito.")


def mostrar_libros(biblioteca):
  if not biblioteca:
    print("No hay libros registrados.")
  else:
    for i, libro in enumerate(biblioteca, 1):
      print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['año']})")


# ==========================================
# PROCESO PRINCIPAL DEL MENÚ
# ==========================================

if iniciar_sesion():

  while True:
    print("\n=========================================")
    print("       SISTEMA DE GESTIÓN BIBLIOTECA     ")
    print("=========================================")
    print(" [1] - Gestionar Personas Vetadas")
    print(" [2] - Gestionar Libros Prestados")
    print(" [3] - Ver Resumen de Hoy (Bitácora)")
    print(" [4] - Registro Libros")
    print(" [5] - Devolución / Multas")
    print(" [6] - Renovación")
    print(" [7] - Salir del Sistema")
    print("=========================================")

    if sesion_iniciada:
      print(" Estado: [✓] Conectado como Carl")
    else:
      print(" Estado: [X] No has iniciado sesión")
    print("=========================================")

    opcion = input("Selecciona una opción (1-7): ")

    if opcion == "1":
      gestionar_personas_vetadas()

    elif opcion == "2":
      gestionar_libros_prestados()

    elif opcion == "3":
      ver_resumen_hoy()

    elif opcion == "4":
      menu()

    elif opcion == "5":
      multas()

    elif opcion == "6":
      Renovaciones()

    elif opcion == "7":
      guardar_biblioteca(
          deudores, almananque, personas_vetadas, libros_prestados
      )
      print("\nArchivo guardado correctamente.")
      print("Gracias por entrar a la Virtualteca. ¡Hasta luego!")
      break

    else:
      print("\n[!] Opción no válida. Por favor, elige un número del 1 al 7.")
      input("Presiona Enter para reintentar...")
# Actividad 2.3 Llamada a archivo de texto

import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(ruta_actual, "equipos_intep.txt")
ruta_reporte = os.path.join(ruta_actual, "reporte_intep.txt")

disponibles = 0
en_mantenimiento = 0
total_lineas = 0

with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            total_lineas += 1
            datos = linea.split(",")
            if len(datos) == 3:
                estado = datos[2].strip().lower()
                if estado == "disponible":
                    disponibles += 1
                elif estado == "en mantenimiento":
                    en_mantenimiento += 1

contenido_reporte = f"""REPORTE DE ESTADO DE EQUIPOS - INTEP
====================================
Total de equipos analizados: {total_lineas}
- Equipos disponibles: {disponibles}
- Equipos en mantenimiento: {en_mantenimiento}
"""

with open(ruta_reporte, "w", encoding="utf-8") as reporte:
    reporte.write(contenido_reporte)

print("¡Proceso completado con éxito! Se ha generado el archivo reporte_intep.txt.")
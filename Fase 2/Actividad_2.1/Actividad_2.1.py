# Actividad 2.1 Correcion y señalizacion de errores en el codigo

class Equipo:

    # Error 1: estaba escrito como **init**, debe ser __init__ para que funcione el constructor
    def __init__(self, codigo, tipo):

        self.codigo = codigo
        self.tipo = tipo
        self.estado = "disponible"


    # Error 2: faltaba : al final de la función
    def asignar(self, responsable):

        self.estado = "asignado a " + responsable
        return self.estado



class PC(Equipo):

    # Error 3: estaba escrito como **init**, debe ser __init__
    def __init__(self, codigo, procesador):

        # Error 4: estaba mal escrito el llamado al constructor de la clase padre
        super().__init__(codigo, "PC")

        self.procesador = procesador


    def asignar(self, responsable):

        if self.estado == "disponible":

            return super().asignar(responsable)

        else:

            # Error 6: se mejora el mensaje de la excepción para identificar mejor el problema
            raise Exception("El equipo ya está asignado a otro responsable")



class Impresora(Equipo):

    # Error 5: estaba escrito como **init**, debe ser __init__
    def __init__(self, codigo, tipo_impresion):

        super().__init__(codigo, "Impresora")

        self.tipo_impresion = tipo_impresion



inventario = [
    PC("INT-001", "i5"),
    PC("INT-002", "i7"),
    Impresora("INT-003", "Láser")
]


for equipo in inventario:

    try:

        print(equipo.asignar("Juan"))
        print(equipo.asignar("María"))

    except Exception as e:

        # Error 7: faltaba cerrar el paréntesis del print
        print(f"Error: {e}")
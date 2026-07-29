**Actividad 2.1 Tabla de derupacion del codigo erroneo**

| # | Línea | Error encontrado | Tipo (sintaxis/lógico) | Corrección |
|---|---|---|---|---|
| 1 | `def \*\*init\*\*(self, codigo, tipo):` | El nombre del constructor estaba escrito de forma incorrecta. En Python debe ser `__init__` para que funcione al crear los objetos. | Sintaxis | `def __init__(self, codigo, tipo):` |
| 2 | `def asignar(self, responsable)` | Faltaba colocar los dos puntos al final de la línea, por eso el programa generaba error. | Sintaxis | `def asignar(self, responsable):` |
| 3 | `def \*\*init\*\*(self, codigo, procesador):` | El constructor de la clase PC tenía el mismo error de escritura. | Sintaxis | `def __init__(self, codigo, procesador):` |
| 4 | `super().\*\*init\*\*(codigo, "PC")` | La forma de llamar al constructor de la clase padre estaba incorrecta. | Sintaxis | `super().__init__(codigo, "PC")` |
| 5 | `def \*\*init\*\*(self, codigo, tipo_impresion):` | El constructor de la clase Impresora estaba mal escrito y no funcionaba correctamente. | Sintaxis | `def __init__(self, codigo, tipo_impresion):` |
| 6 | `super().\*\*init\*\*(codigo, "Impresora")` | La llamada al constructor de la clase principal tenía un error de sintaxis. | Sintaxis | `super().__init__(codigo, "Impresora")` |
| 7 | `self.tipo\_impresion = tipo\_impresion` | El atributo tenía caracteres incorrectos (`\`) que no son necesarios en Python. | Sintaxis | `self.tipo_impresion = tipo_impresion` |
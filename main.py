class Empresa:
    def __init__(self, nombre,num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.lista_deptos = {}

class Departamento:
    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre
        self.lista_empleados = {}

class Empleado:
    def __init__(self, ID, nombre, puesto, salario):
        self.ID = ID
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario


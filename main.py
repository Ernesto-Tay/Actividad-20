# ID, Nombre y puesto son privados para evitar cualquier tipo de cambios, pero "salario" es restringido para admitir cambios seguros.
class Empleado:
    def __init__(self,ID,nombre,puesto,salario):
        self.__ID = ID
        self.__nombre = nombre
        self.__puesto = puesto
        self._salario = salario

# ID y Nombre son privados para evitar cambios, pero la lista "empleados" es restringida para permitir cambios controlados
class Departamento:
    def __init__(self,ID,nombre):
        self.__ID = ID
        self.__nombre = nombre
        self._empleados = []

# Lo mismo que en la clase "Departamento"
class Empresa:
    def __init__(self,ID,nombre):
        self.__ID = ID
        self.__nombre = nombre
        self._deptos = []
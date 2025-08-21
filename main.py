# ID, Nombre y puesto son privados para evitar cualquier tipo de cambios, pero "salario" es restringido para admitir cambios seguros.
class Empleado:
    def __init__(self,ID,nombre,puesto,salario):
        self.__ID = ID
        self.__nombre = nombre
        self.__puesto = puesto
        self._salario = salario

    def getID(self):
        return self.__ID
    def getNombre(self):
        return self.__nombre
    def getPuesto(self):
        return self.__puesto

    def getSalario(self):
        return self._salario
    def updateSalario(self,salario):
        self._salario = salario


# ID y Nombre son privados para evitar cambios, pero la lista "empleados" es restringida para permitir cambios controlados
class Departamento:
    def __init__(self,ID,nombre):
        self.__ID = ID
        self.__nombre = nombre
        self._empleados = []

    def getID(self):
        return self.__ID
    def getNombre(self):
        return self.__nombre
    def getEmpleados(self):
        return self._empleados

    def updateEmpleados(self,empleados_list):
        self._empleados = empleados_list


# Lo mismo que en la clase "Departamento"
class Empresa:
    def __init__(self,ID,nombre):
        self.__ID = ID
        self.__nombre = nombre
        self._deptos = []

    def getID(self):
        return self.__ID
    def getNombre(self):
        return self.__nombre

    def getDeptos(self):
        return self._deptos
    def updateDeptos(self,deptos_list):
        self._deptos = deptos_list

empresa = Empresa("123","wasa")
class ConsolaPrints:
    def mostrarDeptos(empresa):
        deptos_list = empresa.getDeptos()
        if not deptos_list:
            print("No hay departamentos asignados aún")
        else:
            print("\n" + "-"*10 + " LISTA DE DEPARTAMENTOS " + "-"*10)
            print("ID".ljust(20) + "NOMBRE".ljust(35) + "NO. EMPLEADOS".ljust(20))
            for depto in deptos_list:
                print(str(depto.getID()).ljust(20) +str(depto.getNombre()).ljust(35) + str(len(depto.getEmpleados())).ljust(20))

    def obtenerDepto(empresa,nombre_depto):
        deptos_list = empresa.getDeptos()
        if not deptos_list:
            print("No hay departamentos asignados aún")
        else:
            for depto in deptos_list:
                if depto.getNombre() == nombre_depto:
                    return depto
            if not any(nombre_depto == depto.getNombre() for depto in deptos_list):
                return False

    def mostrarEmpleados(depto):
        empleados_list = depto.getEmpleados()
        if not empleados_list:
            print("No hay empleados en el departamento")
        else:
            print("\n" + "-" * 10 + " LISTA DE EMPLEADOS " + "-" * 10)
            print("ID".ljust(20) + "NOMBRE".ljust(35) + "PUESTO".ljust(20)+ "SALARIO".ljust(20))
            for empleado in empleados_list:
                print(str(empleado.getID()).ljust(20) + str(empleado.getNombre()).ljust(35) + str(empleado.getPuesto()).ljust(20)+ f"Q{empleado.getSalario()}".ljust(20))

    def obtenerEmpleado(depto, nombre_empleado):
        empleados_list = depto.getEmpleados()
        if not empleados_list:
            print("No hay empleados en el departamento")
        else:
            for empleado in empleados_list:
                if empleado.getNombre() == nombre_empleado:
                    return empleado
            if not any(nombre_empleado == empleado.getNombre() for empleado in empleados_list):
                return False



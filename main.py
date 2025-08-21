class Empleado:
    def __init__(self, ID, nombre, puesto, salario):
        self.ID = ID
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario


class Departamento:
    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre
        self.lista_empleados = []

    def agregar_empleado(self, empleado):
        self.lista_empleados.append(empleado)
        print("Empleado agregado exitosamente")

    def mostrar_empleados(self):
        if not self.lista_empleados:
            print("No hay empleados en este departamento")
        else:
            print("\n"+"-"*10 + " LISTA DE EMPLEADOS " + "-"*10)
            print("ID".ljust(20) + "NOMBRE".ljust(35) + "PUESTO".ljust(20) + "SALARIO".ljust(20))
            for empleado in self.lista_empleados:
                print(empleado.ID.ljust(20) + empleado.nombre.ljust(35) + empleado.puesto.ljust(20) + f"Q{empleado.salario}".ljust(20))

    def eliminar_empleado(self, id):
        deletion = False
        for empleado in self.lista_empleados:
            if empleado.ID == id:
                deletion = True
                self.lista_empleados.remove(empleado)
                print("Empleado eliminado exitosamente")
        if not deletion:
            print("No hay empleado con esa ID")


class Empresa:
    def __init__(self, nombre,num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.lista_deptos = []

    def agregar_depto(self, depto):
        self.lista_deptos.append(depto)
        print("Empleado agregado exitosamente")

    def mostrar_deptos(self):
        if not self.lista_deptos:
            print("No hay empleados en este departamento")
        else:
            print("\n"+"-"*10 + " LISTA DE DEPTOS " + "-"*10)
            print("ID".ljust(20) + "NOMBRE".ljust(35) + "EMPLEADOS".ljust(20))
            for depto in self.lista_deptos:
                print(depto.ID.ljust(20) + depto.nombre.ljust(20) + str(len(depto.lista_empleados)).ljust(20))



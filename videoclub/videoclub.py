class Videoclub():
    def __init__(self, nombre):
        self.nombre = nombre
        self.socios = []

    def buscar_socio(self, codigo):
        for i in range(len(self.socios)):
            if self.socios[i].codigo == codigo:
                return i
        return -1

    def adicionar_socio(self, socio):
        if self.buscar_socio(socio.codigo) == -1:
            self.socios.append(socio)
            return True
        return False

    def listar_socio(self):
        for socio in self.socios:
            print('*******')
            socio.mostrar_socio()

    def eliminar_socio(self, codigo):
        pos = self.buscar_socio(codigo)

        if pos != -1:
            del(self.socios[pos])
            return True
        return False

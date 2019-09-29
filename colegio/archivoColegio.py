import pickle

class ArchivoColegio:

    def __init__(self, nombre_archivo):
        self.__nombre_archivo = nombre_archivo

    def guardar(self, data):
        archivo = open(self.__nombre_archivo, 'wb')
        pickle.dump(data, archivo)
        archivo.close()

    def cargar(self):
        try:
            archivo = open(self.__nombre_archivo, 'rb')
            data = pickle.load(archivo)
            archivo.close()
        except EOFError:
            data = None
        return data
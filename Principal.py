from Funciones import funciones

class principal:
    __f = funciones()

    def ejecutarPrograma(self):
        self.__f.menuInicial()
#-----------------------------------------------------------------------

p = principal()
p.ejecutarPrograma()
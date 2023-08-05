class Oper:
    def __init__(self, a:int, b:int) -> None:
        self.__a = a
        self.__b = b

    def suma(self):
        return self.__a + self.__b
    
    def resta(self):
        return self.__a - self.__b
    
    def multiplicacion(self):
        return self.__a * self.__b
    
    def divicion(self):
        return self.__a / self.__b
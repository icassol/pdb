class ColaEstatica:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.cola = [None] * capacidad_maxima
        self.frente = 0
        self.fondo = 0

    def esta_vacia(self):
        return self.frente == self.fondo

    def esta_llena(self):
        siguiente_fondo = (self.fondo + 1) % self.capacidad_maxima
        return siguiente_fondo == self.frente

    def encolar(self, elemento):
        if self.esta_llena():
            raise OverflowError("La cola está llena")

        self.cola[self.fondo] = elemento
        self.fondo = (self.fondo + 1) % self.capacidad_maxima

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        elemento = self.cola[self.frente]
        self.cola[self.frente] = None  # opcional (limpieza)
        self.frente = (self.frente + 1) % self.capacidad_maxima
        return elemento

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        return self.cola[self.frente]

    def mostrar(self):
        print(self.cola)

cola = ColaEstatica(5)

cola.encolar(10)
cola.encolar(20)
cola.encolar(30)

print("Cola:", cola.cola)

print("Peek:", cola.peek())

print("Desencolar:", cola.desencolar())
print("Desencolar:", cola.desencolar())

cola.mostrar()

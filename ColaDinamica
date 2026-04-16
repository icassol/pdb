class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ColaDinamica:
    def __init__(self):
        self.frente = None
        self.fondo = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.fondo = nuevo_nodo
        else:
            self.fondo.siguiente = nuevo_nodo
            self.fondo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        dato = self.frente.dato

        if self.frente is self.fondo:
            self.frente = None
            self.fondo = None
        else:
            self.frente = self.frente.siguiente

        return dato

    def frente_cola(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        return self.frente.dato

    def mostrar(self):
        actual = self.frente
        elementos = []

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        print("Frente -> " + " -> ".join(elementos) + " <- Fondo")

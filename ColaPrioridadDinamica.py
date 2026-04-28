class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad   # número mayor = mayor prioridad

    def __str__(self):
        return f"{self.nombre}(P{self.prioridad})"


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ColaPrioridadDinamica:
    def __init__(self):
        self.frente = None
        self.fondo = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)

        # Caso 1: cola vacía
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.fondo = nuevo_nodo
            return

        # Caso 2: insertar al frente
        if dato.prioridad > self.frente.dato.prioridad:
            nuevo_nodo.siguiente = self.frente
            self.frente = nuevo_nodo
            return

        # Caso 3: buscar posición intermedia
        actual = self.frente

        while (actual.siguiente is not None and
               actual.siguiente.dato.prioridad >= dato.prioridad):
            actual = actual.siguiente

        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

        # Si quedó último, actualizar fondo
        if nuevo_nodo.siguiente is None:
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


# -------------------------
# Ejemplo de uso
# -------------------------

cola = ColaPrioridadDinamica()

cola.encolar(Tarea("Proceso A", 1))
cola.encolar(Tarea("Proceso B", 3))
cola.encolar(Tarea("Proceso C", 2))
cola.encolar(Tarea("Proceso D", 3))
cola.encolar(Tarea("Proceso E", 1))

cola.mostrar()

print("\nAtendiendo:")
while not cola.esta_vacia():
    print("Sale:", cola.desencolar())

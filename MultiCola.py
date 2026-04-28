class Turno:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad   # número mayor = mayor prioridad

    def __str__(self):
        return f"{self.nombre}(P{self.prioridad})"


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

    def mostrar(self):
        actual = self.frente
        elementos = []

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        if elementos:
            print("Frente -> " + " -> ".join(elementos) + " <- Fondo")
        else:
            print("Cola vacía")


class MultiCola:
    def __init__(self):
        self.cola_prioridad_1 = ColaDinamica()
        self.cola_prioridad_2 = ColaDinamica()
        self.cola_prioridad_3 = ColaDinamica()

    def encolar(self, turno):
        if turno.prioridad == 1:
            self.cola_prioridad_1.encolar(turno)
        elif turno.prioridad == 2:
            self.cola_prioridad_2.encolar(turno)
        elif turno.prioridad == 3:
            self.cola_prioridad_3.encolar(turno)
        else:
            raise ValueError("Prioridad inválida. Debe ser 1, 2 o 3.")

    def desencolar(self, prioridad):
        if prioridad == 1:
            return self.cola_prioridad_1.desencolar()
        elif prioridad == 2:
            return self.cola_prioridad_2.desencolar()
        elif prioridad == 3:
            return self.cola_prioridad_3.desencolar()
        else:
            raise ValueError("Prioridad inválida. Debe ser 1, 2 o 3.")

    def mostrar(self):
        print("Cola prioridad 1:")
        self.cola_prioridad_1.mostrar()

        print("\nCola prioridad 2:")
        self.cola_prioridad_2.mostrar()

        print("\nCola prioridad 3:")
        self.cola_prioridad_3.mostrar()


# -------------------------
# Ejemplo de uso
# -------------------------

multicola = MultiCola()

multicola.encolar(Turno("Ana", 1))
multicola.encolar(Turno("Luis", 1))
multicola.encolar(Turno("Marta", 2))
multicola.encolar(Turno("Pedro", 3))
multicola.encolar(Turno("Sofía", 2))
multicola.encolar(Turno("Juan", 3))

multicola.mostrar()

print("\nAtendiendo un turno de prioridad 1:")
print(multicola.desencolar(1))

print("\nAtendiendo un turno de prioridad 2:")
print(multicola.desencolar(2))

print("\nEstado final:")
multicola.mostrar()

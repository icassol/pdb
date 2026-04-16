class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Insertar al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    # Eliminar un elemento
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    # eliminar cabeza
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False  # no encontrado

    # Buscar un elemento
    def buscar(self, dato):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

    # Mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        elementos = []

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        print(" -> ".join(elementos))

if __name__ == "__main__":
    lista = ListaEnlazada()

    print("Insertar elementos al inicio:")
    lista.insertar_inicio(3)
    lista.insertar_inicio(1)
    lista.insertar_inicio(0)
    lista.mostrar()  # 0 -> 1 -> 3

    print("\nInsertar elementos al final:")
    lista.insertar_final(5)
    lista.insertar_final(7)
    lista.mostrar()  # 0 -> 1 -> 3 -> 5 -> 7

    print("\nBuscar elementos:")
    print("¿Está el 3?", lista.buscar(3))
    print("¿Está el 10?", lista.buscar(10))

    print("\nEliminar elementos:")
    lista.eliminar(3)
    lista.mostrar()  # 0 -> 1 -> 5 -> 7

    lista.eliminar(0)  # eliminar cabeza
    lista.mostrar()  # 1 -> 5 -> 7

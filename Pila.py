class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    def __init__(self):
        self.tope = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo = Nodo(dato, self.tope)
        self.tope = nuevo
        self._tamanio += 1

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")

        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self._tamanio -= 1
        return dato

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")

        return self.tope.dato

    def tamanio(self):
        return self._tamanio

    def __str__(self):
        elementos = []
        actual = self.tope
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "Tope -> " + " -> ".join(elementos)


# -------------------------
# Test de uso
# -------------------------
if __name__ == "__main__":
    pila = Pila()

    print("¿La pila está vacía?", pila.esta_vacia())

    pila.push(10)
    pila.push(20)
    pila.push(30)

    print("Pila luego de apilar 10, 20 y 30:")
    print(pila)

    print("Elemento en el tope (peek):", pila.peek())
    print("Tamaño actual:", pila.tamanio())

    print("Desapilado (pop):", pila.pop())
    print("Pila después de pop:")
    print(pila)

    print("Desapilado (pop):", pila.pop())
    print("Desapilado (pop):", pila.pop())

    print("¿La pila está vacía ahora?", pila.esta_vacia())

    # Descomentar para probar error
    # pila.pop()
    
    
    
    

from fila_array import FilaArray

class ElementoDuplicado(Exception):
    pass

class SetWithQueue:
    def __init__(self):
        self._fila_dados = FilaArray()

    def list(self):
        fila_temp = FilaArray()
        itens = []

        while len(self._fila_dados) > 0:
            atual = self._fila_dados.dequeue()  
            fila_temp.enqueue(atual)              
            itens.append(atual)             
            
        while len(fila_temp) > 0:
            self._fila_dados.enqueue(fila_temp.dequeue())

        return itens

    def size(self):
        return len(self._fila_dados)

    def add(self, elemento):
        if not self.contains(elemento):
            self._fila_dados.enqueue(elemento)
            return True


    def remove(self, elemento):
        if not self.contains(elemento):
            raise ValueError(f'O elemento {elemento} não está presente no conjunto.')

        nova_fila = FilaArray()
        while len(self._fila_dados) > 0:
            atual = self._fila_dados.dequeue()
            if atual != elemento:
                nova_fila.enqueue(atual)

        self._fila_dados = nova_fila

    def contains(self, elemento):
        fila_temp = FilaArray()
        encontrado = False

        while len(self._fila_dados) > 0:
            atual = self._fila_dados.dequeue()
            fila_temp.enqueue(atual)
            if atual == elemento:
                encontrado = True

        while len(fila_temp) > 0:
            self._fila_dados.enqueue(fila_temp.dequeue())

        return encontrado

    def __str__(self):
        return f"SetWithQueue({self.list()})"

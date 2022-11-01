"""
Node
    value: int
    next
    def update_value
Lista enlazada
    Métodos:
    add(node: Node) -> void
    print() -> void
"""

# Creamos Nodos: 

def check_int(funcion):
    def aux_funcion(self,value,next=None):
        if type(value)==int:
            return funcion(self, value, next)
        else:
            raise Exception('parametro erroneo')
    return aux_funcion        

class Node():
    @check_int
    def __init__(self, value:int, next=None):
        self.value = value
        self.next  = next

# Creamos la clase "linkedList"
class Linkedlist():
    def __init__(self):
        self.head = None
    
    def add_node():




node = Node(1.5)
print(node.value)


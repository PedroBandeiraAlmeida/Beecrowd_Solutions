#estrutura basica de um nó
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Adiciona um elemento ao final da lista
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # exibe os elementos da lista
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

    # Procura um valor na lista
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return - 1 # Retorna -1 se o valor não for encontrado
    
    # Remove um elemento da lista
    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print('Valor não encontrado na lista!')

    def insert_at(self, index, data):
        new_node = Node(data)
        current = self.head
        prev = None
        i = 0
        while current:
            if i == index:
                if prev is None:
                    self.head = new_node
                else:
                    prev.next = new_node
                new_node.next = current
                return
            prev = current
            current = current.next
            i += 1
        if index > i:
            prev.next = new_node
        

ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.insert_at(5, 5)


print("Lista encadeada: ")
ll.display()
print(ll.search(20))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str: 
        return str(self.data)

class LinkedList():
    def __init__(self):
        self.head = None
        self._size = 0
        
        
    def inserir(self, element):
        if self.head: 
            pointer = self.head
            while pointer.next: 
                pointer = pointer.next

            pointer.next = Node(element)

        else:
            self.head = Node(element)

        self._size +=1 
    
    def remove(self, element):
        if self.head is None:
            raise ValueError('{} - NOT FOUND'.format(element))
        elif self.head.data == element:
            self.head = self.head.next
            self._size -= 1
            return 'DELETADO'
        else:
            prev = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    prev.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return 'DELETADO'
                else:
                    prev = pointer
                    pointer = pointer.next
            
            raise ValueError('{} - NOT FOUND'.format(element))

    def index(self, element): 
        pointer = self.head
        i = 0

        while pointer: 
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
def return_ascii(character):
    return ord(character)

def hash_function(word, table_size):
    total_value = 0
    element_position = 0

    for element in word:
        element_position += 1
        ascii_value = return_ascii(element) * element_position
        total_value += ascii_value
    
    return (total_value * 17) % table_size

def main():

    initial_configs = input().split()
    table_size = int(initial_configs[0])
    n_entrance = int(initial_configs[1])

    hash_table = [None] * table_size

    i = 0
    while i < n_entrance:
        name = input().split()[1]
        position = hash_function(name, table_size)
        hash_table[position] = LinkedList()
        hash_table[position].inserir(name)
        

main()
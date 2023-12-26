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
        node = Node(element)
        node.next = self.head
        self.head = node

        self._size +=1 
    
    def remove(self, element):
        if self.head is None:
            return None
        elif self.head.data == element:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            prev = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    prev.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                else:
                    prev = pointer
                    pointer = pointer.next
            
            return None

    def index(self, element): 
        pointer = self.head
        i = 0

        while pointer: 
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        return None

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
        if not hash_table[position]:
            hash_table[position] = LinkedList()
        hash_table[position].inserir(name)

        i += 1

    n_ops = int(input())
    j = 0

    while j < n_ops:
        operation_name = input().split()
        operation = operation_name[0]
        name = operation_name[1]
        position = hash_function(name, table_size)

        if operation == 'GET':
            if hash_table[position]:
                idx_in_position = hash_table[position].index(name) + 1

            if idx_in_position is None or hash_table[position] is None:
                print('{} - NOT FOUND'.format(position))
            else:
                print(position, idx_in_position)

        elif operation == 'POST':
            if not hash_table[position]:
                hash_table[position] = LinkedList()
            hash_table[position].inserir(name)

        else:
            resultado = hash_table[position].remove(name)
            
            if resultado is True:
                print('DELETADO')

        j += 1
        

if __name__ == '__main__':
    main()
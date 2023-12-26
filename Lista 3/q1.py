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

print(hash_function('aba', 491))
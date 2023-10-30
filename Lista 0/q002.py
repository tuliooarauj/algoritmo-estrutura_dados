def check_bigger(array):

    n_elements = 0
    biggest_list = array
    n_biggest_list = n_elements

    for element in array:

        n_elements += 1

    if n_elements > n_biggest_list:

        n_biggest_list = n_elements
        biggest_list = array

    return biggest_list

def main():

    running = True
    
    while running:

        array = input()

        if not array == '':
            biggest = check_bigger(array)
        
        runnning = False

    print(biggest)
        

main()

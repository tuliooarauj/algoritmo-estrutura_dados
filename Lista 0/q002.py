def main():

    biggest = ''
    n_biggest_list = 0
    
    while True:

        n_elements = 0
        array = input()

        if not array == '':

            for element in array:

                n_elements += 1

            for element in biggest:

                n_biggest_list += 1

            if n_elements > n_biggest_list:

                n_biggest_list = n_elements
                biggest_list = array

        else:
                
            break
    
    print(biggest_list)
        

if __name__ == '__main__':
    main()
def main():

    n_biggest_list = 0
    idx = 0
    
    while True:

        try:

            idx += 1

            n_elements = 0
            array = input()

            for element in eval(array):

                n_elements += 1

            if idx == 1:

                n_biggest_list = n_elements
                biggest_list = array

            elif n_elements > n_biggest_list:

                n_biggest_list = n_elements
                biggest_list = array
            
        except:
                
            break
    
    print(biggest_list)
        

if __name__ == '__main__':
    main()
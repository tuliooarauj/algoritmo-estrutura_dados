first_element = '{'
second_element = '}'

def check_wellformed(string):

    count_first = 0
    count_second = 0
   
    if first_element in string or second_element in string:
      
      for element in string:

        if element == first_element:
            count_first += 1

        elif element == second_element:
           count_second += 1
    
    if count_first == count_second:
        return True
    else:
       return False

def main():
    
    expression = input()
    
    if check_wellformed(expression):
        print('S')
    else:
        print('N')

main()
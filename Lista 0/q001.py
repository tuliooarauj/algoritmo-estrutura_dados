def check_wellformed(string):
    
    open_bracket = '{'
    close_bracket = '}'

    brackets_count = 0
   
    if open_bracket in string or close_bracket in string:
      
      for element in string:

        if element == open_bracket:
            brackets_count += 1

        elif element == close_bracket:
           brackets_count -= 1
           if brackets_count < 0:
              return False
    
    if brackets_count == 0:
       return True
    else:
       return False
    

def main():
    
    expression = input()
    
    if check_wellformed(expression):
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()

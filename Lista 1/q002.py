class DepartureSolicitation:
    def __init__(self, car_size) -> None:
        self.car_size = car_size
        self.next = None
    
class CarQueue:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def push(self, car_size):
        solicitation = DepartureSolicitation(car_size)

        if self._size == 0:
            #First insert
            self.head = solicitation
            self.tail = solicitation
        
        else:
            self.tail.next = solicitation
            self.tail = solicitation
        
        self._size += 1

    def remove(self):
        if not self._size == 0:
            self.head = self.head.next
        self._size -= 1 

    def boat_walks(self, boat_length, n_carsLeft):
        total = 0
        desenfileirou = False
        while not self.head == None and total <= boat_length:
            car_size = self.head.car_size
            total += car_size
            if total <= boat_length:
                self.remove()
                desenfileirou = True

        if desenfileirou:  
            return True
        elif n_carsLeft > 0:
            return True           
            
    def __len__(self):
        return self._size

def main():
    left_to_right = CarQueue()
    right_to_left = CarQueue()

    n_testCase = int(input())
    i = 0

    while i < n_testCase:
        i += 1

        nTrips = 0
        j = 0 
        length_nCars = input().split() #Input to receive boat length and the number of cars.
        boat_length = int(length_nCars[0]) * 100 #In meters
        numberCars = int(length_nCars[1])

        while j < numberCars: #Car enqueue by side arrive
            j+=1 

            boat_position = 'esquerda'

            carLength_side = input().split() #Input to receive car length and the side wich it arrived.
            car_length = int(carLength_side[0])
            arrived_side = carLength_side[1]

            if arrived_side == 'esquerdo':
                left_to_right.push(car_length)
            else:
                right_to_left.push(car_length)

        while len(left_to_right) != 0 or len(right_to_left) != 0:
            if boat_position == 'esquerda' and left_to_right.boat_walks(boat_length, len(right_to_left)):
                nTrips += 1
                boat_position = 'direita'

            if boat_position == 'direita' and right_to_left.boat_walks(boat_length, len(left_to_right)):
                nTrips += 1
                boat_position = 'esquerda'

        print('Caso {}: {}'.format(i, nTrips))

if __name__ == '__main__':
    main()
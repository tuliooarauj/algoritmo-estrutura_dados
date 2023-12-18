def parent(idx):
    return idx // 2

def left(idx):
    if idx == 0:
        return (idx * 2) + 1
    return idx * 2

def right(idx):
    if idx == 0:
        return (idx * 2) + 2 
    return (idx * 2) + 1

def len_heap(array):
    n = 0
    for _ in array:
        n += 1
    return n

def switch(array, elem1, elem2):
    aux = elem1
    array[elem1] = array[elem2]
    array[elem2] = aux

def max_heapify(array, idx):

    left_idx = left(idx)
    right_idx = right(idx)

    if left_idx <= array_size and array[left_idx] > array[idx]:
        
        maior = left_idx
    else:
        maior = idx

    if right_idx <= array_size and array[right_idx] > array[maior]:

        maior = right_idx
    
    if maior != idx:
        switch(array, idx, maior)
        max_heapify(array, maior)

def build_max_heap(array):
    for idx in range((array_size//2), -1, -1):
        max_heapify(array, idx - 1)

v1= [3, 10, 40, 1, 60, 34, 21, 100, 5, 31, 2, 4, 6]

v2=[100, 90, 80, 70, 60, 50, 40, 30, 20, 11, 1001]

v3= [1, 2, 3, 9, 8, 7, 6, 5, 4, 20, 30, 40, 50, 60]

for v in [v1, v2,v3]:
  v = [0] + v 
  array_size = len_heap(v)
  build_max_heap(v)
  print(v[1:])



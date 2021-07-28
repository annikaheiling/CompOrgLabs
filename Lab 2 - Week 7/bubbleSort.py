def bubbleSort(arr):
    n = len(arr)
  
    # Traverse all elements
    for i in range(n-1):
        print('outer!')
        # Last i elements are now in place
        for j in range(0, n-i-1):
            # traverse array from 0 to n-i-1
            # Swap if el found is greater than next el
            print('inner:')
            print(arr[j])
            print(arr[j+1])
            print(arr)
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [3,7,4,1,5,2]
  
bubbleSort(arr)
# def bubbleSort(A,n): 
#   len = len(A)
#   for k in range()

#   print(sorted)
#   return

# bubbleSort([3,7,4,1,5,2], 6)
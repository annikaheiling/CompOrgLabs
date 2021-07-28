#based on Prof. McKay's pseudocode

def insertionSort(arr):
    n=len(arr)
    for i in range(1, n):
        j=i
        while (j>0) and (arr[j] < arr[j-1]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j=j-1
            print(arr)

arr = [7,3,4,1,5,2]
insertionSort(arr)


    # # Traverse els 1 to len(arr)
    # for i in range(1, len(arr)):
    #     key = arr[i]
    #     # Move elements of arr[0..i-1], > key, up one position
    #     j = i-1
    #     while j >=0 and key < arr[j] :
    #             arr[j+1] = arr[j]
    #             j -= 1
    #     arr[j+1] = key
    #     print(arr)
    # print(arr)
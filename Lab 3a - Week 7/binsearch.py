def binSearch(arr, size, target):
    low = 0
    high = size
    while(low+1 < high):
      test = (low+high) // 2
      if (arr[test] > target):
        high = test
      else:
        low = test
    if (arr[low] == target):
      print("target found at index "+str(low))
    else:
      print("target not found")

arr = [1, 15, 19, 20, 21, 25, 30, 39]
size = len(arr)
binSearch(arr, size, 15)
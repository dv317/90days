# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
#
a= int(input()) # how many elements to add
arr = list(int(i) for i in input().strip().split(' '))
print(arr)
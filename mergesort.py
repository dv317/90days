def merge(list1,list2,arr):
    i=0
    j=0
    k=0
    while i <len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            arr[k]=list1[i]
            i=i+1
            k=k+1
        else:
            arr[k]=list2[j]
            j=j+1
            k=k+1
    while i<len(list1):
        arr[k]=list1[i]
        k=k+1
        i=i+1
    while j<len(list2):
        arr[k]=list2[j]
        k=k+1
        j=j+1
def merge_sort(arr):
    if len(arr)<2:
        return
    mid = len(arr) // 2
    list1 = arr[:mid]
    list2 = arr[mid:]
    merge_sort(list1)
    merge_sort(list2)
    merge(list1,list2,arr)


a=[10,9,8,7,6,5,4,3]
merge_sort(a)
print(*a)


arr = [2,3,1,8,5,8,9]
n = len(arr)
print("The peak element of the given array is at index : ",end = '')
if n == 1 :
    print(0)
elif arr[0] > arr[1] :
    print(0)
elif arr[n-1] > arr[n-2] :
    print(n-1)
else :
    flag = False
    for i in range(1,n-1) :
        if arr[i] > arr[i-1] and arr[i] > arr[i+1] :
            flag = True
            print(i)
            break 
    if flag == False : 
        print("There is no such peak element.")
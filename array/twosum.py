# O(N^2)

def two_sum(arr, target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            
            if arr[i] + arr [j] == target:
                return True
    
    return False

arr = [0, -1, 2, -3, 1]
target = -2

if two_sum(arr, target):
    print('true')
else:
    print('false')


# nlog(n) approach

def two_sum(arr, target):
    
    arr.sort()
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else: 
            right -= 1
            
    return False

arr = [0, -1, 2, -3, 1]
target = -2

if two_sum(arr, target):
    print("true")
else:
    print("false")
        
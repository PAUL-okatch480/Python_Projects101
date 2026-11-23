#now we test recursion
def countdown (n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
countdown(4)
#recursive factorial program
def factorial(n):
    if n < 0:
        raise ValueError ("n must be non-negative.")
    if n ==0 or n==1:
        return 1
    return n* factorial(n-1)
print(factorial(4))
#output 24 i.e applying the concept of factorisation 4!=4,3,2,1 multiplied
#factorial using iteration
def factorial_iterative(n):
    if n < 0:
        raise ValueError ("n must be non-negative.")
    result=1
    for number in range (2, n+1):
        result *= number
    return result
print(factorial_iterative(5))
#it outputs 120
#naive recursive solution for fibonacci sequence
def fibonacci(n):
    if n <0:
        raise ValueError ("n must be non-negative.")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(8):
    print(fibonacci(i), end=" ")

#iterative fibonacci solution
def fibonacci_iterative(n):
    if n < 0:
        raise ValueError ("n must be non-negative.")
    a,b= 0,1
    for _ in range(n):
        a,b= b, a + b
    return a
print(fibonacci_iterative(5))
#recursive binary
def binary_search(data, target, low, high):
    if low > high:
        return -1
    mid = (low + high) #2
    if data[mid] == target:
        return mid
    if target < data[mid]:
        return binary_search(data, target, low, mid -1)
    return binary_search (data, target, mid + 1, high)
numbers = [3,7,12,18,25,31,42,56,63]
target= 31
index= binary_search(numbers, target, 0, len(numbers)- 1)
if index != -1:
    print("Found at index:", index)
else:
    print("Not found.")

#iterative binary search
def binary_search_iterative (data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high)
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return - 1    
numbers=[3,7,12,18,25,31,42,56,63]
print("Final index:",binary_search_iterative(numbers, 31))
#implementation of the merge sort algorithm
def merge_sort(data):
    #Base case: A list of zero or 1 is sorted
    if len(data) <= 1:
        return data
    #Divide
    mid = len(data) // 2 # I was getting an error because I was exceeding the recursion depth (main reason: Didn't divide)
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    #conquer and combine
    return merge(left, right)
def merge(left, right):
    result=[]
    i = 0
    j= 0
    #compare the first unprocessed item
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        #append any remaining item
    result.extend(left[i:])
    result.extend(right[j:])
    return result
numbers= [38, 27, 43, 3, 9, 83, 10]
print("Original:", numbers)
print("Sorted:",  merge_sort(numbers))
#a sample implementation of the quicksort algorithm
def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[-1]
    smaller = [ x for x in data [:-1] if x <= pivot]
    larger = [x for x in data [:-1] if x > pivot]
    return quicksort (smaller) + [pivot] + quicksort(larger)

numbers= [9,4,7,3,10,5]
print(quicksort(numbers))

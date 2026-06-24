# Problem 14.1: Given sorted arrays A and B of lengths n and m respectively, return
# an array C containing elements common to A and B. The array C should be free of
# duplicates. How would you perform this intersection if—(1.) n ≈ m and (2.) n << m?

# Step one decode the p
# This problem just wants us to return the intersets of two arrays
# the intersect array must not have duplicates

# Step 2 decode the variables
# n ≈ m  stipulates a condition when they are both close is value 1000 ≈ 1200
# n << m is when the grately differ is value 100 << 1,000,000 

# Brute force

def intersection_brute_force(A, B):
    intersect_array = []

    for i in A:
        if i in intersect_array:
            continue
        for j in B:
            if i == j: 
                intersect_array.append(i)
                break  
    return intersect_array

## complexity
# Time O(n*m) we scan all of n and m but the stuff is that there is also a case where n and m are equal so\
# Time O(n^2)
# space O(n) if all values in A and B all form an intercept


# Optimized code 1
# for n ≈ m  condition 

def intersection_brute_force_op1(A, B):
    intersect_array = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        # # Skip duplicate values in A
        if i > 0 and A[i] == A[i - 1]: ## this will work because it is sorted ,  this is better cause we dont need to search through the intersec_array
            i += 1
            continue

        if A[i] == B[j]: 
            # if A[i] not in intersect_array: ## this will constitute O(n) because we get to search through again
            intersect_array.append(A[i]) 
            i += 1
            j += 1
    
        elif A[i] < B[j]:
            i +=1
        
        else:
            j+=1
    return intersect_array

# complexity
# time O(n+m ) worst case we dont get an intersect and we go through A and B entirely and one after another with i and j
# Space O(n) worst case we have a perfect n and m intersect where all values in n inter with m 


# Optimized code 2 
# n << m condition

# the idea is to go through be at log m to find the target(the value from a that we are searching for in B)
#  haven filtered A duplicates

# REf: this is a under kill of find the first occurance(Chapter 12_search/find first ocurance on a sorted list), 
# we wont need to find the first because we just need to 
#  confirm that the value from A exist in B, duplicate will be handled on the small array(A)

def binary_search(arr: list,target: int):
    L = 0
    R = len(arr) - 1

    while L <= R:
        M = L + (R-L) // 2

        if target == arr[M]:
            return True
        if target < arr[M]:
            R = M - 1
        if target > arr[M]:
            L = M + 1
    return False

def intersection_brute_force_op2(A, B):
    intersect_arr = []

    for i in range(len(A)):
        if i> 0 and A[i] == A[i-1]:
            continue
        
        if binary_search(B, A[i]):
            intersect_arr.append(A[i])
    return intersect_arr

## Complexity
# Time O(n log m) where n is the smaller and m is the larger(this is where binary search occurs)
# Space O(n) worst case if all values of n are intersects             

if __name__ == "__main__":

    A = [2, 3, 3, 5, 7, 11]
    B = [3, 3, 7, 15, 31]

    print(intersection_brute_force_op2(A, B))



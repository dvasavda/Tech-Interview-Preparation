'''
Goal: Run a binary search

Benefit: We can ignore half of the elements after searching, speeding up overall search

Plan:
Compare indesearch search with the middle element
if search = middle element:
    return mid indesearch
elif search > mid:
    recur for only the right half of the array
else: (when search is < mid)
    recur for only the left half of the array
'''

def findNumber(arr, k):
    left = 0
    right = len(arr) - 1

    accepted = 'YES'
    unaccepted = 'NO'

    while left <= right:
        middle = left + right

        if arr[middle] == k:
            return accepted

        elif arr[middle] < k:
            left = middle + 1

        else:
            right = middle - 1

    return unaccepted


if __name__ == '__main__':
    arr = [ 5, 2, 3, 4, 5, 1 ]
    k = 0.1

    result = findNumber(arr, k)
    print(result)


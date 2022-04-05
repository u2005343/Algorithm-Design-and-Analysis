"""
Given the following array A = [16, 30, 95, 51, 84, 23, 62, 44], implement a program to sort the array using the following algorithm:

a)	Counting Sort
b)	Radix Sort
c)	Shell Sort

Provide the pseudocode, implement the algorithm using Python, explain the codes/algorithm, and explain running time complexity of each algorithm.

"""

A = [16, 30, 95, 51, 84, 23, 62, 44]

B = [1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]

C = [121, 432, 564, 23, 1, 45, 788]


def counting_sort(array):
    output = [0] * (len(array))
    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    for j in range(1, max(array) + 1):
        count[j] += count[j - 1]

    for k in range(len(array) - 1, -1, -1):
        output[count[array[k]] - 1] = array[k]
        count[array[k]] -= 1

    return output


def radix_sort(arr):
    def mod_counting_sort(a, d: int):
        size: int = len(a)
        output = [0] * size
        count = [0] * (10)

        for i in range(0, size):
            index = arr[i] // d
            count[index % 10] += 1

        for j in range(1, 10):
            count[j] += count[j - 1]

        for i in range(size - 1, -1, -1):
            index = a[i] // d
            output[count[index % 10] - 1] = a[i]
            count[index % 10] -= 1
        # Deep copy array (for some reason output.copy() won't give the same assert result)
        for f in range(0, size):
            a[f] = output[f]

    maximum = max(arr)

    place = 1
    while maximum // place > 0:
        mod_counting_sort(arr, place)
        place *= 10

    return arr

# Python3 program for implementation of Shell Sort

def shellSort(arr):
    gap = len(arr) // 2  # initialize the gap

    while gap > 0:
        i = 0
        j = gap

        # check the array in from left to right
        # till the last possible index of j
        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1


            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1

        gap //= 2
    return arr



A.sort()
B.sort()
C.sort()

assert counting_sort([16, 30, 95, 51, 84, 23, 62, 44]) == A
assert counting_sort([1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]) == B
assert counting_sort([121, 432, 564, 23, 1, 45, 788]) == C

assert radix_sort([16, 30, 95, 51, 84, 23, 62, 44]) == A
assert radix_sort([1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]) == B
assert radix_sort([121, 432, 564, 23, 1, 45, 788]) == C

assert shellSort([16, 30, 95, 51, 84, 23, 62, 44]) == A
assert shellSort([1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]) == B
assert shellSort([121, 432, 564, 23, 1, 45, 788]) == C
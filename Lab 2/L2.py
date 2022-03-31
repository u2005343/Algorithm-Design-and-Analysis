"""
Given the following array A = [16, 30, 95, 51, 84, 23, 62, 44], implement a program to sort the array using the following algorithm:

a)	Counting Sort
b)	Radix Sort
c)	Shell Sort

Provide the pseudocode, implement the algorithm using Python, explain the codes/algorithm, and explain running time complexity of each algorithm.

"""

A: list[int] = [16, 30, 95, 51, 84, 23, 62, 44]

B: list[int] = [1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]

C: list[int] = [121, 432, 564, 23, 1, 45, 788]


def counting_sort(array: list[int]):
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


def radix_sort(arr: list[int]):
    def mod_counting_sort(a: list[int], d: int):
        size: int = len(a)
        output = [0] * size
        count = [0] * (10)

        for i in range(0, size):
            index = arr[i] // d
            count[index % 10] += 1

        for j in range(1, 10):
            count[j] += count[j - 1]


        i = size - 1
        while i >= 0:
            index = a[i] // d
            output[count[index % 10] - 1] = a[i]
            count[index % 10] -= 1
            i -= 1

        # TODO: change this to simple copy
        for f in range(0, size):
            a[f] = output[f]

    maximum = max(arr)

    place = 1
    while maximum // place > 0:
        mod_counting_sort(arr, place)
        place *= 10

    return arr


B.sort()
A.sort()
C.sort()

assert counting_sort([16, 30, 95, 51, 84, 23, 62, 44]) == A
assert counting_sort([1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]) == B
assert counting_sort([121, 432, 564, 23, 1, 45, 788]) == C

assert radix_sort([16, 30, 95, 51, 84, 23, 62, 44]) == A
assert radix_sort([1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]) == B
assert radix_sort([121, 432, 564, 23, 1, 45, 788]) == C



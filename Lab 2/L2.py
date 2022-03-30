"""
Given the following array A = [16, 30, 95, 51, 84, 23, 62, 44], implement a program to sort the array using the following algorithm:

a)	Counting Sort
b)	Radix Sort
c)	Shell Sort

Provide the pseudocode, implement the algorithm using Python, explain the codes/algorithm, and explain running time complexity of each algorithm.

"""

A: list[int] = [16, 30, 95, 51, 84, 23, 62, 44]

B: list[int] = [1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]


def counting_sort(array: list[int]):
    output = [0] * (len(array))
    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    for j in range(1, max(array)):
        count[j] += count[j - 1]

    for k in range(len(array) - 1, 0, -1):
        output[count[array[k]] - 1] = array[k]
        count[array[k]] -= 1

    #
    # i = len(array) - 1
    # while i > 0:
    #     output[count[array[i]] - 1] = array[i]
    #     count[array[i]] -= 1
    #     i -= 1

    return output


B.sort()
print(B)
print(counting_sort(B))
assert counting_sort(B) == B

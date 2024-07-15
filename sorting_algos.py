# https://docs.python.org/3/howto/sorting.html
# https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length
# itertools.product https://docs.python.org/ko/3/library/itertools.html#itertools.product
# regex split https://pynative.com/python-regex-split/
# https://soundprovider.tistory.com/entry/python-itertools#1)%20itertools.product()-1


"""
Simple method of sorting by selecting an element to insert in place


"""


# 0. selection sort
def simple_sort(unsorted_list):
    # return sorted(list), selection sort
    temp = 0
    for i, num in enumerate(unsorted_list):
        if num != min(unsorted_list[i:]):
            temp = unsorted_list.index(min(unsorted_list[i:]))
            unsorted_list[i] = min(unsorted_list[i:])
            unsorted_list[temp] = num

    return unsorted_list


print(simple_sort([4, 1, 5, 8, 2, 6, 3, 11, 19, 12, 10]))


# 1. bubble sort: change adjacent i, j until all sorted
def bubblesort(li):
    temp = 0
    for _ in range(len(li) - 1):
        for i, num in enumerate(li):
            if i + 1 < len(li):
                if num > li[i + 1]:
                    temp = num
                    li[i] = li[i + 1]
                    li[i + 1] = temp
    return li

    # other way of doing this:


print(bubblesort([4, 1, 5, 8, 2, 6, 3, 11, 19, 12, 10]))

# 2. Insertion sort
"""
In-place sorting algorithm
Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
Average case: O(n2), If the list is randomly ordered
Worst case: O(n2), If the list is in reverse order
Space Complexity of Insertion Sort
Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.
Advantages of Insertion Sort:
Simple and easy to implement.
Stable sorting algorithm.
Efficient for small lists and nearly sorted lists.
Space-efficient.

Start with the second element in the list (assuming the first element is already sorted by default).
Compare the current element with the one before it. If the current element is smaller, swap them.
Move to the next element and repeat step 2 until the entire list is sorted.
"""


def insertion_sort(lis):
    for i in range(1, len(lis)):
        current = lis[i]
        j = i - 1

        while j >= 0 and current < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1

        lis[j + 1] = current

    return lis


print(insertion_sort([5, 3, 8, 1, 2]))

# 3. Merge sort: divide and conquer
"""
Divide: Divide the list or array recursively into two halves until it can no more be divided.
Conquer: Each subarray is sorted individually using the merge sort algorithm.
Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.


Time Complexity:

Best Case: O(n log n), When the array is already sorted or nearly sorted.
Average Case: O(n log n), When the array is randomly ordered.
Worst Case: O(n log n), When the array is sorted in reverse order.
Space Complexity: O(n), Additional space is required for the temporary array used during merging.

Advantages of Merge Sort:
Stability: Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.
Simple to implement: The divide-and-conquer approach is straightforward.
Disadvantage of Merge Sort:
Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process. 
Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
"""


def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        print(left, right, left[i], right[j])
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # take care of possible remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2

    lp = li[:mid]
    rp = li[mid:]

    left = merge_sort(lp)
    right = merge_sort(rp)

    return merge(left, right)


print(merge_sort([5, 3, 8, 1, 2]))

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

"""
Best Case: Ω (N log (N))
The best-case scenario for quicksort occur when the pivot chosen at the each step divides the array into roughly equal halves.
In this case, the algorithm will make balanced partitions, leading to efficient Sorting.
Average Case: θ ( N log (N))
Quicksort’s average-case performance is usually very good in practice, making it one of the fastest sorting Algorithm.
Worst Case: O(N2)
The worst-case Scenario for Quicksort occur when the pivot at each step consistently results in highly unbalanced partitions. When the array is already sorted and the pivot is always chosen as the smallest or largest element. To mitigate the worst-case Scenario, various techniques are used such as choosing a good pivot (e.g., median of three) and using Randomized algorithm (Randomized Quicksort ) to shuffle the element before sorting.
Auxiliary Space: O(1), if we don’t consider the recursive stack space. If we consider the recursive stack space then, in the worst case quicksort could make O(N).
Advantages of Quick Sort:
It is a divide-and-conquer algorithm that makes it easier to solve problems.
It is efficient on large data sets.
It has a low overhead, as it only requires a small amount of memory to function.
Disadvantages of Quick Sort:
It has a worst-case time complexity of O(N2), which occurs when the pivot is chosen poorly.
It is not a good choice for small data sets.
It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we are swapping elements according to the pivot’s position (without considering their original positions).

"""


# simple pythonic implementation
def quicksort(lis):
    if len(lis) <= 1:
        return lis

    pivot = lis[len(lis) // 2]

    left = [x for x in lis if x < pivot]
    mid = [x for x in lis if x == pivot]
    right = [x for x in lis if x > pivot]

    return left + mid + right


# other implementation
def partition(array, low, high):
    pivot = array[high]
    i = low  # Initialize i to the starting index of the subarray

    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[high] = array[high], array[i]
    return i


def qsort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        # left partition, high = pi-1 since pi doesn't get included
        partition(array, low, pi - 1)

        # right partition, same logic
        partition(array, pi + 1, high)


"""
Heap Sort: Heap Sort is one of the best sorting algorithms that use Binary Heap to sort an array in O(N*log N) time.
Priority Queue: A priority queue can be implemented by using a heap because it supports insert(), delete(), extractMax(), decreaseKey() operations in O(log N) time.
Graph Algorithms: The heaps are especially used in Graph Algorithms like Dijkstra’s Shortest Path and Prim’s Minimum Spanning Tree.

Heapsort is a comparison-based sorting algorithm that leverages the properties of a binary heap data structure. It's known for its efficiency and is often used in practice for sorting large datasets. The algorithm consists of two main steps: building a max heap from the input array and repeatedly extracting the maximum element from the heap to create the sorted output.

Advantages of Heapsort:
Efficient Worst-Case Performance: Heapsort guarantees a worst-case time complexity of O(n log n), making it suitable for large datasets.
In-place Sorting: Heapsort requires only a constant amount of additional space, making it memory-efficient compared to algorithms like merge sort or quicksort that require additional space proportional to the input size.
Not Recursive: Unlike quicksort, which relies heavily on recursion and can encounter stack overflow issues for large datasets, heapsort is not recursive and doesn't suffer from such problems.
Disadvantages of Heapsort:
Not Stable: Heapsort is not a stable sorting algorithm, meaning it does not preserve the relative order of equal elements in the input array.
Not Adaptive: Heapsort's time complexity remains the same regardless of the initial order of elements in the input array. It does not adapt to pre-sorted or nearly sorted arrays.
Not Suitable for Linked Lists: Heapsort's array-based implementation makes it less suitable for sorting linked lists compared to algorithms like merge sort.

logic explained for implementation:

When iterating in the heapify phase from n // 2 - 1 down to 0, 
you're starting from the last non-leaf node and moving up towards the root. 
This is because elements below the half index are leaf nodes or have only one child, 
 <-this is trivially because of the structure of the max heap
so they're already trivially heaps. By starting from the last non-leaf node and working up,
 you ensure that each subtree rooted at i satisfies the heap property, thus maintaining the heap structure.
 <this is trivially because of the structure of the max heap

In the extraction phase, you're starting from the last element (n-1) and moving towards the first element (0). 
This is because after the initial heapify phase, the largest element (root of the heap) is at arr[0], 
which you want to move to the end of the array to build up the sorted portion of the array. 
By swapping the root with the last element and reducing the heap size (i in heapify), 
you maintain the heap property on the remaining elements, and the largest elements "bubble up" to the front of the array 
in sorted order.

"""


def heapify(li, n, i):
    largest = i

    # properties of heap
    left = 2 * i + 1
    right = 2 * i + 1

    if left < n and li[left] > li[largest]:
        largest = left

    if right < n and li[right] > li[largest]:
        largest = right

    if largest != i:
        # this is to change the element order for max heap property
        # since we only changed the temp indices above, not the list element itself
        li[i], li[largest] = li[largest], li[i]
        # then we run the algo again to confirm max heap property is satisfied
        heapify(li, n, largest)


def heapsort(li):
    n = len(li)

    for i in range(n // 2 - 1, -1, -1):
        heapify(li, n, i)

    for i in range(n - 1, 0, -1):
        # we make a swap starting from the last element downwards
        li[0], li[i] = li[i], li[0]
        # since max heap needs to be maintained for the remaining elems, we call heapify w/largest = 0 to cause shifts
        heapify(li, i, 0)
"""
https://programmers.co.kr/learn/courses/30/lessons/12913
sample input
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |
find best non-overlapping combination of number from each row
"""

# Since same col cannot be added, and we need to find all global max, add current row to next row to find max
def solution(land):
    # return max([max(land[row][:col] + land[row][col+1:]) + land[row][col] for row in range(1, len(land)) for col in range(4)])
    # note that we need to start from second row as we add onto the second row and downward
    for row in range(1, len(land)):

        # max col size = 4
        for col in range(4):

            # list concat and find max [lastrow][col not current]
            land[row][col] += max(land[row-1][:col] + land[row-1][col+1:])


    # same as land[len(land)]
    return max(land[-1])



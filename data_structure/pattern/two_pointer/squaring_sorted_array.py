# LC 977 - Squares of a Sorted Array
#
# PROBLEM: Given sorted array (may have negatives), return array
#          of squares in non-decreasing order.
#
# BRUTE FORCE: square all → sort → O(n log n)
# TWO POINTER: O(n) — use the fact that largest squares are
#              at the ENDS (most negative or most positive)
#
# APPROACH: opposite ends two pointer
#   left = 0, right = n-1
#   fill result from the END (largest first)
#   compare abs(left) vs abs(right)
#   place the larger square at current end of result
#   move that pointer inward
#
# WHY ENDS HAVE LARGEST SQUARES:
#   [-4, -1, 0, 3, 10]
#   squares: [16, 1, 0, 9, 100]
#   largest squares are at -4 (left) and 10 (right)

def sorted_squares(nums):
    n      = len(nums)
    result = [0] * n
    left   = 0
    right  = n - 1
    pos    = n - 1                      # fill result from the end

    while left <= right:
        left_sq  = nums[left]  ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

        pos -= 1

    return result


print(sorted_squares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(sorted_squares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
print(sorted_squares([-5, -3, -1]))        # [1, 9, 25]

# LC 167 - Two Sum II (Sorted Array)
#
# PROBLEM: Given a SORTED array and a target, return indices
#          of two numbers that add up to target (1-indexed).
#
# BRUTE FORCE: O(n²) — check every pair
# TWO POINTER:  O(n)  — use sorted property to move smartly
#
# APPROACH:
#   left = 0, right = n-1
#   current_sum = arr[left] + arr[right]
#   if sum == target → found
#   if sum < target  → need bigger sum → move left right
#   if sum > target  → need smaller sum → move right left
#
# WHY IT WORKS:
#   Array is sorted → moving left right increases sum
#                   → moving right left decreases sum
#   Every pair is checked without nested loops

def two_sum_sorted(numbers, target):
    left  = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]   # 1-indexed

        elif current_sum < target:
            left += 1                       # need larger sum → move left right

        else:
            right -= 1                      # need smaller sum → move right left

    return []


print(two_sum_sorted([2, 7, 11, 15], 9))   # [1, 2]
print(two_sum_sorted([2, 3, 4], 6))        # [1, 3]
print(two_sum_sorted([-1, 0], -1))         # [1, 2]

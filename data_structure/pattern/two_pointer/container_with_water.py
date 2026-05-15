# LC 11 - Container With Most Water
#
# PROBLEM: Given array of heights, find two lines that together
#          with x-axis forms a container holding the most water.
#
# BRUTE FORCE: O(n²) — check every pair
# TWO POINTER: O(n)
#
# APPROACH: opposite ends two pointer
#   left = 0, right = n-1
#   water = min(height[left], height[right]) * (right - left)
#   always move the SHORTER side inward
#
# WHY MOVE SHORTER SIDE?
#   Water is limited by the SHORTER wall.
#   Moving the taller side inward can only decrease width
#   while keeping the same height limit → never better.
#   Moving the shorter side inward might find a taller wall
#   → only chance to increase water.

def max_area(height):
    left     = 0
    right    = len(height) - 1
    max_water = 0

    while left < right:
        width    = right - left
        h        = min(height[left], height[right])
        water    = h * width
        max_water = max(max_water, water)

        if height[left] < height[right]:
            left  += 1      # left is shorter → move it inward
        else:
            right -= 1      # right is shorter (or equal) → move it inward

    return max_water


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 1]))                         # 1
print(max_area([4, 3, 2, 1, 4]))               # 16
print(max_area([1, 2, 1]))                      # 2

## 3661. Maximum Walls Destroyed by Robots
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWallsDestroyed(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        sorted_robots = sorted(robots)
        sorted_walls = sorted(walls)
        destroyed = set()

        for pos, dist in zip(robots, distance):
            idx = bisect_left(sorted_robots, pos)  # index of this robot in sorted list

            # Left range: blocked by nearest robot to the left
            left_bound = sorted_robots[idx - 1] + 1 if idx > 0 else 0
            left_start = max(left_bound, pos - dist)

            # Right range: blocked by nearest robot to the right
            right_bound = sorted_robots[idx + 1] - 1 if idx < len(sorted_robots) - 1 else float('inf')
            right_end = min(right_bound, pos + dist)

            # Walls in [left_start, pos]
            l = bisect_left(sorted_walls, left_start)
            r = bisect_right(sorted_walls, pos)
            for i in range(l, r):
                destroyed.add(sorted_walls[i])

            # Walls in [pos, right_end]
            l = bisect_left(sorted_walls, pos)
            r = bisect_right(sorted_walls, right_end)
            for i in range(l, r):
                destroyed.add(sorted_walls[i])

        return len(destroyed)

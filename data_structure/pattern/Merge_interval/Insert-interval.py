# LC 57 - Insert Interval
#
# DIFFERENCE FROM MERGE INTERVAL (LC 56):
# ─────────────────────────────────────────────────────────────────
# Merge Interval  → input has MANY unsorted intervals, sort first,
#                   then merge all overlapping ones with each other.
#
# Insert Interval → input is ALREADY sorted & merged (no overlaps),
#                   you get ONE new interval to insert at the right
#                   position and merge only where it overlaps.
#                   NO sorting needed — list is already clean.
# ─────────────────────────────────────────────────────────────────
#
# APPROACH: 3 cases for each existing interval vs newInterval
#
#   Case 1 — existing interval ends BEFORE new starts → no overlap, keep it
#             [curr_end < start]
#             existing:  |---|
#             new:              |---|
#
#   Case 2 — existing interval starts AFTER new ends → no overlap, insert new first
#             [curr_start > end]
#             existing:         |---|
#             new:       |---|
#
#   Case 3 — OVERLAP → expand new interval to cover both
#             [anything else]
#             existing:    |-----|
#             new:      |-----|
#             merged:   |--------|
#
# After the loop, always append [start, end] because the last
# interval (or the newInterval itself) is never added inside loop.

class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start = newInterval[0]
        end = newInterval[1]

        for interval in intervals:
            curr_start = interval[0]
            curr_end = interval[1]

            # Case 1: current interval is completely before newInterval
            if curr_end < start:
                result.append(interval)

            # Case 2: current interval is completely after newInterval
            elif curr_start > end:
                result.append([start, end])   # insert merged newInterval first
                start = curr_start            # now track remaining interval
                end = curr_end

            # Case 3: overlap → expand newInterval boundaries
            else:
                if curr_start < start:
                    start = curr_start
                if curr_end > end:
                    end = curr_end

        # always append the last tracked interval
        result.append([start, end])

        return result


s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))           # [[1,5],[6,9]]
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]
print(s.insert([], [5,7]))                      # [[5,7]]
print(s.insert([[1,5]], [2,3]))                 # [[1,5]]

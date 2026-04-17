# LC 253 - Minimum Meeting Rooms (Hard)
#
# DIFFERENCE FROM OVERLAPPING INTERVALS:
# ─────────────────────────────────────────────────────────────────
# Overlapping Intervals → counts max overlaps using sorted
#                         starts/ends + two pointers (no heap)
#
# Minimum Meeting Rooms → same answer BUT uses a min-heap to
#                         TRACK which room frees up earliest.
#                         Harder because heap gives you the actual
#                         earliest end time at every step.
# ─────────────────────────────────────────────────────────────────
#
# APPROACH: Min-Heap (priority queue)
#
#   - Sort intervals by start time
#   - Heap stores END times of ongoing meetings
#   - For each new meeting:
#       if heap top (earliest end) <= new start → room is free
#          → pop it (reuse that room)
#       always push new end time into heap
#   - Heap size at the end = min rooms needed
#
#   WHY HEAP over two-pointer?
#   Heap tells you WHICH room ends earliest so you can reuse it.
#   Two-pointer only counts, heap actually assigns rooms.

import heapq

def min_meeting_rooms(intervals):
    if len(intervals) == 0:
        return 0

    intervals.sort(key=lambda x: x[0])  # sort by start time

    heap = []  # min-heap of end times

    for interval in intervals:
        start = interval[0]
        end   = interval[1]

        # if earliest ending room is free before this meeting starts → reuse it
        if len(heap) > 0 and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)  # assign room, track its end time

    return len(heap)  # rooms still occupied = min rooms needed


print(min_meeting_rooms([[0,30],[5,10],[15,20]]))   # 2
print(min_meeting_rooms([[7,10],[2,4]]))            # 1
print(min_meeting_rooms([[1,5],[2,6],[3,7]]))       # 3
print(min_meeting_rooms([[9,10],[4,9],[4,17]]))     # 2

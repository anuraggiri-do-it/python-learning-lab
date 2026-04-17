# Maximum CPU Load (Hard)
# GFG / Educative variant
#
# PROBLEM:
#   Given a list of jobs [start, end, cpu_load],
#   find the maximum CPU load at any point in time.
#
# DIFFERENCE FROM PREVIOUS MERGE INTERVAL PROBLEMS:
# ─────────────────────────────────────────────────────────────────
# Min Meeting Rooms  → count rooms (each job needs 1 unit)
# Maximum CPU Load   → each job has a WEIGHT (cpu load),
#                      sum the weights of all overlapping jobs,
#                      find the MAXIMUM sum at any point
# ─────────────────────────────────────────────────────────────────
#
# APPROACH: Min-Heap (sort by end time)
#
#   - Sort jobs by start time
#   - Heap stores [end, cpu_load] of active jobs
#   - For each new job:
#       pop all jobs from heap whose end <= current start (they finished)
#       push current job into heap
#       current_load = sum of all loads in heap
#       update max_load
#
#   WHY HEAP?
#   Heap lets us efficiently remove jobs that have ended
#   before the current job starts, so we only sum active ones.

import heapq

def max_cpu_load(jobs):
    jobs.sort(key=lambda x: x[0])  # sort by start time

    heap = []        # [end_time, cpu_load] of active jobs
    current_load = 0
    max_load = 0

    for job in jobs:
        start = job[0]
        end   = job[1]
        load  = job[2]

        # remove all jobs that ended before current job starts
        while len(heap) > 0 and heap[0][0] <= start:
            finished = heapq.heappop(heap)
            current_load -= finished[1]

        heapq.heappush(heap, [end, load])
        current_load += load

        if current_load > max_load:
            max_load = current_load

    return max_load


print(max_cpu_load([[1,4,3],[2,5,4],[7,9,6]]))    # 7  (jobs 1&2 overlap: 3+4=7)
print(max_cpu_load([[6,7,10],[2,4,11],[8,12,15]])) # 15 (no overlap, max single=15)
print(max_cpu_load([[1,4,2],[2,4,1],[3,6,5]]))     # 8  (all 3 overlap at t=3: 2+1+5=8)

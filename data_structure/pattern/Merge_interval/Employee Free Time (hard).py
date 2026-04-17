# LC 759 - Employee Free Time (Hard)
#
# PROBLEM:
#   Given a list of employees, each with a list of working intervals,
#   find the FREE time common to ALL employees (gaps between all work).
#
# DIFFERENCE FROM PREVIOUS MERGE INTERVAL PROBLEMS:
# ─────────────────────────────────────────────────────────────────
# Merge Interval     → merge overlapping intervals into one list
# Insert Interval    → insert one interval into sorted list
# Intersection       → find common parts between two lists
# Min Meeting Rooms  → count rooms needed using heap
# Max CPU Load       → sum weights of overlapping jobs
# Employee Free Time → flatten ALL employees schedules, merge them,
#                      then find the GAPS between merged intervals
#                      Gaps = free time for everyone
# ─────────────────────────────────────────────────────────────────
#
# APPROACH:
#   Step 1 → flatten all employee schedules into one list
#   Step 2 → sort by start time
#   Step 3 → merge overlapping intervals (like LC 56)
#   Step 4 → gaps between merged intervals = free time
#
#   WHY FLATTEN FIRST?
#   Free time = time when NO employee is working.
#   So merge everyone's schedule → gaps are the answer.

def employee_free_time(schedules):
    # step 1: flatten all intervals into one list
    all_intervals = []
    for employee in schedules:
        for interval in employee:
            all_intervals.append(interval)

    # step 2: sort by start time
    all_intervals.sort(key=lambda x: x[0])

    # step 3: merge overlapping intervals
    merged = []
    for interval in all_intervals:
        start = interval[0]
        end   = interval[1]

        if len(merged) == 0:
            merged.append([start, end])
        else:
            last_end = merged[-1][1]

            if last_end < start:           # no overlap → append
                merged.append([start, end])
            else:                          # overlap → extend end
                if end > last_end:
                    merged[-1][1] = end

    # step 4: gaps between merged intervals = free time
    free_time = []
    for i in range(1, len(merged)):
        free_start = merged[i - 1][1]
        free_end   = merged[i][0]
        free_time.append([free_start, free_end])

    return free_time


# employee 1: [1,3],[6,7]   employee 2: [2,4]   employee 3: [2,5],[9,12]
print(employee_free_time([[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]))
# [[5,6],[7,9]]

# employee 1: [1,3],[9,12]  employee 2: [2,4]   employee 3: [6,8]
print(employee_free_time([[[1,3],[9,12]], [[2,4]], [[6,8]]]))
# [[4,6],[8,9]]

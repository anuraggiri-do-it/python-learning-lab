# Overlapping Intervals - Count minimum meeting rooms needed
# GFG / LC 253 variant
#
# DIFFERENCE FROM OTHER MERGE INTERVAL PROBLEMS:
# ─────────────────────────────────────────────────────────────────
# Merge Interval    → merge overlapping intervals into one
# Insert Interval   → insert one new interval into sorted list
# Intersection      → find common parts between two lists
# Overlapping       → COUNT how many intervals overlap at the same
#                     time → tells you min rooms/resources needed
# ─────────────────────────────────────────────────────────────────
#
# APPROACH: Split starts and ends, sort separately
#
#   Key insight: we don't care which start matches which end,
#   we only care HOW MANY are open at the same time.
#
#   - Sort start times and end times separately
#   - Two pointers: s (start), e (end)
#   - If next start < current end → new overlap → count += 1
#   - If next start >= current end → one ended → move end pointer
#   - Track max count = answer

def min_meeting_rooms(intervals):
    if len(intervals) == 0:
        return 0

    starts = sorted([i[0] for i in intervals])
    ends   = sorted([i[1] for i in intervals])

    s = 0
    e = 0
    count = 0
    max_rooms = 0

    while s < len(starts):
        if starts[s] < ends[e]:   # new meeting starts before one ends → overlap
            count += 1
            s += 1
        else:                      # a meeting ended → free one room
            count -= 1
            e += 1

        if count > max_rooms:
            max_rooms = count

    return max_rooms


print(min_meeting_rooms([[0,30],[5,10],[15,20]]))   # 2
print(min_meeting_rooms([[7,10],[2,4]]))            # 1
print(min_meeting_rooms([[1,5],[2,6],[3,7]]))       # 3

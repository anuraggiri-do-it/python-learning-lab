# LC 986 - Interval List Intersections
#
# DIFFERENCE FROM MERGE & INSERT INTERVAL:
# ─────────────────────────────────────────────────────────────────
# Merge Interval  → one list, merge overlapping intervals together
# Insert Interval → one sorted list, insert one new interval
# Intersection    → TWO separate sorted lists, find common overlaps
#                   between them using two pointers (i, j)
# ─────────────────────────────────────────────────────────────────
#
# APPROACH: Two pointer on both lists
#
#   Overlap condition:
#       a_end >= b_start  AND  b_end >= a_start
#       i.e. neither interval ends before the other starts
#
#   Intersection = [max(a_start, b_start), min(a_end, b_end)]
#
#   Pointer move:
#       whichever interval ends first → move its pointer
#       because the other interval may still overlap the next one

class Solution:
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            a_start = firstList[i][0]
            a_end = firstList[i][1]

            b_start = secondList[j][0]
            b_end = secondList[j][1]

            # check overlap
            if a_end >= b_start and b_end >= a_start:
                start = max(a_start, b_start)
                end = min(a_end, b_end)
                result.append([start, end])

            # move pointer of whichever interval ends first
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return result


s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
print(s.intervalIntersection([[1,3],[5,9]], []))   # []

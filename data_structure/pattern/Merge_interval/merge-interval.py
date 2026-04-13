# LC 56 - Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []

    for interval in intervals:
        start = interval[0]
        end = interval[1]

        if len(result) == 0:
            result.append([start, end])

        else:
            last_start = result[-1][0]
            last_end = result[-1][1]

            if last_end < start:  # no overlap
                result.append([start, end])

            else:  # overlap → merge
                if end > last_end:
                    result[-1][1] = end

    return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                 # [[1,5]]

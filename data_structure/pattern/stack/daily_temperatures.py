# LC 739 - Daily Temperatures (Easy/Medium)
#
# PROBLEM: Given temperatures[], return result[] where result[i] =
#          number of days to wait for a warmer temperature.
#          Return 0 if no warmer day exists.
#
# PATTERN: Monotonic Decreasing Stack (stores indices)
#   Stack keeps indices of days with DECREASING temperatures.
#   When a warmer day arrives → pop all cooler days, record wait.
#
# ANALOGY: People waiting for a sunny day ☀️
#   Each cold day waits in line.
#   First warm day that arrives → answers all the cold days before it.
#
# WHY STORE INDICES not values?
#   We need the distance (i - idx) → need the index, not just value.

def daily_temperatures(temps):
    stack  = []            # stores indices
    result = [0] * len(temps)

    for i in range(len(temps)):
        while len(stack) > 0 and temps[i] > temps[stack[-1]]:
            idx        = stack.pop()
            result[idx] = i - idx   # days waited
        stack.append(i)

    return result


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30, 40, 50, 60]))                   # [1,1,1,0]
print(daily_temperatures([30, 60, 90]))                       # [1,1,0]

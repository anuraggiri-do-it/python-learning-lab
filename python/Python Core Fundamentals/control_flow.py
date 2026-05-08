# ═══════════════════════════════════════════════════════════════
#         CONTROL FLOW — Decisions & Loops
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS CONTROL FLOW?
# ─────────────────────────────────────────────────────────────
# Control flow = the order in which Python executes statements.
# By default code runs top to bottom (sequential).
# Control flow lets you branch (if/elif/else) and repeat (loops).
#
# ANALOGY: GPS navigation 🗺️
#   Sequential = drive straight
#   if/elif    = turn left or right based on condition
#   for loop   = repeat the same road N times
#   while loop = keep driving until you reach destination
#   break      = take an exit ramp immediately
#   continue   = skip this turn, go to next


# ═══════════════════════════════════════════════════════════════
# PART 1: if / elif / else
# ═══════════════════════════════════════════════════════════════
#
# SYNTAX:
#   if condition:       ← colon required
#       block           ← 4-space indent required
#   elif condition:
#       block
#   else:
#       block
#
# condition = any expression that evaluates to True or False
# FALSY values: 0, 0.0, '', [], {}, set(), None, False
# TRUTHY values: everything else

age = 20

if age < 13:
    print('child')
elif age < 18:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('senior')

# ── multiple conditions ──────────────────────────────────────
score = 85
grade = 'A'

if score >= 90 and grade == 'A':
    print('Excellent')
elif score >= 70 or grade == 'A':
    print('Good')
else:
    print('Needs improvement')

# ── chained comparisons (Pythonic) ───────────────────────────
x = 5
if 0 < x < 10:              # Python allows this — no need for x>0 and x<10
    print('x is between 0 and 10')

# ── ternary (one-liner if) ────────────────────────────────────
# SYNTAX: value_if_true if condition else value_if_false
status  = 'even' if age % 2 == 0 else 'odd'
label   = 'pass' if score >= 50 else 'fail'
print(status, label)

# ── nested if ────────────────────────────────────────────────
if score >= 50:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    else:
        print('C')
else:
    print('Fail')

# ── match statement (Python 3.10+) ───────────────────────────
# ANALOGY: Switch statement in other languages
command = 'quit'

match command:
    case 'start':
        print('Starting...')
    case 'stop' | 'quit':       # OR pattern
        print('Stopping...')
    case 'help':
        print('Showing help...')
    case _:                     # default (like else)
        print(f'Unknown command: {command}')

# match with value capture
point = (1, 0)
match point:
    case (0, 0):
        print('Origin')
    case (x, 0):
        print(f'On x-axis at {x}')
    case (0, y):
        print(f'On y-axis at {y}')
    case (x, y):
        print(f'Point at ({x}, {y})')


# ═══════════════════════════════════════════════════════════════
# PART 2: for LOOP
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Conveyor belt 🏭
#   for loop = pick each item off the belt, process it, move on
#   Stops automatically when belt is empty

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# ── range() ──────────────────────────────────────────────────
# range(stop)           → 0 to stop-1
# range(start, stop)    → start to stop-1
# range(start, stop, step)

for i in range(5):          # 0 1 2 3 4
    print(i, end=' ')
print()

for i in range(1, 6):       # 1 2 3 4 5
    print(i, end=' ')
print()

for i in range(0, 10, 2):   # 0 2 4 6 8
    print(i, end=' ')
print()

for i in range(10, 0, -1):  # 10 9 8 ... 1 (countdown)
    print(i, end=' ')
print()

# ── enumerate() — index + value ──────────────────────────────
for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')

for i, fruit in enumerate(fruits, start=1):  # start index at 1
    print(f'{i}. {fruit}')

# ── zip() — iterate multiple iterables together ──────────────
names  = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
cities = ['Delhi', 'Mumbai', 'Pune']

for name, score in zip(names, scores):
    print(f'{name}: {score}')

for name, score, city in zip(names, scores, cities):
    print(f'{name} from {city} scored {score}')

# ── iterating dicts ──────────────────────────────────────────
person = {'name': 'Alice', 'age': 30, 'city': 'Delhi'}

for key in person:                      # keys only
    print(key)

for value in person.values():           # values only
    print(value)

for key, value in person.items():       # key-value pairs
    print(f'{key}: {value}')

# ── nested loops ─────────────────────────────────────────────
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end='\t')
    print()

# ── for with else ────────────────────────────────────────────
# else block runs ONLY if loop completed without break
# ANALOGY: Security guard 🔒 — checks every item, reports "all clear" at end
#          unless something suspicious found (break)

for i in range(5):
    if i == 10:             # never true
        break
else:
    print('Loop completed without break')   # this runs

for i in range(5):
    if i == 3:
        break               # breaks at 3
else:
    print('This will NOT print')            # skipped


# ═══════════════════════════════════════════════════════════════
# PART 3: while LOOP
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Vending machine 🎰
#   Keep dispensing while coins remain
#   Stop when coins run out (condition becomes False)
#
# USE WHEN: number of iterations unknown in advance
# USE for WHEN: iterating over a known collection

count = 0
while count < 5:
    print(count, end=' ')
    count += 1
print()

# ── while with user input ────────────────────────────────────
# while True:
#     answer = input('Enter "quit" to exit: ')
#     if answer == 'quit':
#         break
#     print(f'You entered: {answer}')

# ── while with else ──────────────────────────────────────────
n = 10
while n > 0:
    n -= 3
else:
    print(f'Loop ended, n = {n}')   # runs when condition becomes False

# ── infinite loop with break ─────────────────────────────────
attempts = 0
while True:
    attempts += 1
    if attempts >= 3:
        print('Max attempts reached')
        break


# ═══════════════════════════════════════════════════════════════
# PART 4: break / continue / pass
# ═══════════════════════════════════════════════════════════════
#
# break    → exit the loop immediately
# continue → skip rest of current iteration, go to next
# pass     → do nothing (placeholder)
#
# ANALOGY: Walking through a hallway 🚶
#   break    = emergency exit — leave immediately
#   continue = skip this door, go to next
#   pass     = door is there but locked — move on silently

# break — stop at first match
numbers = [1, 3, 5, 7, 4, 9, 11]
for n in numbers:
    if n % 2 == 0:
        print(f'First even: {n}')
        break

# continue — skip unwanted items
for i in range(10):
    if i % 2 == 0:
        continue            # skip even numbers
    print(i, end=' ')       # prints only odd: 1 3 5 7 9
print()

# pass — empty block placeholder
for i in range(3):
    pass                    # TODO: implement later

class EmptyClass:
    pass                    # valid empty class

def not_yet():
    pass                    # valid empty function


# ═══════════════════════════════════════════════════════════════
# PART 5: LOOP PATTERNS (common interview patterns)
# ═══════════════════════════════════════════════════════════════

# ── pattern 1: accumulator ───────────────────────────────────
nums  = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n
print(total)                # 15  (same as sum(nums))

# ── pattern 2: find first match ──────────────────────────────
target = 7
found  = False
for n in [3, 1, 7, 4, 9]:
    if n == target:
        found = True
        break
print('Found' if found else 'Not found')

# ── pattern 3: collect results ───────────────────────────────
evens = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
print(evens)                # [0, 2, 4, 6, 8]

# ── pattern 4: two-pointer style with while ──────────────────
left, right = 0, len(nums) - 1
while left < right:
    print(nums[left], nums[right])
    left  += 1
    right -= 1

# ── pattern 5: sliding window with for ───────────────────────
arr    = [1, 3, 2, 5, 4]
k      = 3
window = sum(arr[:k])
max_sum = window
for i in range(k, len(arr)):
    window  = window + arr[i] - arr[i - k]
    max_sum = max(max_sum, window)
print(max_sum)              # 11  (3+2+5+4 → max window of 3)

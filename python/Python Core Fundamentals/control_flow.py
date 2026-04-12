# ─── if / elif / else ────────────────────────────────────────────────────────
age = 20

if age < 13:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("adult")

# ─── Ternary (one-liner if) ───────────────────────────────────────────────────
status = "even" if age % 2 == 0 else "odd"
print(status)

# ─── Nested if ───────────────────────────────────────────────────────────────
score = 85
if score >= 50:
    if score >= 90:
        print("A")
    else:
        print("B")
else:
    print("Fail")

# ─── for loop ────────────────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# range()
for i in range(5):          # 0 1 2 3 4
    print(i, end=" ")

for i in range(1, 6):       # 1 2 3 4 5
    print(i, end=" ")

for i in range(0, 10, 2):   # 0 2 4 6 8  (step)
    print(i, end=" ")

# enumerate()
for i, fruit in enumerate(fruits):
    print(i, fruit)

# ─── while loop ──────────────────────────────────────────────────────────────
count = 0
while count < 5:
    print(count, end=" ")
    count += 1

# ─── break / continue / pass ─────────────────────────────────────────────────
for i in range(10):
    if i == 5:
        break               # stop loop
    print(i, end=" ")

for i in range(10):
    if i % 2 == 0:
        continue            # skip even
    print(i, end=" ")

for i in range(3):
    pass                    # placeholder, does nothing

# ─── else on loops ───────────────────────────────────────────────────────────
for i in range(3):
    print(i)
else:
    print("loop finished")  # runs if loop was NOT broken

# ─── Nested loops ────────────────────────────────────────────────────────────
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()

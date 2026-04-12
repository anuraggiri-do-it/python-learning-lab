import array

# array module gives a typed, memory-efficient array (unlike list which holds any type).
# array.array(typecode, initializer)
#
# Common typecodes:
#   'i'  → signed int   (4 bytes)
#   'f'  → float        (4 bytes)
#   'd'  → double float (8 bytes)
#   'b'  → signed char  (1 byte)
#   'u'  → unicode char (deprecated in 3.3+)
#
# Memory layout: contiguous block — all elements same type, same size.
#   index:  0    1    2    3
#           [10] [20] [30] [40]
#   access by index is O(1) because offset = base_address + index * element_size


# ── Create ─────────────────────────────────────────────────────────────────────

arr = array.array('i', [10, 20, 30, 40, 50])
print("Created :", arr)                  # array('i', [10, 20, 30, 40, 50])
print("Typecode:", arr.typecode)         # i
print("Itemsize:", arr.itemsize, "bytes")# 4 bytes per int


# ── Access & Slicing ───────────────────────────────────────────────────────────

# Index access — O(1)
print(arr[0])        # 10  (first element)
print(arr[-1])       # 50  (last element)

# Slicing returns a NEW array of the same typecode — O(k)
print(arr[1:4])      # array('i', [20, 30, 40])


# ── Update ─────────────────────────────────────────────────────────────────────

arr[2] = 99          # direct index assignment — O(1)
print("After update index 2:", arr)      # array('i', [10, 20, 99, 40, 50])


# ── Insert / Append ────────────────────────────────────────────────────────────

arr.append(60)       # add at end — O(1) amortized
print("After append 60:", arr)

arr.insert(1, 15)    # insert at index 1, shifts right — O(n)
print("After insert 15 at idx 1:", arr)


# ── Remove / Delete ────────────────────────────────────────────────────────────

arr.remove(99)       # removes FIRST occurrence of value — O(n)
print("After remove 99:", arr)

popped = arr.pop(0)  # remove & return element at index — O(n) for non-tail
print("Popped index 0:", popped, "| Array:", arr)


# ── Search ─────────────────────────────────────────────────────────────────────

# index() — returns index of first occurrence, raises ValueError if not found — O(n)
print("Index of 40:", arr.index(40))

# membership check — O(n)
print("20 in arr:", 20 in arr)


# ── Traversal ──────────────────────────────────────────────────────────────────

# by value — O(n)
for val in arr:
    print(val, end=" ")
print()

# by index — O(n)
for i in range(len(arr)):
    print(f"arr[{i}] = {arr[i]}")


# ── Useful Methods ─────────────────────────────────────────────────────────────

arr2 = array.array('i', [1, 2, 3])
arr3 = array.array('i', [4, 5, 6])

arr2.extend(arr3)            # append all elements of arr3 to arr2 — O(k)
print("After extend:", arr2) # array('i', [1, 2, 3, 4, 5, 6])

print("Count of 3:", arr2.count(3))   # occurrences of value — O(n)

arr2.reverse()               # in-place reverse — O(n)
print("Reversed:", arr2)

copy = arr2.tolist()         # convert to Python list
print("As list:", copy)


# ── Time Complexity Summary ────────────────────────────────────────────────────
#
#   Operation          | Time
#   -------------------|-------
#   Access by index    | O(1)
#   Update by index    | O(1)
#   Append (end)       | O(1) amortized
#   Insert (middle)    | O(n)  — shifts elements
#   Remove by value    | O(n)  — scan + shift
#   Pop (end)          | O(1)
#   Pop (middle/start) | O(n)  — shifts elements
#   Search (index/in)  | O(n)  — linear scan
#   Slice              | O(k)  — k = slice length
#
# Space: O(n) — contiguous block, no pointer overhead (unlike list)
#
# array vs list:
#   list  → dynamic, any type, more memory (stores object refs + metadata)
#   array → typed, compact memory, faster for numeric bulk operations
#   Use array when: storing large numeric data, interfacing with C/binary I/O

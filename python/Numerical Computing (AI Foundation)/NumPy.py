# ═══════════════════════════════════════════════════════════════
#         NUMPY — Numerical Computing (AI Foundation)
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS NUMPY?
# ─────────────────────────────────────────────────────────────
# NumPy = Numerical Python
# Core library for numerical computing in Python.
# Foundation of Pandas, Matplotlib, Scikit-learn, TensorFlow.
#
# WHY NOT JUST USE PYTHON LISTS?
#   Python list  → stores pointers to objects → slow, more memory
#   NumPy array  → stores raw numbers in contiguous memory → fast
#
# ANALOGY: Spreadsheet vs sticky notes 📊
#   Python list  = sticky notes scattered on a wall
#                  each note points to a value somewhere in memory
#   NumPy array  = spreadsheet grid
#                  all values packed tightly side by side
#                  math on entire column at once → vectorized
#
# SPEED: NumPy is 50-100x faster than Python loops for math
#   because operations run in C under the hood (compiled, not interpreted)

import numpy as np

# ═══════════════════════════════════════════════════════════════
# PART 1: CREATING ARRAYS
# ═══════════════════════════════════════════════════════════════

# from list
a = np.array([1, 2, 3, 4, 5])
print(a)              # [1 2 3 4 5]
print(type(a))        # <class 'numpy.ndarray'>
print(a.dtype)        # int64 → all elements same type (unlike list)

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix.shape)   # (3, 3) → 3 rows, 3 cols
print(matrix.ndim)    # 2      → number of dimensions
print(matrix.size)    # 9      → total elements

# ── special arrays ──────────────────────────────────────────
zeros  = np.zeros((3, 4))          # 3x4 matrix of 0.0
ones   = np.ones((2, 3))           # 2x3 matrix of 1.0
full   = np.full((2, 2), 7)        # 2x2 matrix filled with 7
eye    = np.eye(3)                 # 3x3 identity matrix (diagonal=1)
empty  = np.empty((2, 2))          # uninitialized (random garbage values)

print(zeros)
print(ones)
print(eye)

# ── ranges ──────────────────────────────────────────────────
arange  = np.arange(0, 10, 2)      # [0 2 4 6 8]  like range()
linspace = np.linspace(0, 1, 5)    # [0. 0.25 0.5 0.75 1.] → 5 evenly spaced
print(arange)
print(linspace)

# ── random arrays ────────────────────────────────────────────
np.random.seed(42)                 # seed for reproducibility
rand_uniform = np.random.rand(3, 3)      # uniform [0, 1)
rand_normal  = np.random.randn(3, 3)     # standard normal (mean=0, std=1)
rand_int     = np.random.randint(0, 10, (3, 3))  # random ints in [0, 10)
print(rand_int)


# ═══════════════════════════════════════════════════════════════
# PART 2: ARRAY PROPERTIES
# ═══════════════════════════════════════════════════════════════

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)    # (2, 3)  → 2 rows, 3 cols
print(a.ndim)     # 2       → 2D
print(a.size)     # 6       → total elements
print(a.dtype)    # int64
print(a.itemsize) # 8       → bytes per element


# ═══════════════════════════════════════════════════════════════
# PART 3: INDEXING & SLICING
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Excel cells 📊
#   a[row, col] → like clicking cell B2 in Excel
#   a[0:2, 1:3] → like selecting a range of cells

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# single element
print(a[0, 0])    # 1  → row 0, col 0
print(a[1, 2])    # 6  → row 1, col 2
print(a[-1, -1])  # 9  → last row, last col

# slicing [start:stop:step]
print(a[0, :])    # [1 2 3]  → entire first row
print(a[:, 1])    # [2 5 8]  → entire second column
print(a[0:2, 1:3])# [[2 3]   → rows 0-1, cols 1-2
                  #  [5 6]]

# ── boolean indexing ─────────────────────────────────────────
# ANALOGY: Filter in Excel → show only rows where value > 5
a = np.array([1, 2, 3, 4, 5, 6, 7])
mask = a > 4
print(mask)       # [False False False False  True  True  True]
print(a[mask])    # [5 6 7]  → only values where mask is True
print(a[a % 2 == 0])  # [2 4 6]  → even numbers

# ── fancy indexing ───────────────────────────────────────────
a = np.array([10, 20, 30, 40, 50])
print(a[[0, 2, 4]])   # [10 30 50]  → pick specific indices


# ═══════════════════════════════════════════════════════════════
# PART 4: RESHAPING & MANIPULATION
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Reshaping clay 🏺
#   Same amount of clay, different shape.
#   reshape() → same data, different dimensions (no copy)

a = np.arange(1, 13)          # [1 2 3 ... 12]
print(a.reshape(3, 4))        # 3 rows, 4 cols
print(a.reshape(2, 2, 3))     # 3D: 2 blocks of 2x3
print(a.reshape(4, -1))       # -1 → numpy figures out the dim (4x3)

# flatten vs ravel
matrix = np.array([[1, 2], [3, 4]])
print(matrix.flatten())       # [1 2 3 4]  → always returns a COPY
print(matrix.ravel())         # [1 2 3 4]  → returns a VIEW (faster)

# transpose
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)                    # flip rows and cols → (3,2) from (2,3)
print(a.shape)                # (2, 3)
print(a.T.shape)              # (3, 2)

# expand_dims & squeeze
a = np.array([1, 2, 3])       # shape (3,)
print(np.expand_dims(a, axis=0).shape)  # (1, 3) → add row dimension
print(np.expand_dims(a, axis=1).shape)  # (3, 1) → add col dimension


# ═══════════════════════════════════════════════════════════════
# PART 5: MATH OPERATIONS — VECTORIZATION
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Microwave vs stove 🍳
#   Python loop = cook each item one by one on stove
#   NumPy vectorized = microwave entire tray at once
#
# Operations apply element-wise automatically — no loops needed

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)       # [11 22 33 44]
print(a - b)       # [-9 -18 -27 -36]
print(a * b)       # [10 40 90 160]
print(a / b)       # [0.1 0.1 0.1 0.1]
print(a ** 2)      # [1 4 9 16]
print(a + 10)      # [11 12 13 14]  ← scalar broadcast

# universal functions (ufuncs)
print(np.sqrt(a))  # [1. 1.41 1.73 2.]
print(np.exp(a))   # e^1, e^2, e^3, e^4
print(np.log(a))   # natural log
print(np.abs(np.array([-1, -2, 3])))  # [1 2 3]


# ═══════════════════════════════════════════════════════════════
# PART 6: AGGREGATION FUNCTIONS
# ═══════════════════════════════════════════════════════════════

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(a))          # 21       → sum of all
print(np.sum(a, axis=0))  # [5 7 9]  → sum each column (collapse rows)
print(np.sum(a, axis=1))  # [6 15]   → sum each row (collapse cols)

print(np.mean(a))         # 3.5
print(np.median(a))       # 3.5
print(np.std(a))          # standard deviation
print(np.var(a))          # variance
print(np.min(a))          # 1
print(np.max(a))          # 6
print(np.argmin(a))       # 0  → index of min in flattened array
print(np.argmax(a))       # 5  → index of max in flattened array

# axis analogy: think of axis as "which direction to collapse"
#   axis=0 → collapse ROWS → result has shape of one row
#   axis=1 → collapse COLS → result has shape of one column


# ═══════════════════════════════════════════════════════════════
# PART 7: BROADCASTING
# ═══════════════════════════════════════════════════════════════
#
# Broadcasting = applying operations between arrays of different shapes
# NumPy stretches the smaller array to match the larger one (no copy)
#
# ANALOGY: Salary raise 💰
#   Give every employee a 10% raise → multiply entire column by 1.1
#   You don't write 1.1 for each row → it broadcasts automatically

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

row_add = np.array([10, 20, 30])   # shape (3,)
print(a + row_add)
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]
# row_add was broadcast across all 3 rows

col_add = np.array([[1], [2], [3]])  # shape (3,1)
print(a + col_add)
# [[ 2  3  4]
#  [ 6  7  8]
#  [10 11 12]]
# col_add was broadcast across all 3 cols

# BROADCASTING RULES:
#   1. If shapes differ in ndim → prepend 1s to smaller shape
#   2. Dimensions must match or one of them must be 1
#   3. Size-1 dimension is stretched to match the other


# ═══════════════════════════════════════════════════════════════
# PART 8: LINEAR ALGEBRA (AI Foundation)
# ═══════════════════════════════════════════════════════════════
#
# WHY THIS MATTERS FOR AI:
#   Neural networks = matrix multiplications
#   Weights × inputs → dot product → activation
#   Everything in deep learning is linear algebra

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# dot product / matrix multiplication
print(np.dot(A, B))       # [[19 22] [43 50]]
print(A @ B)              # same as np.dot, cleaner syntax

# element-wise vs matrix multiply
print(A * B)              # [[5 12] [21 32]]  ← element-wise
print(A @ B)              # [[19 22] [43 50]] ← matrix multiply

# transpose
print(A.T)                # [[1 3] [2 4]]

# determinant
print(np.linalg.det(A))   # -2.0

# inverse
print(np.linalg.inv(A))   # [[-2.   1. ] [ 1.5 -0.5]]

# eigenvalues & eigenvectors (used in PCA)
vals, vecs = np.linalg.eig(A)
print(vals)               # eigenvalues
print(vecs)               # eigenvectors

# solving linear equations: Ax = b
# 2x + y = 5
# x + 3y = 10
A_eq = np.array([[2, 1], [1, 3]])
b_eq = np.array([5, 10])
x    = np.linalg.solve(A_eq, b_eq)
print(x)                  # [1. 3.]  → x=1, y=3


# ═══════════════════════════════════════════════════════════════
# PART 9: STACKING & SPLITTING
# ═══════════════════════════════════════════════════════════════

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack([a, b]))          # [1 2 3 4 5 6]  → horizontal stack
print(np.vstack([a, b]))          # [[1 2 3]        → vertical stack
                                  #  [4 5 6]]
print(np.concatenate([a, b]))     # [1 2 3 4 5 6]

# splitting
arr = np.arange(1, 10)
print(np.split(arr, 3))           # [array([1,2,3]), array([4,5,6]), array([7,8,9])]

matrix = np.arange(1, 13).reshape(4, 3)
print(np.hsplit(matrix, 3))       # split into 3 column arrays
print(np.vsplit(matrix, 2))       # split into 2 row arrays


# ═══════════════════════════════════════════════════════════════
# PART 10: COPIES vs VIEWS
# ═══════════════════════════════════════════════════════════════
#
# CRITICAL: NumPy slices return VIEWS not copies by default
# Modifying a view modifies the original array
#
# ANALOGY: Google Docs 📄
#   View = shared document → changes affect everyone
#   Copy = downloaded local file → changes are independent

original = np.array([1, 2, 3, 4, 5])

view = original[1:4]      # view → shares memory
view[0] = 99
print(original)           # [1 99 3 4 5]  ← original changed!

copy = original[1:4].copy()  # explicit copy → independent
copy[0] = 0
print(original)           # [1 99 3 4 5]  ← original unchanged

# check if two arrays share memory
print(np.shares_memory(original, view))   # True
print(np.shares_memory(original, copy))   # False


# ═══════════════════════════════════════════════════════════════
# PART 11: PRACTICAL AI/ML PATTERNS
# ═══════════════════════════════════════════════════════════════

# ── normalize data (scale to [0, 1]) ─────────────────────────
data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
normalized = (data - data.min()) / (data.max() - data.min())
print(normalized)         # [0.   0.25 0.5  0.75 1.  ]

# ── standardize data (z-score: mean=0, std=1) ────────────────
standardized = (data - data.mean()) / data.std()
print(standardized)       # [-1.41 -0.71  0.    0.71  1.41]

# ── dot product for similarity (cosine similarity base) ───────
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([1, 0, 0])
print(np.dot(v1, v2))     # 0   → perpendicular, no similarity
print(np.dot(v1, v3))     # 1   → identical direction

# ── one-hot encoding ─────────────────────────────────────────
def one_hot(label, num_classes):
    vec = np.zeros(num_classes)
    vec[label] = 1
    return vec

print(one_hot(2, 5))      # [0. 0. 1. 0. 0.]

# ── batch matrix multiply (common in neural networks) ─────────
# batch of 4 samples, each with 3 features
X = np.random.randn(4, 3)
# weight matrix: 3 inputs → 2 outputs
W = np.random.randn(3, 2)
# forward pass
output = X @ W            # (4,3) @ (3,2) → (4,2)
print(output.shape)       # (4, 2)  → 4 samples, 2 output neurons

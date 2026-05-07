# ═══════════════════════════════════════════════════════════════
#         PANDAS — Data Analysis & Manipulation
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS PANDAS?
# ─────────────────────────────────────────────────────────────
# Pandas = Python Data Analysis Library
# Built on top of NumPy. The standard tool for working with
# tabular data (like Excel or SQL tables) in Python.
#
# ANALOGY: Excel on steroids 📊
#   DataFrame = Excel spreadsheet (rows + columns)
#   Series    = one column of that spreadsheet
#   index     = row numbers (or labels) on the left
#   columns   = column headers on top
#
# TWO CORE DATA STRUCTURES:
#   Series    → 1D labeled array  (one column)
#   DataFrame → 2D labeled table  (rows + columns)

import pandas as pd
import numpy as np

# ═══════════════════════════════════════════════════════════════
# PART 1: SERIES
# ═══════════════════════════════════════════════════════════════

s = pd.Series([10, 20, 30, 40, 50])
print(s)
# 0    10
# 1    20  ← index on left, values on right
# dtype: int64

# custom index
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s2['b'])          # 20

# from dict
s3 = pd.Series({'Python': 90, 'Java': 75, 'Rust': 85})
print(s3['Rust'])       # 85

# Series operations (vectorized)
print(s * 2)            # [20, 40, 60, 80, 100]
print(s[s > 25])        # filter: [30, 40, 50]
print(s.mean())         # 30.0


# ═══════════════════════════════════════════════════════════════
# PART 2: CREATING DATAFRAMES
# ═══════════════════════════════════════════════════════════════

# from dict of lists
df = pd.DataFrame({
    'name':   ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age':    [25, 30, 35, 28, 22],
    'city':   ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Mumbai'],
    'salary': [70000, 85000, 90000, 75000, 60000],
    'score':  [88.5, 92.0, 78.3, 95.1, 83.7]
})

print(df)
print(df.shape)         # (5, 5) → rows, cols
print(df.dtypes)        # data type of each column
print(df.info())        # summary: dtypes, nulls, memory
print(df.describe())    # stats: count, mean, std, min, max

# from list of dicts
records = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
df2 = pd.DataFrame(records)

# from CSV / Excel
# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')
# df.to_csv('output.csv', index=False)


# ═══════════════════════════════════════════════════════════════
# PART 3: VIEWING & INSPECTING DATA
# ═══════════════════════════════════════════════════════════════

print(df.head(3))       # first 3 rows
print(df.tail(2))       # last 2 rows
print(df.sample(2))     # 2 random rows

print(df.columns.tolist())  # ['name', 'age', 'city', 'salary', 'score']
print(df.index)             # RangeIndex(start=0, stop=5, step=1)
print(df['age'].unique())   # unique values in column
print(df['city'].value_counts())  # count per city


# ═══════════════════════════════════════════════════════════════
# PART 4: SELECTING DATA
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Selecting cells in Excel 📊
#   df['col']         = click a column header
#   df[['a','b']]     = select multiple columns
#   df.loc[row, col]  = select by LABEL
#   df.iloc[row, col] = select by POSITION (integer index)

# select single column → Series
print(df['name'])

# select multiple columns → DataFrame
print(df[['name', 'salary']])

# loc — label-based (inclusive on both ends)
print(df.loc[0])                    # row 0 (all columns)
print(df.loc[0, 'name'])            # row 0, name column → 'Alice'
print(df.loc[0:2, 'name':'city'])   # rows 0-2, cols name to city

# iloc — position-based (exclusive end like Python slicing)
print(df.iloc[0])                   # first row
print(df.iloc[0, 1])                # row 0, col 1 → 25
print(df.iloc[0:3, 0:2])            # first 3 rows, first 2 cols
print(df.iloc[-1])                  # last row


# ═══════════════════════════════════════════════════════════════
# PART 5: FILTERING (BOOLEAN INDEXING)
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Excel AutoFilter 🔽
#   Create a True/False mask → apply it to get matching rows

# single condition
print(df[df['age'] > 28])

# multiple conditions — use & (and), | (or), ~ (not)
print(df[(df['age'] > 25) & (df['city'] == 'Delhi')])
print(df[(df['salary'] > 80000) | (df['score'] > 90)])
print(df[~(df['city'] == 'Mumbai')])    # NOT Mumbai

# isin — match against a list
print(df[df['city'].isin(['Delhi', 'Pune'])])

# between
print(df[df['age'].between(25, 30)])

# string methods
print(df[df['name'].str.startswith('A')])
print(df[df['name'].str.contains('li')])


# ═══════════════════════════════════════════════════════════════
# PART 6: ADDING & MODIFYING COLUMNS
# ═══════════════════════════════════════════════════════════════

df['bonus']      = df['salary'] * 0.10              # new column
df['total']      = df['salary'] + df['bonus']       # derived column
df['senior']     = df['age'] > 30                   # boolean column
df['grade']      = df['score'].apply(
    lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C')
)

# apply — apply a function to each row or column
df['name_upper'] = df['name'].apply(str.upper)

# map — element-wise mapping using dict
city_map = {'Delhi': 'North', 'Mumbai': 'West', 'Pune': 'West'}
df['region'] = df['city'].map(city_map)

print(df[['name', 'salary', 'bonus', 'total', 'grade', 'region']])


# ═══════════════════════════════════════════════════════════════
# PART 7: HANDLING MISSING DATA
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Empty cells in Excel 📭
#   NaN = Not a Number = missing value
#   Pandas represents missing as NaN (float) or None

df_missing = pd.DataFrame({
    'name':   ['Alice', 'Bob', None, 'Diana'],
    'age':    [25, None, 35, 28],
    'salary': [70000, 85000, None, 75000]
})

print(df_missing.isnull())              # True where NaN
print(df_missing.isnull().sum())        # count NaN per column
print(df_missing.notnull())             # True where NOT NaN

# drop rows with any NaN
print(df_missing.dropna())

# drop rows where ALL values are NaN
print(df_missing.dropna(how='all'))

# drop columns with NaN
print(df_missing.dropna(axis=1))

# fill NaN with a value
print(df_missing.fillna(0))
print(df_missing['age'].fillna(df_missing['age'].mean()))  # fill with mean

# forward fill / backward fill
print(df_missing.ffill())   # fill with previous value
print(df_missing.bfill())   # fill with next value


# ═══════════════════════════════════════════════════════════════
# PART 8: SORTING
# ═══════════════════════════════════════════════════════════════

print(df.sort_values('salary'))                          # ascending
print(df.sort_values('salary', ascending=False))         # descending
print(df.sort_values(['city', 'salary']))                # multi-column sort
print(df.sort_index())                                   # sort by index


# ═══════════════════════════════════════════════════════════════
# PART 9: GROUPBY — split → apply → combine
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: Pivot table in Excel 📊
#   Group rows by a column → apply aggregation → get summary
#
# split   → divide DataFrame into groups by column value
# apply   → compute aggregation on each group
# combine → merge results back into a new DataFrame

grouped = df.groupby('city')

print(grouped['salary'].mean())         # avg salary per city
print(grouped['salary'].sum())          # total salary per city
print(grouped['salary'].agg(['mean', 'min', 'max', 'count']))

# multiple columns
print(df.groupby('city')[['salary', 'score']].mean())

# custom aggregation
print(df.groupby('city').agg(
    avg_salary=('salary', 'mean'),
    max_score=('score', 'max'),
    count=('name', 'count')
))


# ═══════════════════════════════════════════════════════════════
# PART 10: MERGING & JOINING
# ═══════════════════════════════════════════════════════════════
#
# ANALOGY: SQL JOIN 🔗
#   merge = JOIN two tables on a common column

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name':   ['Alice', 'Bob', 'Charlie', 'Diana'],
    'dept_id': [10, 20, 10, 30]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30],
    'dept':    ['Engineering', 'Marketing', 'Finance']
})

# inner join — only matching rows
inner = pd.merge(employees, departments, on='dept_id', how='inner')
print(inner)

# left join — all from left, matching from right
left = pd.merge(employees, departments, on='dept_id', how='left')

# concat — stack DataFrames vertically or horizontally
df_a = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
df_b = pd.DataFrame({'x': [5, 6], 'y': [7, 8]})
stacked = pd.concat([df_a, df_b], ignore_index=True)  # vertical
side    = pd.concat([df_a, df_b], axis=1)              # horizontal


# ═══════════════════════════════════════════════════════════════
# PART 11: PIVOT TABLES
# ═══════════════════════════════════════════════════════════════

pivot = df.pivot_table(
    values='salary',
    index='city',
    aggfunc='mean'
)
print(pivot)

# cross-tab — frequency table
print(pd.crosstab(df['city'], df['grade']))


# ═══════════════════════════════════════════════════════════════
# PART 12: STRING OPERATIONS
# ═══════════════════════════════════════════════════════════════
# All string methods available via .str accessor

df['name_lower']  = df['name'].str.lower()
df['name_len']    = df['name'].str.len()
df['city_upper']  = df['city'].str.upper()
df['name_split']  = df['name'].str.split('a')   # split on 'a'

# check patterns
print(df['name'].str.contains('li'))
print(df['city'].str.startswith('D'))
print(df['name'].str.replace('a', '@'))


# ═══════════════════════════════════════════════════════════════
# PART 13: DATE & TIME
# ═══════════════════════════════════════════════════════════════

dates = pd.date_range('2024-01-01', periods=5, freq='D')
ts = pd.Series([100, 110, 105, 120, 115], index=dates)

print(ts)
print(ts.index.year)        # year of each date
print(ts.index.month)       # month
print(ts.index.day_name())  # Monday, Tuesday...

# resample — aggregate by time period
# ts.resample('W').mean()   # weekly average
# ts.resample('M').sum()    # monthly sum


# ═══════════════════════════════════════════════════════════════
# PART 14: PRACTICAL EDA WORKFLOW
# ═══════════════════════════════════════════════════════════════

print('\n--- EDA WORKFLOW ---')
print('Shape:',    df.shape)
print('Nulls:\n',  df.isnull().sum())
print('Types:\n',  df.dtypes)
print('Stats:\n',  df.describe())
print('Uniques:\n',df.nunique())

# correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
print('\nCorrelation:\n', numeric_df.corr())

# value counts for categorical
print('\nCity counts:\n', df['city'].value_counts())
print('\nGrade counts:\n', df['grade'].value_counts())


# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
#
#   READ/WRITE:
#     pd.read_csv()       pd.read_excel()     pd.read_json()
#     df.to_csv()         df.to_excel()       df.to_json()
#
#   INSPECT:
#     df.head()  df.tail()  df.info()  df.describe()  df.shape
#
#   SELECT:
#     df['col']           → Series
#     df[['a','b']]       → DataFrame
#     df.loc[row, col]    → by label
#     df.iloc[row, col]   → by position
#
#   FILTER:
#     df[df['col'] > x]
#     df[(cond1) & (cond2)]
#     df['col'].isin([...])
#
#   TRANSFORM:
#     df['new'] = ...
#     df['col'].apply(func)
#     df['col'].map(dict)
#
#   AGGREGATE:
#     df.groupby('col').agg(...)
#     df.pivot_table(...)
#
#   CLEAN:
#     df.dropna()   df.fillna()   df.drop_duplicates()

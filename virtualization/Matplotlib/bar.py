# ═══════════════════════════════════════════════════════════════
#              MATPLOTLIB — Bar Charts
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS MATPLOTLIB?
# ─────────────────────────────────────────────────────────────
# Python's core plotting library. Everything else (Seaborn, Pandas
# plots) is built on top of it.
#
# ANALOGY: Matplotlib = blank canvas + paintbrush 🎨
#   You control every pixel — axes, colors, labels, ticks.
#   More verbose but maximum control.
#
# BAR CHART — when to use:
#   ✅ Compare categories (sales by region, scores by student)
#   ✅ Show counts or totals per group
#   ✅ Ranked data
#   ❌ Not for trends over time (use line chart)
#   ❌ Not for distributions (use histogram)

import matplotlib.pyplot as plt
import numpy as np

# ─────────────────────────────────────────────────────────────
# 1. BASIC VERTICAL BAR CHART
# ─────────────────────────────────────────────────────────────

categories = ['Python', 'JavaScript', 'Java', 'C++', 'Rust']
scores     = [90, 75, 70, 65, 55]

plt.figure(figsize=(8, 5))
plt.bar(categories, scores, color='steelblue', edgecolor='black', width=0.6)

plt.title('Programming Language Popularity', fontsize=14)
plt.xlabel('Language')
plt.ylabel('Score')
plt.ylim(0, 100)

# add value labels on top of each bar
for i, val in enumerate(scores):
    plt.text(i, val + 1, str(val), ha='center', fontsize=10)

plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 2. HORIZONTAL BAR CHART (barh)
# ─────────────────────────────────────────────────────────────
# Use when: category names are long, or ranking is the focus

languages = ['Python', 'JavaScript', 'Java', 'C++', 'Rust']
usage     = [30, 25, 20, 15, 10]

plt.figure(figsize=(8, 5))
bars = plt.barh(languages, usage, color='coral', edgecolor='black')

plt.title('Language Usage (%)', fontsize=14)
plt.xlabel('Usage (%)')
plt.xlim(0, 35)

# add value labels at end of each bar
for bar, val in zip(bars, usage):
    plt.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{val}%', va='center', fontsize=10)

plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 3. GROUPED BAR CHART
# ─────────────────────────────────────────────────────────────
# Compare multiple groups side by side per category

quarters  = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [20, 35, 30, 40]
product_b = [25, 30, 35, 45]
product_c = [15, 20, 25, 30]

x     = np.arange(len(quarters))
width = 0.25                          # width of each bar

plt.figure(figsize=(9, 5))
plt.bar(x - width, product_a, width, label='Product A', color='steelblue')
plt.bar(x,         product_b, width, label='Product B', color='coral')
plt.bar(x + width, product_c, width, label='Product C', color='mediumseagreen')

plt.title('Quarterly Sales by Product', fontsize=14)
plt.xlabel('Quarter')
plt.ylabel('Sales (units)')
plt.xticks(x, quarters)
plt.legend()
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 4. STACKED BAR CHART
# ─────────────────────────────────────────────────────────────
# Show part-to-whole relationship within each category

months   = ['Jan', 'Feb', 'Mar', 'Apr']
frontend = [30, 25, 35, 40]
backend  = [20, 30, 25, 35]
devops   = [10, 15, 10, 20]

x = np.arange(len(months))

plt.figure(figsize=(8, 5))
plt.bar(x, frontend, label='Frontend', color='steelblue')
plt.bar(x, backend,  label='Backend',  color='coral',          bottom=frontend)
plt.bar(x, devops,   label='DevOps',   color='mediumseagreen',
        bottom=[f + b for f, b in zip(frontend, backend)])

plt.title('Monthly Work Hours by Team', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Hours')
plt.xticks(x, months)
plt.legend()
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 5. BAR CHART WITH ERROR BARS
# ─────────────────────────────────────────────────────────────
# Show uncertainty / standard deviation alongside values

groups  = ['Group A', 'Group B', 'Group C', 'Group D']
means   = [75, 82, 68, 90]
std_dev = [5, 3, 7, 4]

plt.figure(figsize=(8, 5))
plt.bar(groups, means, yerr=std_dev, capsize=6,
        color='mediumpurple', edgecolor='black', alpha=0.8)

plt.title('Test Scores with Standard Deviation', fontsize=14)
plt.xlabel('Group')
plt.ylabel('Mean Score')
plt.ylim(0, 105)
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# KEY PARAMETERS REFERENCE
# ─────────────────────────────────────────────────────────────
#
#   plt.bar(x, height)
#     color      → bar fill color ('steelblue', '#3498db', (r,g,b))
#     edgecolor  → border color
#     width      → bar width (default 0.8)
#     alpha      → transparency 0-1
#     bottom     → stacking base values
#     yerr       → error bar values
#     capsize    → error bar cap width
#
#   plt.barh(y, width) → horizontal version, same params
#
#   plt.xticks(positions, labels) → custom tick labels
#   plt.text(x, y, s)             → add text annotation
#   plt.tight_layout()            → prevent label clipping
      
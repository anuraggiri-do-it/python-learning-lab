# ═══════════════════════════════════════════════════════════════
#         PLOT TYPES FOR EDA — Mean, Central Tendency & Spread
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS EDA?
# ─────────────────────────────────────────────────────────────
# Exploratory Data Analysis = visually understanding your data
# BEFORE building any model.
#
# ANALOGY: Doctor's checkup 🩺
#   Before treating a patient, doctor checks vitals first.
#   EDA = checking your data's vitals (shape, spread, outliers).
#
# THIS FILE COVERS:
#   Mean lines on plots, distribution plots, box plots,
#   violin plots — all showing central tendency and spread.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# ─────────────────────────────────────────────────────────────
# 1. HISTOGRAM WITH MEAN, MEDIAN, MODE LINES
# ─────────────────────────────────────────────────────────────
# Most important EDA plot — shows distribution shape

data = np.random.normal(loc=70, scale=10, size=200)  # normal dist, mean=70

mean   = np.mean(data)
median = np.median(data)

plt.figure(figsize=(9, 5))
plt.hist(data, bins=20, color='steelblue', edgecolor='black', alpha=0.7)

plt.axvline(mean,   color='red',    linestyle='--', linewidth=2, label=f'Mean   = {mean:.1f}')
plt.axvline(median, color='orange', linestyle='-',  linewidth=2, label=f'Median = {median:.1f}')

plt.title('Score Distribution with Mean & Median', fontsize=14)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()

# WHAT TO LOOK FOR:
#   Mean ≈ Median → symmetric distribution (normal)
#   Mean > Median → right skewed (outliers pulling mean up)
#   Mean < Median → left skewed  (outliers pulling mean down)


# ─────────────────────────────────────────────────────────────
# 2. BOX PLOT — 5-number summary
# ─────────────────────────────────────────────────────────────
# Shows: min, Q1, median, Q3, max + outliers
#
# ANALOGY: Ruler with marked zones 📏
#   Box = middle 50% of data (IQR)
#   Line in box = median
#   Whiskers = range (excluding outliers)
#   Dots beyond whiskers = outliers

group_a = np.random.normal(70, 10, 100)
group_b = np.random.normal(80, 15, 100)
group_c = np.random.normal(65, 8,  100)

plt.figure(figsize=(8, 5))
plt.boxplot([group_a, group_b, group_c],
            labels=['Group A', 'Group B', 'Group C'],
            patch_artist=True,
            boxprops=dict(facecolor='steelblue', alpha=0.6),
            medianprops=dict(color='red', linewidth=2))

plt.title('Score Distribution by Group (Box Plot)', fontsize=14)
plt.ylabel('Score')
plt.tight_layout()
plt.show()

# READ A BOX PLOT:
#   Top whisker    → max (or Q3 + 1.5*IQR)
#   Top of box     → Q3 (75th percentile)
#   Line in box    → median (50th percentile)
#   Bottom of box  → Q1 (25th percentile)
#   Bottom whisker → min (or Q1 - 1.5*IQR)
#   Dots           → outliers


# ─────────────────────────────────────────────────────────────
# 3. VIOLIN PLOT — distribution shape + box plot combined
# ─────────────────────────────────────────────────────────────
# Box plot shows summary stats.
# Violin plot shows the FULL distribution shape (like a sideways histogram).
#
# ANALOGY: X-ray vs height measurement 🩻
#   Box plot = just the height measurement
#   Violin   = full X-ray showing internal structure

plt.figure(figsize=(8, 5))
plt.violinplot([group_a, group_b, group_c],
               positions=[1, 2, 3],
               showmedians=True,
               showmeans=True)

plt.xticks([1, 2, 3], ['Group A', 'Group B', 'Group C'])
plt.title('Score Distribution by Group (Violin Plot)', fontsize=14)
plt.ylabel('Score')
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 4. MEAN BAR CHART WITH ERROR BARS (std dev)
# ─────────────────────────────────────────────────────────────
# Compare group means + show spread around the mean

groups  = ['Group A', 'Group B', 'Group C']
means   = [np.mean(group_a), np.mean(group_b), np.mean(group_c)]
stds    = [np.std(group_a),  np.std(group_b),  np.std(group_c)]

plt.figure(figsize=(8, 5))
plt.bar(groups, means, yerr=stds, capsize=8,
        color=['steelblue', 'coral', 'mediumseagreen'],
        edgecolor='black', alpha=0.8)

for i, (m, s) in enumerate(zip(means, stds)):
    plt.text(i, m + s + 1, f'{m:.1f}', ha='center', fontsize=10)

plt.title('Mean Scores with Std Deviation', fontsize=14)
plt.ylabel('Mean Score')
plt.ylim(0, 110)
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 5. SCATTER PLOT WITH MEAN LINES
# ─────────────────────────────────────────────────────────────
# Show individual data points + where the mean sits

x = np.random.normal(50, 10, 100)
y = 2 * x + np.random.normal(0, 15, 100)

x_mean = np.mean(x)
y_mean = np.mean(y)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5, color='steelblue', label='Data points')
plt.axvline(x_mean, color='red',    linestyle='--', label=f'X mean = {x_mean:.1f}')
plt.axhline(y_mean, color='orange', linestyle='--', label=f'Y mean = {y_mean:.1f}')
plt.scatter(x_mean, y_mean, color='red', s=100, zorder=5, label='Mean point')

plt.title('Scatter Plot with Mean Lines', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 6. SUBPLOTS — all EDA plots in one figure
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('EDA Dashboard — Central Tendency & Spread', fontsize=16)

data = np.random.normal(70, 12, 300)
mean, median = np.mean(data), np.median(data)

# histogram
axes[0, 0].hist(data, bins=25, color='steelblue', edgecolor='black', alpha=0.7)
axes[0, 0].axvline(mean,   color='red',    linestyle='--', label=f'Mean={mean:.1f}')
axes[0, 0].axvline(median, color='orange', linestyle='-',  label=f'Median={median:.1f}')
axes[0, 0].set_title('Histogram')
axes[0, 0].legend(fontsize=8)

# box plot
axes[0, 1].boxplot(data, patch_artist=True,
                   boxprops=dict(facecolor='steelblue', alpha=0.6),
                   medianprops=dict(color='red', linewidth=2))
axes[0, 1].set_title('Box Plot')

# violin plot
axes[1, 0].violinplot(data, showmedians=True, showmeans=True)
axes[1, 0].set_title('Violin Plot')

# cumulative distribution
sorted_data = np.sort(data)
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
axes[1, 1].plot(sorted_data, cdf, color='steelblue')
axes[1, 1].axvline(mean, color='red', linestyle='--', label=f'Mean={mean:.1f}')
axes[1, 1].set_title('CDF (Cumulative Distribution)')
axes[1, 1].legend(fontsize=8)

plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# WHEN TO USE WHICH PLOT:
# ─────────────────────────────────────────────────────────────
#
#   Histogram    → shape of distribution, skewness, modality
#   Box plot     → compare medians + spread across groups, spot outliers
#   Violin plot  → like box plot but shows full distribution shape
#   Bar + error  → compare group means with uncertainty
#   Scatter      → relationship between two variables
#   CDF          → what % of data falls below a value

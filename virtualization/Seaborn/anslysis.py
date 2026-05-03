# ═══════════════════════════════════════════════════════════════
#              SEABORN — Statistical Data Visualization
# ═══════════════════════════════════════════════════════════════
#
# WHAT IS SEABORN?
# ─────────────────────────────────────────────────────────────
# Seaborn = high-level statistical plotting built on Matplotlib.
# Less code, better defaults, built-in statistical summaries.
#
# ANALOGY: Matplotlib vs Seaborn 🎨
#   Matplotlib = manual painting (full control, more work)
#   Seaborn    = smart templates (beautiful defaults, less code)
#
# WHEN TO USE SEABORN:
#   ✅ Statistical plots (distributions, relationships, categories)
#   ✅ Working with Pandas DataFrames directly
#   ✅ Want beautiful plots with minimal code
#   ✅ Need built-in confidence intervals, regression lines

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
sns.set_theme(style='whitegrid')     # global style: whitegrid, darkgrid, ticks, white, dark


# ─────────────────────────────────────────────────────────────
# SAMPLE DATASETS
# ─────────────────────────────────────────────────────────────

# seaborn built-in datasets (no download needed)
tips     = sns.load_dataset('tips')       # restaurant tips
iris     = sns.load_dataset('iris')       # flower measurements
titanic  = sns.load_dataset('titanic')    # passenger survival
penguins = sns.load_dataset('penguins').dropna()

print(tips.head())
print(tips.describe())


# ─────────────────────────────────────────────────────────────
# 1. DISTRIBUTION PLOTS
# ─────────────────────────────────────────────────────────────

# histplot — histogram with optional KDE
plt.figure(figsize=(8, 5))
sns.histplot(tips['total_bill'], bins=20, kde=True, color='steelblue')
plt.title('Distribution of Total Bill')
plt.tight_layout()
plt.show()

# kdeplot — smooth density curve only
plt.figure(figsize=(8, 5))
sns.kdeplot(data=tips, x='total_bill', hue='sex', fill=True, alpha=0.4)
plt.title('Bill Distribution by Gender (KDE)')
plt.tight_layout()
plt.show()

# displot — figure-level distribution (combines hist + kde + rug)
sns.displot(tips, x='total_bill', hue='sex', kind='kde', fill=True, height=5, aspect=1.5)
plt.title('Bill Distribution by Gender')
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 2. CATEGORICAL PLOTS
# ─────────────────────────────────────────────────────────────

# barplot — mean + confidence interval per category
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex', palette='Set2')
plt.title('Average Bill by Day and Gender')
plt.tight_layout()
plt.show()

# boxplot — median, IQR, outliers per category
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', palette='Set3')
plt.title('Bill Distribution by Day and Gender')
plt.tight_layout()
plt.show()

# violinplot — full distribution shape per category
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex',
               split=True, palette='muted')
plt.title('Bill Distribution Shape by Day and Gender')
plt.tight_layout()
plt.show()

# stripplot — individual data points per category
plt.figure(figsize=(8, 5))
sns.stripplot(data=tips, x='day', y='total_bill', hue='sex',
              dodge=True, alpha=0.6, palette='Set1')
plt.title('Individual Bills by Day and Gender')
plt.tight_layout()
plt.show()

# swarmplot — non-overlapping points (better than strip for small data)
plt.figure(figsize=(8, 5))
sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex',
              dodge=True, palette='Set2')
plt.title('Swarm Plot — Bills by Day')
plt.tight_layout()
plt.show()

# countplot — count of observations per category
plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x='day', hue='sex', palette='pastel')
plt.title('Number of Visits by Day and Gender')
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 3. RELATIONAL PLOTS
# ─────────────────────────────────────────────────────────────

# scatterplot — relationship between two numeric variables
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='sex', size='size', palette='deep', alpha=0.7)
plt.title('Tip vs Total Bill')
plt.tight_layout()
plt.show()

# lineplot — trend over ordered variable (with confidence interval)
# create time-series style data
monthly = pd.DataFrame({
    'month': list(range(1, 13)) * 2,
    'sales': np.random.normal(100, 15, 12).tolist() + np.random.normal(120, 10, 12).tolist(),
    'product': ['A'] * 12 + ['B'] * 12
})

plt.figure(figsize=(9, 5))
sns.lineplot(data=monthly, x='month', y='sales', hue='product',
             marker='o', palette='Set1')
plt.title('Monthly Sales by Product')
plt.tight_layout()
plt.show()

# regplot — scatter + regression line
plt.figure(figsize=(8, 6))
sns.regplot(data=tips, x='total_bill', y='tip',
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Tip vs Bill with Regression Line')
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 4. HEATMAP — correlation matrix
# ─────────────────────────────────────────────────────────────
# Best way to visualize correlations between all numeric columns
#
# ANALOGY: Weather map 🗺️
#   Color intensity = strength of relationship
#   Red = strong positive, Blue = strong negative, White = no relation

plt.figure(figsize=(8, 6))
corr = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            vmin=-1, vmax=1, linewidths=0.5)
plt.title('Correlation Matrix — Tips Dataset')
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 5. PAIRPLOT — all pairwise relationships at once
# ─────────────────────────────────────────────────────────────
# Best single plot for initial EDA on a dataset
# Diagonal = distribution of each variable
# Off-diagonal = scatter between each pair

sns.pairplot(iris, hue='species', palette='Set2', diag_kind='kde')
plt.suptitle('Iris Dataset — Pairwise Relationships', y=1.02)
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 6. FACETGRID — same plot across subgroups
# ─────────────────────────────────────────────────────────────
# Automatically creates a grid of plots, one per category value

g = sns.FacetGrid(tips, col='day', row='sex', height=3, aspect=1.2)
g.map(sns.histplot, 'total_bill', bins=10, color='steelblue')
g.set_titles('{row_name} | {col_name}')
g.set_axis_labels('Total Bill', 'Count')
plt.suptitle('Bill Distribution by Day and Gender', y=1.02)
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# 7. COMPLETE EDA DASHBOARD
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle('Seaborn EDA Dashboard — Tips Dataset', fontsize=16)

sns.histplot(tips['total_bill'], kde=True, ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('Bill Distribution')

sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0, 1], palette='Set3')
axes[0, 1].set_title('Bill by Day (Box)')

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex',
                ax=axes[0, 2], palette='deep', alpha=0.7)
axes[0, 2].set_title('Tip vs Bill')

sns.barplot(data=tips, x='day', y='tip', hue='sex',
            ax=axes[1, 0], palette='Set2')
axes[1, 0].set_title('Avg Tip by Day')

sns.countplot(data=tips, x='day', hue='smoker',
              ax=axes[1, 1], palette='pastel')
axes[1, 1].set_title('Visits by Day')

corr = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            ax=axes[1, 2], linewidths=0.5)
axes[1, 2].set_title('Correlation Matrix')

plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────────────────────
# SEABORN PLOT CHEAT SHEET
# ─────────────────────────────────────────────────────────────
#
#   DISTRIBUTION:
#     histplot   → histogram + optional KDE
#     kdeplot    → smooth density curve
#     ecdfplot   → empirical cumulative distribution
#
#   CATEGORICAL:
#     barplot    → mean + CI per category
#     boxplot    → 5-number summary per category
#     violinplot → full distribution per category
#     stripplot  → raw points per category
#     swarmplot  → non-overlapping points
#     countplot  → count per category
#
#   RELATIONAL:
#     scatterplot → two numeric variables
#     lineplot    → trend over ordered variable
#     regplot     → scatter + regression line
#
#   MATRIX:
#     heatmap    → color-coded matrix (correlations)
#     clustermap → heatmap + hierarchical clustering
#
#   MULTI-PLOT:
#     pairplot   → all pairwise relationships
#     FacetGrid  → same plot across subgroups

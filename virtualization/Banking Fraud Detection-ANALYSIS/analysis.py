import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

df = pd.read_csv("banking_transactions.csv")
df["fraud_flag"] = df["fraud_flag"].astype(str).str.strip().str.upper().map({"TRUE": 1, "FALSE": 0})

fraud = df[df["fraud_flag"] == 1]
legit = df[df["fraud_flag"] == 0]

print("=" * 50)
print("BANKING FRAUD DETECTION - ANALYSIS SUMMARY")
print("=" * 50)
print(f"Total Transactions : {len(df):,}")
print(f"Fraud Cases        : {len(fraud):,} ({len(fraud)/len(df)*100:.1f}%)")
print(f"Legit Cases        : {len(legit):,} ({len(legit)/len(df)*100:.1f}%)")
print()

# Key metric comparison
num_cols = ["transaction_amount", "anomaly_score", "login_attempts",
            "device_risk_score", "geo_distance_km", "failed_transactions_last_30d"]

print("FRAUD vs LEGIT - Key Metric Averages:")
print(f"{'Metric':<35} {'Fraud':>10} {'Legit':>10}")
print("-" * 57)
for col in num_cols:
    print(f"{col:<35} {fraud[col].mean():>10.2f} {legit[col].mean():>10.2f}")

# ── FIGURE 1: Overview Dashboard ─────────────────────────────
fig = plt.figure(figsize=(16, 10))
fig.suptitle("Banking Fraud Detection – Analysis Dashboard", fontsize=16, fontweight="bold")
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

# 1. Fraud vs Legit pie
ax1 = fig.add_subplot(gs[0, 0])
counts = df["fraud_flag"].value_counts()
labels_pie = ["Legit" if i == 0 else "Fraud" for i in counts.index]
ax1.pie(counts, labels=labels_pie, autopct="%1.1f%%",
        colors=["#4CAF50" if i == 0 else "#F44336" for i in counts.index], startangle=90)
ax1.set_title("Fraud vs Legit Distribution")

# 2. Anomaly score distribution
ax2 = fig.add_subplot(gs[0, 1])
ax2.hist(legit["anomaly_score"], bins=30, alpha=0.6, color="#4CAF50", label="Legit")
ax2.hist(fraud["anomaly_score"], bins=30, alpha=0.7, color="#F44336", label="Fraud")
ax2.set_title("Anomaly Score Distribution")
ax2.set_xlabel("Anomaly Score")
ax2.legend()

# 3. Transaction amount boxplot
ax3 = fig.add_subplot(gs[0, 2])
ax3.boxplot([legit["transaction_amount"], fraud["transaction_amount"]],
            labels=["Legit", "Fraud"], patch_artist=True,
            boxprops=dict(facecolor="#90CAF9"))
ax3.set_title("Transaction Amount")
ax3.set_ylabel("Amount ($)")

# 4. Fraud by payment channel
ax4 = fig.add_subplot(gs[1, 0])
channel_fraud = df.groupby("payment_channel")["fraud_flag"].mean().sort_values()
channel_fraud.plot(kind="barh", ax=ax4, color="#FF7043")
ax4.set_title("Fraud Rate by Payment Channel")
ax4.set_xlabel("Fraud Rate")

# 5. Fraud by authentication type
ax5 = fig.add_subplot(gs[1, 1])
auth_fraud = df.groupby("authentication_type")["fraud_flag"].mean().sort_values()
auth_fraud.plot(kind="barh", ax=ax5, color="#7E57C2")
ax5.set_title("Fraud Rate by Auth Type")
ax5.set_xlabel("Fraud Rate")

# 6. Fraud by hour of day
ax6 = fig.add_subplot(gs[1, 2])
hour_fraud = df.groupby("transaction_time_hour")["fraud_flag"].mean()
ax6.plot(hour_fraud.index, hour_fraud.values, color="#F44336", linewidth=2, marker="o", markersize=3)
ax6.set_title("Fraud Rate by Hour of Day")
ax6.set_xlabel("Hour")
ax6.set_ylabel("Fraud Rate")

plt.savefig("fraud_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n[Saved] fraud_dashboard.png")

# ── FIGURE 2: Risk Factor Deep Dive ──────────────────────────
fig2, axes = plt.subplots(2, 3, figsize=(16, 9))
fig2.suptitle("Risk Factor Deep Dive", fontsize=15, fontweight="bold")

risk_cols = [
    ("login_attempts",              "Login Attempts"),
    ("device_risk_score",           "Device Risk Score"),
    ("failed_transactions_last_30d","Failed Txns (30d)"),
    ("geo_distance_km",             "Geo Distance (km)"),
    ("transaction_velocity_score",  "Velocity Score"),
    ("avg_monthly_balance",         "Avg Monthly Balance"),
]

for ax, (col, title) in zip(axes.flat, risk_cols):
    ax.hist(legit[col], bins=30, alpha=0.6, color="#4CAF50", label="Legit", density=True)
    ax.hist(fraud[col], bins=30, alpha=0.7, color="#F44336", label="Fraud", density=True)
    ax.set_title(title)
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig("risk_factors.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] risk_factors.png")

# ── FIGURE 3: Flag Analysis ───────────────────────────────────
fig3, axes3 = plt.subplots(1, 3, figsize=(14, 5))
fig3.suptitle("Binary Flag Impact on Fraud Rate", fontsize=14, fontweight="bold")

flags = [
    ("suspicious_ip_flag",          "Suspicious IP"),
    ("international_transaction_flag", "International Txn"),
    ("card_present_flag",           "Card Present"),
]

for ax, (col, title) in zip(axes3, flags):
    rates = df.groupby(col)["fraud_flag"].mean()
    bars = ax.bar(["No", "Yes"], rates.values, color=["#4CAF50", "#F44336"], width=0.5)
    ax.set_title(title)
    ax.set_ylabel("Fraud Rate")
    ax.set_ylim(0, rates.max() * 1.4)
    for bar, val in zip(bars, rates.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
                f"{val:.3f}", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("flag_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] flag_analysis.png")

# ── FIGURE 4: Correlation Heatmap ────────────────────────────
fig4, ax4 = plt.subplots(figsize=(12, 9))
corr_cols = ["transaction_amount", "login_attempts", "device_risk_score",
             "transfer_frequency", "anomaly_score", "account_age_days",
             "failed_transactions_last_30d", "avg_monthly_balance",
             "daily_transaction_count", "geo_distance_km",
             "transaction_velocity_score", "fraud_flag"]
corr = df[corr_cols].corr()
im = ax4.imshow(corr, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(im, ax=ax4)
ax4.set_xticks(range(len(corr_cols)))
ax4.set_yticks(range(len(corr_cols)))
ax4.set_xticklabels(corr_cols, rotation=45, ha="right", fontsize=8)
ax4.set_yticklabels(corr_cols, fontsize=8)
for i in range(len(corr_cols)):
    for j in range(len(corr_cols)):
        ax4.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=6)
ax4.set_title("Feature Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] correlation_heatmap.png")

# ── Top fraud correlations ────────────────────────────────────
print("\nTop Features Correlated with Fraud:")
fraud_corr = corr["fraud_flag"].drop("fraud_flag").abs().sort_values(ascending=False)
for feat, val in fraud_corr.items():
    print(f"  {feat:<40} {val:.4f}")

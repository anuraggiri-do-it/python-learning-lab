import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── Load all datasets ─────────────────────────────────────────
master    = pd.read_csv("hantavirus_master.csv")
yearly    = pd.read_csv("hantavirus_country_yearly.csv")
outbreaks = pd.read_csv("hantavirus_outbreaks.csv")
clinical  = pd.read_csv("hantavirus_clinical.csv")
monthly   = pd.read_csv("hantavirus_monthly_trends.csv")
env       = pd.read_csv("hantavirus_environmental.csv")
strains   = pd.read_csv("hantavirus_virus_strains.csv")
registry  = pd.read_csv("Hantavirus_Andes_Global_Registry.csv", on_bad_lines="skip")
sources   = pd.read_csv("sources_metadata.csv")

# ── Deduplicate master (one row per country) ──────────────────
country_summary = master.drop_duplicates("iso3")[
    ["iso3","country","who_region","syndrome","total_cases","total_deaths","avg_cfr"]
].copy()

print("=" * 55)
print("HANTAVIRUS GLOBAL EPIDEMIOLOGY — ANALYSIS SUMMARY")
print("=" * 55)
print(f"Countries reporting  : {country_summary['iso3'].nunique()}")
print(f"Total cases (global) : {country_summary['total_cases'].sum():,}")
print(f"Total deaths (global): {country_summary['total_deaths'].sum():,}")
print(f"Outbreaks documented : {len(outbreaks)}")
print(f"Clinical records     : {len(clinical):,}")
print(f"Virus strains        : {strains['virus_strain'].nunique() if 'virus_strain' in strains.columns else 'N/A'}")
print()

# ── FIGURE 1: Global Overview Dashboard ──────────────────────
fig = plt.figure(figsize=(18, 11))
fig.suptitle("Hantavirus (Andes Virus) — Global Epidemiology Dashboard",
             fontsize=15, fontweight="bold", y=0.98)
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

# 1a. Cases by country (top 10)
ax1 = fig.add_subplot(gs[0, 0])
top = country_summary.nlargest(10, "total_cases")
colors = ["#E53935" if s == "HPS" else "#1E88E5" for s in top["syndrome"]]
ax1.barh(top["country"], top["total_cases"], color=colors)
ax1.set_title("Top 10 Countries by Total Cases")
ax1.set_xlabel("Total Cases")
ax1.invert_yaxis()
from matplotlib.patches import Patch
ax1.legend(handles=[Patch(color="#E53935", label="HPS"),
                    Patch(color="#1E88E5", label="HFRS")], fontsize=8)

# 1b. CFR by syndrome
ax2 = fig.add_subplot(gs[0, 1])
cfr_by_syn = country_summary.groupby("syndrome")["avg_cfr"].mean()
ax2.bar(cfr_by_syn.index, cfr_by_syn.values * 100,
        color=["#E53935", "#1E88E5"], width=0.5)
ax2.set_title("Average CFR by Syndrome")
ax2.set_ylabel("CFR (%)")
for i, (s, v) in enumerate(cfr_by_syn.items()):
    ax2.text(i, v * 100 + 0.3, f"{v*100:.1f}%", ha="center", fontsize=10)

# 1c. Cases by WHO region
ax3 = fig.add_subplot(gs[0, 2])
region_cases = country_summary.groupby("who_region")["total_cases"].sum().sort_values()
ax3.barh(region_cases.index, region_cases.values, color="#43A047")
ax3.set_title("Total Cases by WHO Region")
ax3.set_xlabel("Total Cases")

# 1d. Global yearly trend (top 5 countries)
ax4 = fig.add_subplot(gs[1, :2])
top5 = country_summary.nlargest(5, "total_cases")["iso3"].tolist()
for iso in top5:
    sub = yearly[yearly["iso3"] == iso].sort_values("year")
    ax4.plot(sub["year"], sub["confirmed_cases"], label=iso, linewidth=1.5)
ax4.set_title("Annual Case Trends — Top 5 Countries")
ax4.set_xlabel("Year")
ax4.set_ylabel("Confirmed Cases")
ax4.legend(fontsize=8)

# 1e. Deaths vs Cases scatter
ax5 = fig.add_subplot(gs[1, 2])
ax5.scatter(country_summary["total_cases"], country_summary["total_deaths"],
            c=["#E53935" if s == "HPS" else "#1E88E5"
               for s in country_summary["syndrome"]],
            alpha=0.8, s=60)
ax5.set_title("Deaths vs Cases (per Country)")
ax5.set_xlabel("Total Cases")
ax5.set_ylabel("Total Deaths")

plt.savefig("fig1_global_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] fig1_global_dashboard.png")

# ── FIGURE 2: Outbreak Timeline ───────────────────────────────
fig2, ax = plt.subplots(figsize=(14, 6))
fig2.suptitle("Major Hantavirus Outbreaks Timeline (1993–2026)",
              fontsize=13, fontweight="bold")
colors_ob = {"HPS": "#E53935", "HFRS": "#1E88E5"}
for _, row in outbreaks.iterrows():
    c = colors_ob.get(row["syndrome"], "gray")
    ax.scatter(row["year"], row["cfr"], s=row["cases"] * 4,
               color=c, alpha=0.7, edgecolors="black", linewidths=0.5)
    ax.annotate(f"{row['location']}\n({row['cases']})",
                (row["year"], row["cfr"]),
                textcoords="offset points", xytext=(5, 5), fontsize=6.5)
ax.set_xlabel("Year")
ax.set_ylabel("Case Fatality Rate")
ax.set_title("Bubble size = number of cases")
ax.legend(handles=[Patch(color="#E53935", label="HPS"),
                   Patch(color="#1E88E5", label="HFRS")])
plt.tight_layout()
plt.savefig("fig2_outbreak_timeline.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] fig2_outbreak_timeline.png")

# ── FIGURE 3: Clinical Profile ────────────────────────────────
fig3, axes3 = plt.subplots(2, 3, figsize=(16, 9))
fig3.suptitle("Clinical Profile — HPS vs HFRS", fontsize=14, fontweight="bold")

# 3a. Severity distribution
ax = axes3[0, 0]
sev = clinical.groupby(["syndrome", "severity"]).size().unstack(fill_value=0)
sev.T.plot(kind="bar", ax=ax, color=["#E53935", "#1E88E5"], width=0.6)
ax.set_title("Severity Distribution")
ax.set_xlabel("")
ax.tick_params(axis="x", rotation=30)
ax.legend(fontsize=8)

# 3b. Outcome by syndrome
ax = axes3[0, 1]
out = clinical.groupby(["syndrome", "outcome"]).size().unstack(fill_value=0)
out.T.plot(kind="bar", ax=ax, color=["#E53935", "#1E88E5"], width=0.6)
ax.set_title("Outcome by Syndrome")
ax.tick_params(axis="x", rotation=30)
ax.legend(fontsize=8)

# 3c. Hospital days by severity
ax = axes3[0, 2]
hd = clinical.groupby("severity")["hospital_days"].mean().reindex(
    ["Mild", "Moderate", "Severe", "Critical"])
ax.bar(hd.index, hd.values, color=["#66BB6A", "#FFA726", "#EF5350", "#B71C1C"])
ax.set_title("Avg Hospital Days by Severity")
ax.set_ylabel("Days")

# 3d. Age group CFR
ax = axes3[1, 0]
if "age_group" in clinical.columns:
    age_cfr = clinical.groupby("age_group").apply(
        lambda x: (x["outcome"] == "Deceased").mean()
    ).sort_index()
    ax.bar(age_cfr.index, age_cfr.values * 100, color="#7E57C2")
    ax.set_title("CFR by Age Group")
    ax.set_ylabel("CFR (%)")
    ax.tick_params(axis="x", rotation=30)

# 3e. Gender CFR
ax = axes3[1, 1]
if "gender" in clinical.columns:
    g_cfr = clinical.groupby("gender").apply(
        lambda x: (x["outcome"] == "Deceased").mean()
    )
    ax.bar(g_cfr.index, g_cfr.values * 100,
           color=["#42A5F5", "#EC407A"], width=0.4)
    ax.set_title("CFR by Gender")
    ax.set_ylabel("CFR (%)")
    for i, (g, v) in enumerate(g_cfr.items()):
        ax.text(i, v * 100 + 0.3, f"{v*100:.1f}%", ha="center", fontsize=10)

# 3f. ICU admission rate by syndrome
ax = axes3[1, 2]
icu = clinical.groupby("syndrome")["icu_admission"].mean() * 100
ax.bar(icu.index, icu.values, color=["#E53935", "#1E88E5"], width=0.4)
ax.set_title("ICU Admission Rate by Syndrome")
ax.set_ylabel("ICU Rate (%)")
for i, (s, v) in enumerate(icu.items()):
    ax.text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("fig3_clinical_profile.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] fig3_clinical_profile.png")

# ── FIGURE 4: Virus Strain Analysis ──────────────────────────
if not strains.empty:
    fig4, axes4 = plt.subplots(1, 3, figsize=(16, 5))
    fig4.suptitle("Virus Strain Epidemiology", fontsize=13, fontweight="bold")

    # 4a. CFR by strain
    ax = axes4[0]
    strain_cfr = master.groupby("virus_strain")["clinical_cfr"].mean().sort_values(ascending=False)
    ax.barh(strain_cfr.index, strain_cfr.values * 100, color="#EF5350")
    ax.set_title("Clinical CFR by Virus Strain")
    ax.set_xlabel("CFR (%)")

    # 4b. Avg incubation by strain
    ax = axes4[1]
    inc = master.groupby("virus_strain")["avg_incubation"].mean().sort_values(ascending=False)
    ax.barh(inc.index, inc.values, color="#42A5F5")
    ax.set_title("Avg Incubation Period by Strain (days)")
    ax.set_xlabel("Days")

    # 4c. ICU rate by strain
    ax = axes4[2]
    icu_s = master.groupby("virus_strain")["icu_rate"].mean().sort_values(ascending=False)
    ax.barh(icu_s.index, icu_s.values * 100, color="#AB47BC")
    ax.set_title("ICU Rate by Virus Strain (%)")
    ax.set_xlabel("ICU Rate (%)")

    plt.tight_layout()
    plt.savefig("fig4_strain_analysis.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("[Saved] fig4_strain_analysis.png")

# ── FIGURE 5: Environmental & Seasonal Factors ───────────────
if not env.empty and not monthly.empty:
    fig5, axes5 = plt.subplots(1, 2, figsize=(14, 5))
    fig5.suptitle("Environmental & Seasonal Patterns", fontsize=13, fontweight="bold")

    # 5a. Monthly trend (global average)
    ax = axes5[0]
    if "month" in monthly.columns and "confirmed_cases" in monthly.columns:
        mon_avg = monthly.groupby("month")["confirmed_cases"].mean()
        ax.bar(mon_avg.index, mon_avg.values, color="#26A69A")
        ax.set_title("Average Monthly Cases (Global)")
        ax.set_xlabel("Month")
        ax.set_ylabel("Avg Confirmed Cases")
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(["Jan","Feb","Mar","Apr","May","Jun",
                             "Jul","Aug","Sep","Oct","Nov","Dec"], rotation=45)

    # 5b. Environmental correlation
    ax = axes5[1]
    if "temperature_c" in env.columns and "cases" in env.columns:
        ax.scatter(env["temperature_c"], env["cases"], alpha=0.4,
                   color="#FF7043", s=20)
        ax.set_title("Temperature vs Cases")
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Cases")
    elif len(env.columns) >= 2:
        num_cols = env.select_dtypes(include="number").columns[:2]
        ax.scatter(env[num_cols[0]], env[num_cols[1]], alpha=0.4,
                   color="#FF7043", s=20)
        ax.set_title(f"{num_cols[0]} vs {num_cols[1]}")
        ax.set_xlabel(num_cols[0])
        ax.set_ylabel(num_cols[1])

    plt.tight_layout()
    plt.savefig("fig5_environmental.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("[Saved] fig5_environmental.png")

# ── FIGURE 6: Country-Level CFR & Burden Heatmap ─────────────
fig6, axes6 = plt.subplots(1, 2, figsize=(14, 6))
fig6.suptitle("Country-Level Burden & CFR Analysis", fontsize=13, fontweight="bold")

# 6a. CFR by country (sorted)
ax = axes6[0]
cfr_c = country_summary.sort_values("avg_cfr", ascending=True)
colors_c = ["#E53935" if s == "HPS" else "#1E88E5" for s in cfr_c["syndrome"]]
ax.barh(cfr_c["country"], cfr_c["avg_cfr"] * 100, color=colors_c)
ax.set_title("Average CFR by Country")
ax.set_xlabel("CFR (%)")
ax.legend(handles=[Patch(color="#E53935", label="HPS"),
                   Patch(color="#1E88E5", label="HFRS")], fontsize=8)

# 6b. Years reporting vs total cases
ax = axes6[1]
ax.scatter(country_summary["years_reporting"] if "years_reporting" in country_summary.columns
           else [0] * len(country_summary),
           country_summary["total_cases"],
           c=["#E53935" if s == "HPS" else "#1E88E5"
              for s in country_summary["syndrome"]],
           s=80, alpha=0.8)
for _, row in country_summary.iterrows():
    yr = row.get("years_reporting", 0)
    ax.annotate(row["iso3"], (yr, row["total_cases"]),
                fontsize=7, xytext=(3, 3), textcoords="offset points")
ax.set_title("Years Reporting vs Total Cases")
ax.set_xlabel("Years Reporting")
ax.set_ylabel("Total Cases")

plt.tight_layout()
plt.savefig("fig6_country_burden.png", dpi=150, bbox_inches="tight")
plt.show()
print("[Saved] fig6_country_burden.png")

# ── Key Statistics Summary ────────────────────────────────────
print("\n-- KEY FINDINGS ------------------------------------------")
hps = country_summary[country_summary["syndrome"] == "HPS"]
hfrs = country_summary[country_summary["syndrome"] == "HFRS"]
print(f"HPS  countries : {len(hps)} | Avg CFR: {hps['avg_cfr'].mean()*100:.1f}%")
print(f"HFRS countries : {len(hfrs)} | Avg CFR: {hfrs['avg_cfr'].mean()*100:.1f}%")
print(f"Highest burden : {country_summary.nlargest(1,'total_cases')['country'].values[0]}")
print(f"Highest CFR    : {country_summary.nlargest(1,'avg_cfr')['country'].values[0]} "
      f"({country_summary['avg_cfr'].max()*100:.1f}%)")
print(f"Deadliest outbreak: {outbreaks.nlargest(1,'deaths')['location'].values[0]} "
      f"({outbreaks['deaths'].max()} deaths)")

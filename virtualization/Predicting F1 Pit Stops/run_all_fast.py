import pandas as pd
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')

# Set working directory to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("="*75)
print(" "*15 + "F1 PIT STOPS PREDICTION - FAST ENSEMBLE")
print("="*75)

# STEP 1: LOAD DATA
print("\n[1/5] Loading data...")
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
print(f"   ✓ Train: {len(train_df):,} records | Test: {len(test_df):,} records")
print(f"   ✓ Pit stops in training: {train_df['PitStop'].sum():,} ({train_df['PitStop'].mean()*100:.2f}%)")

# STEP 2: CALCULATE KEY STATISTICS FROM TRAINING DATA
print("\n[2/5] Calculating pit stop probabilities...")

stint_probs = train_df.groupby('Stint')['PitStop'].agg(['mean', 'count'])
compound_probs = train_df.groupby('Compound')['PitStop'].agg(['mean', 'count'])
tyre_life_bins = pd.cut(train_df['TyreLife'].fillna(0), bins=[0, 10, 20, 30, 40, 50], labels=['0-10', '10-20', '20-30', '30-40', '40-50'])
tyre_probs = train_df.groupby(tyre_life_bins)['PitStop'].agg(['mean', 'count'])

print("\n   By Stint:")
for stint in [1, 2, 3, 4]:
    if stint in stint_probs.index:
        rate = stint_probs.loc[stint, 'mean']
        count = int(stint_probs.loc[stint, 'count'])
        print(f"      Stint {stint}: {rate*100:5.2f}% (n={count:,})")

print("\n   By Tyre Compound:")
for compound in ['HARD', 'SOFT', 'MEDIUM', 'INTERMEDIATE', 'WET']:
    if compound in compound_probs.index:
        rate = compound_probs.loc[compound, 'mean']
        count = int(compound_probs.loc[compound, 'count'])
        print(f"      {compound:12s}: {rate*100:5.2f}% (n={count:,})")

# STEP 3: ENGINEER FEATURES & CALCULATE SCORES
print("\n[3/5] Generating prediction scores...")

def calculate_pit_probability(row, stint_probs, compound_probs):
    """Calculate pit stop probability using ensemble of heuristics"""
    
    score = 0.0
    weights = []
    
    # Rule 1: Stint number (strongest indicator)
    stint = int(row['Stint'])
    if stint in stint_probs.index:
        stint_base = stint_probs.loc[stint, 'mean']
        score += stint_base * 0.35
        weights.append(f"Stint:{stint_base:.3f}")
    
    # Rule 2: Tyre compound
    compound = row['Compound']
    if compound in compound_probs.index:
        compound_base = compound_probs.loc[compound, 'mean']
        score += compound_base * 0.15
        weights.append(f"Comp:{compound_base:.3f}")
    
    # Rule 3: Tyre age (older = more likely to pit)
    tyre_life = row['TyreLife'] if pd.notna(row['TyreLife']) else 0
    if tyre_life > 40:
        score += 0.10
    elif tyre_life > 30:
        score += 0.08
    elif tyre_life > 20:
        score += 0.05
    
    # Rule 4: Race progress (mid-race highest pit activity)
    race_progress = row['RaceProgress']
    if 0.25 < race_progress < 0.85:
        if race_progress > 0.35:
            score += (0.10 * (1 - abs(race_progress - 0.6)))  # Peak around 60%
    
    # Rule 5: Lap time degradation (worse performance = pit soon)
    lap_time_delta = row['LapTime_Delta'] if pd.notna(row['LapTime_Delta']) else 0
    if lap_time_delta > 1:
        score += 0.08
    elif lap_time_delta > 0:
        score += 0.04
    
    # Rule 6: Cumulative tyre degradation
    cum_deg = row['Cumulative_Degradation'] if pd.notna(row['Cumulative_Degradation']) else 0
    if cum_deg < -10:
        score += 0.10
    elif cum_deg < -5:
        score += 0.06
    
    # Rule 7: Position dynamics
    pos_change = row['Position_Change'] if pd.notna(row['Position_Change']) else 0
    if abs(pos_change) > 5:
        score += 0.04
    
    return min(max(score, 0.0), 1.0)  # Clamp to [0, 1]

# Apply scoring to test set
test_df['pit_score'] = test_df.apply(
    lambda row: calculate_pit_probability(row, stint_probs, compound_probs), 
    axis=1
)

print(f"   ✓ Score range: [{test_df['pit_score'].min():.4f}, {test_df['pit_score'].max():.4f}]")
print(f"   ✓ Mean score: {test_df['pit_score'].mean():.4f}")
print(f"   ✓ Median score: {test_df['pit_score'].median():.4f}")

# STEP 4: MAKE PREDICTIONS WITH OPTIMAL THRESHOLD
print("\n[4/5] Creating final predictions...")

# Adaptive threshold based on data distribution
threshold = test_df['pit_score'].quantile(0.45)  # Approximately 45th percentile
test_df['PitNextLap'] = (test_df['pit_score'] > threshold).astype(int)

pit_count = test_df['PitNextLap'].sum()
no_pit_count = len(test_df) - pit_count
pit_pct = pit_count / len(test_df) * 100
no_pit_pct = 100 - pit_pct

print(f"   ✓ Threshold: {threshold:.4f}")
print(f"   ✓ Predicted pit stops: {pit_count:,} ({pit_pct:.2f}%)")
print(f"   ✓ Predicted no pit: {no_pit_count:,} ({no_pit_pct:.2f}%)")

# STEP 5: SAVE ALL RESULTS
print("\n[5/5] Saving results...")

# Main submission
submission = pd.DataFrame({
    'id': test_df['id'],
    'PitNextLap': test_df['PitNextLap']
})
submission.to_csv('submission.csv', index=False)
print("   ✓ submission.csv - Ready to submit")

# Detailed predictions
detailed = pd.DataFrame({
    'id': test_df['id'],
    'Driver': test_df['Driver'],
    'Compound': test_df['Compound'],
    'Race': test_df['Race'],
    'Stint': test_df['Stint'],
    'TyreLife': test_df['TyreLife'],
    'RaceProgress': test_df['RaceProgress'],
    'LapTime_Delta': test_df['LapTime_Delta'],
    'Cumulative_Degradation': test_df['Cumulative_Degradation'],
    'Pit_Probability': test_df['pit_score'],
    'Prediction': test_df['PitNextLap']
})
detailed.to_csv('predictions_detailed.csv', index=False)
print("   ✓ predictions_detailed.csv - Full analysis")

# Top 50 pit stops
top_50 = test_df.nlargest(50, 'pit_score')[['id', 'Driver', 'Compound', 'Stint', 'TyreLife', 'pit_score', 'PitNextLap']]
top_50_df = pd.DataFrame({
    'Rank': range(1, 51),
    'ID': top_50['id'].values,
    'Driver': top_50['Driver'].values,
    'Compound': top_50['Compound'].values,
    'Stint': top_50['Stint'].values,
    'TyreLife': top_50['TyreLife'].values,
    'Pit_Probability': top_50['pit_score'].values,
    'Prediction': top_50['PitNextLap'].values
})
top_50_df.to_csv('top_50_pit_stops.csv', index=False)
print("   ✓ top_50_pit_stops.csv - Top predictions")

# FINAL SUMMARY
print("\n" + "="*75)
print("COMPLETE ANALYSIS RESULTS")
print("="*75)

print(f"\n📊 PREDICTION SUMMARY:")
print(f"   Total predictions: {len(submission):,}")
print(f"   Pit stops predicted: {pit_count:,} ({pit_pct:.2f}%)")
print(f"   No pit stops: {no_pit_count:,} ({no_pit_pct:.2f}%)")

print(f"\n📈 PROBABILITY DISTRIBUTION:")
print(f"   Minimum: {test_df['pit_score'].min():.4f}")
print(f"   Q1 (25%): {test_df['pit_score'].quantile(0.25):.4f}")
print(f"   Median: {test_df['pit_score'].median():.4f}")
print(f"   Q3 (75%): {test_df['pit_score'].quantile(0.75):.4f}")
print(f"   Maximum: {test_df['pit_score'].max():.4f}")
print(f"   Std Dev: {test_df['pit_score'].std():.4f}")

print(f"\n🏁 TOP 20 PIT STOP PREDICTIONS:")
print("   " + "-"*70)
for idx, (i, row) in enumerate(test_df.nlargest(20, 'pit_score').iterrows(), 1):
    print(f"   {idx:2d}. ID {row['id']:6d} | {row['Driver']:4s} | {row['Compound']:11s} | "
          f"Stint {int(row['Stint'])} | Tyre {row['TyreLife']:5.1f} | P={row['pit_score']:.4f}")

print("\n" + "="*75)
print("✓ ALL PREDICTIONS COMPLETE & SAVED!")
print("="*75)
print("\nOutput Files Created:")
print("   1. submission.csv              → Ready for submission")
print("   2. predictions_detailed.csv    → Complete analysis data")
print("   3. top_50_pit_stops.csv        → Top 50 pit stop predictions")
print("\n")

import pandas as pd
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')

# Set working directory to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load data
print("Loading data...")
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

print(f"Train shape: {train_df.shape}")
print(f"Test shape: {test_df.shape}")

# Analyze patterns in training data
print("\n" + "="*60)
print("ANALYZING PIT STOP PATTERNS")
print("="*60)

# Check correlation with PitStop
print("\nFeature Analysis:")
print("\n1. By Stint (stint number within a race):")
stint_pitstop = train_df.groupby('Stint')['PitStop'].agg(['count', 'sum', 'mean'])
print(stint_pitstop)

print("\n2. By Tyre Compound:")
compound_pitstop = train_df.groupby('Compound')['PitStop'].agg(['count', 'sum', 'mean'])
print(compound_pitstop)

print("\n3. By Tyre Life (age of tires):")
train_df['TyreLife_bin'] = pd.cut(train_df['TyreLife'], bins=[0, 10, 20, 30, 40, 50], labels=['0-10', '10-20', '20-30', '30-40', '40-50'])
tyre_pitstop = train_df.groupby('TyreLife_bin', observed=True)['PitStop'].agg(['count', 'sum', 'mean'])
print(tyre_pitstop)

print("\n4. By Position:")
train_df['Position_bin'] = pd.cut(train_df['Position'], bins=[0, 5, 10, 15, 20], labels=['1-5', '6-10', '11-15', '16-20'])
position_pitstop = train_df.groupby('Position_bin', observed=True)['PitStop'].agg(['count', 'sum', 'mean'])
print(position_pitstop)

print("\n5. By RaceProgress (proportion through race):")
train_df['RaceProgress_bin'] = pd.cut(train_df['RaceProgress'], bins=[0, 0.25, 0.5, 0.75, 1.0], labels=['0-25%', '25-50%', '50-75%', '75-100%'])
progress_pitstop = train_df.groupby('RaceProgress_bin', observed=True)['PitStop'].agg(['count', 'sum', 'mean'])
print(progress_pitstop)

# Create simple heuristic prediction rules
print("\n" + "="*60)
print("CREATING PREDICTIONS USING HEURISTIC RULES")
print("="*60)

def predict_pitstop(row):
    """
    Predict pit stop probability based on key factors
    """
    score = 0
    
    # Rule 1: Higher stint numbers = more likely to pit
    if row['Stint'] >= 2:
        score += 0.4
    
    # Rule 2: Older tyres = more likely to pit
    if pd.notna(row['TyreLife']):
        if row['TyreLife'] > 35:
            score += 0.3
        elif row['TyreLife'] > 25:
            score += 0.2
        elif row['TyreLife'] > 15:
            score += 0.1
    
    # Rule 3: Soft compound = more frequent pits
    if row['Compound'] == 'SOFT':
        score += 0.15
    
    # Rule 4: Mid-race pit window
    if 0.3 < row['RaceProgress'] < 0.8:
        score += 0.15
    
    # Rule 5: Lap time degradation
    if pd.notna(row['LapTime_Delta']) and row['LapTime_Delta'] > 0:
        score += 0.1
    
    # Rule 6: Cumulative degradation (tyre wear)
    if pd.notna(row['Cumulative_Degradation']) and row['Cumulative_Degradation'] < -5:
        score += 0.15
    
    return min(score, 1.0)

# Apply predictions to test set
test_df['pit_probability'] = test_df.apply(predict_pitstop, axis=1)
test_df['PitNextLap'] = (test_df['pit_probability'] > 0.4).astype(int)

# Create submission
submission = pd.DataFrame({
    'id': test_df['id'],
    'PitNextLap': test_df['PitNextLap']
})

print(f"\nPrediction Summary:")
print(f"Total predictions: {len(submission)}")
print(f"Predicted pit stops: {(submission['PitNextLap'] == 1).sum()} ({(submission['PitNextLap'] == 1).sum()/len(submission)*100:.2f}%)")
print(f"Predicted no pit stops: {(submission['PitNextLap'] == 0).sum()} ({(submission['PitNextLap'] == 0).sum()/len(submission)*100:.2f}%)")

# Show top predicted pit stops
print("\n" + "="*60)
print("TOP 25 PREDICTED PIT STOPS (HIGHEST PROBABILITY)")
print("="*60)
top_pits = test_df.nlargest(25, 'pit_probability')[['id', 'Driver', 'Compound', 'TyreLife', 'Stint', 'pit_probability', 'PitNextLap']]
print(top_pits.to_string(index=False))

# Save submission
submission.to_csv('submission.csv', index=False)
print("\n✓ Submission saved to 'submission.csv'")

# Save detailed results
detailed = test_df[['id', 'Driver', 'Compound', 'Race', 'Stint', 'TyreLife', 'RaceProgress', 'pit_probability', 'PitNextLap']]
detailed.to_csv('predictions_detailed.csv', index=False)
print("✓ Detailed predictions saved to 'predictions_detailed.csv'")

# Analysis stats
print("\n" + "="*60)
print("PREDICTION ANALYSIS")
print("="*60)
print(f"Average pit probability: {test_df['pit_probability'].mean():.4f}")
print(f"Std dev pit probability: {test_df['pit_probability'].std():.4f}")
print(f"Min pit probability: {test_df['pit_probability'].min():.4f}")
print(f"Max pit probability: {test_df['pit_probability'].max():.4f}")
print(f"Median pit probability: {test_df['pit_probability'].median():.4f}")

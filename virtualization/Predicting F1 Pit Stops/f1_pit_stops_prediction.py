import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import warnings
warnings.filterwarnings('ignore')

# Load data
print("Loading training data...")
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

print(f"Train shape: {train_df.shape}")
print(f"Test shape: {test_df.shape}")
print(f"\nTraining data info:")
print(train_df.head())
print(f"\nTarget distribution:")
print(train_df['PitStop'].value_counts())

# Prepare features
def prepare_features(df):
    df_copy = df.copy()
    
    # Encode categorical variables
    le_compound = LabelEncoder()
    le_race = LabelEncoder()
    le_driver = LabelEncoder()
    
    # Fit encoders on combined data to ensure consistency
    all_compounds = pd.concat([train_df['Compound'], test_df['Compound']]).unique()
    all_races = pd.concat([train_df['Race'], test_df['Race']]).unique()
    all_drivers = pd.concat([train_df['Driver'], test_df['Driver']]).unique()
    
    le_compound.fit(all_compounds)
    le_race.fit(all_races)
    le_driver.fit(all_drivers)
    
    df_copy['Compound_encoded'] = le_compound.transform(df_copy['Compound'])
    df_copy['Race_encoded'] = le_race.transform(df_copy['Race'])
    df_copy['Driver_encoded'] = le_driver.transform(df_copy['Driver'])
    
    return df_copy, le_compound, le_race, le_driver

train_df, le_compound, le_race, le_driver = prepare_features(train_df)
test_df_prepared, _, _, _ = prepare_features(test_df)

# Select features for the model
feature_cols = ['Compound_encoded', 'Race_encoded', 'Year', 'LapNumber', 'Stint', 
                'TyreLife', 'Position', 'LapTime (s)', 'LapTime_Delta', 
                'Cumulative_Degradation', 'RaceProgress', 'Position_Change', 'Driver_encoded']

X_train = train_df[feature_cols].fillna(0)
y_train = train_df['PitStop']
X_test = test_df_prepared[feature_cols].fillna(0)

print(f"\nFeatures selected: {len(feature_cols)}")
print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

# Train models - using Gradient Boosting for faster training
print("\n" + "="*60)
print("Training Gradient Boosting model...")
print("="*60)

# Use smaller Random Forest for speed
gb_model = GradientBoostingClassifier(n_estimators=50, max_depth=5, random_state=42, verbose=1)
gb_model.fit(X_train, y_train)

# Get feature importance
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': gb_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 10 Feature Importance:")
print(feature_importance.head(10))

# Make predictions on test set
print("\n" + "="*60)
print("Making predictions on test set...")
print("="*60)

y_pred_proba = gb_model.predict_proba(X_test)[:, 1]
y_pred = gb_model.predict(X_test)

print(f"\nPrediction distribution:")
print(f"Pit Stop (1): {(y_pred == 1).sum()}")
print(f"No Pit Stop (0): {(y_pred == 0).sum()}")
print(f"Probability stats - Min: {y_pred_proba.min():.4f}, Max: {y_pred_proba.max():.4f}, Mean: {y_pred_proba.mean():.4f}")

# Create submission
submission = pd.DataFrame({
    'id': test_df['id'],
    'PitNextLap': y_pred
})

print(f"\nSubmission preview:")
print(submission.head(20))
print(f"\nSubmission statistics:")
print(submission['PitNextLap'].value_counts())

# Save submission
submission.to_csv('submission.csv', index=False)
print("\n✓ Submission saved to 'submission.csv'")

# Additional predictions with probabilities
submission_proba = pd.DataFrame({
    'id': test_df['id'],
    'PitNextLap': y_pred,
    'Probability': y_pred_proba
})
submission_proba.to_csv('submission_with_probabilities.csv', index=False)
print("✓ Detailed submission with probabilities saved to 'submission_with_probabilities.csv'")

print("\n" + "="*60)
print("BEST PREDICTIONS - HIGH CONFIDENCE PIT STOPS")
print("="*60)
top_pit_stops = submission_proba[submission_proba['PitNextLap'] == 1].sort_values('Probability', ascending=False).head(20)
print(f"\nTop 20 most likely pit stops (probability > {top_pit_stops['Probability'].min():.4f}):")
print(top_pit_stops.to_string(index=False))

print("\n" + "="*60)
print("ANALYSIS SUMMARY")
print("="*60)
print(f"Total test samples: {len(test_df)}")
print(f"Predicted pit stops: {(y_pred == 1).sum()} ({(y_pred == 1).sum()/len(test_df)*100:.2f}%)")
print(f"Predicted no pit stops: {(y_pred == 0).sum()} ({(y_pred == 0).sum()/len(test_df)*100:.2f}%)")
print(f"\nModel: Gradient Boosting with {gb_model.n_estimators} trees")
print(f"Max depth: {gb_model.max_depth}")
print(f"Features used: {len(feature_cols)}")

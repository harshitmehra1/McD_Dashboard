import pandas as pd
import os

# Load cleaned data
filename = "./data/Cleaned_mcd.csv"
if not os.path.exists(filename):
    print(f"❌ File '{filename}' not found.")
    exit()

df = pd.read_csv(filename)

# Nutrients to score
beneficial = {
    'Protein': 0.20,
    'Dietary Fiber': 0.15
}
harmful = {
    'Saturated Fat': 0.20,
    'Sodium': 0.20,
    'Sugars': 0.15,
    'Calories': 0.10
}

# Min-max normalize and compute weighted scores
def normalize(series, inverse=False):
    norm = (series - series.min()) / (series.max() - series.min())
    return 1 - norm if inverse else norm

score = pd.Series(0, index=df.index)

for col, weight in beneficial.items():
    norm_col = normalize(df[col])
    score += norm_col * weight * 100

for col, weight in harmful.items():
    norm_col = normalize(df[col], inverse=True)
    score += norm_col * weight * 100

# Clip scores between 0 and 100
df['Health Score'] = score.clip(0, 100).round(2)

# Save new file
output_file = "./data/Scored_mcd.csv"
df.to_csv(output_file, index=False)
print(f"✅ Scored file saved as '{output_file}'")
print(df[['Item', 'Health Score']].sort_values(by='Health Score', ascending=False).head(10))

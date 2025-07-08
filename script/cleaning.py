import pandas as pd
import os

# Step 1: Load CSV
filename = "./data/menu.csv"

if not os.path.exists(filename):
    print(f"❌ File '{filename}' not found.")
    exit()

df = pd.read_csv(filename)

# Step 2: Display basic info
print("📊 ORIGINAL DATA SUMMARY")
print(f"🧾 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\n📌 Columns:\n{list(df.columns)}\n")

print("🔍 COLUMN TYPES & SAMPLE VALUES")
for col in df.columns:
    print(f"• {col}")
    print(f"  - Type: {df[col].dtype}")
    print(f"  - Sample: {df[col].dropna().unique()[:5].tolist()}")
    print()

# Step 3: Clean — drop unnecessary columns
columns_to_drop = ["Serving Size", "Calories from Fat"]
df_cleaned = df.drop(columns=columns_to_drop)

# Step 4: Display post-cleaning info
print("🧹 CLEANING COMPLETE")
print(f"📉 Dropped Columns: {columns_to_drop}")
print(f"📐 New Shape: {df_cleaned.shape[0]} rows × {df_cleaned.shape[1]} columns")
print(f"\n✅ Remaining Columns:\n{list(df_cleaned.columns)}")

# Step 5: Save cleaned data
output_file = "./data/Cleaned_mcd.csv"
df_cleaned.to_csv(output_file, index=False)
print(f"\n💾 Cleaned dataset saved as '{output_file}'")

import seaborn as sns
import pandas as pd
import os

# Create analytics directory if it doesn't exist
os.makedirs("analytics", exist_ok=True)

print("Loading Titanic dataset from Seaborn...")
df = sns.load_dataset('titanic')

# Save as offline fallback inside /analytics
output_path = "analytics/titanic.csv"
df.to_csv(output_path, index=False)
print(f"Successfully saved offline fallback dataset to {output_path}")
print("Dataset shape:", df.shape)
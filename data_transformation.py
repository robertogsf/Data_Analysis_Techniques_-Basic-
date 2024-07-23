import pandas as pd

# Load a dataset
df = pd.read_csv('data.csv')

# Normalize a column
df['normalized_column'] = (df['column'] - df['column'].mean()) / df['column'].std()

# Encode categorical variables
df = pd.get_dummies(df, columns=['category'])

# Create new features
df['new_column'] = df['column1'] * df['column2']

print(df.head())

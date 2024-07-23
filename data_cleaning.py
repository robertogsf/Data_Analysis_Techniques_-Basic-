import pandas as pd

# Load a dataset
df = pd.read_csv('data.csv')

# Show the first 5 rows
print(df.head())

# Delete rows with missing values
df.dropna(inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(df.mean(), inplace=True)

print(df.head())

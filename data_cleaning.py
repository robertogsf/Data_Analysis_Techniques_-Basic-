import pandas as pd

# Load the dataset
df = pd.read_csv('./data/data.csv')

# Print the initial data
print("Initial Data:")
print(df)

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Print the cleaned data
print("\nCleaned Data:")
print(df)

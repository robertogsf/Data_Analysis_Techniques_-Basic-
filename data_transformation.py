import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./data/data.csv')

# Normalize a column
df['normalized_feature1'] = (df['feature1'] - df['feature1'].mean()) / df['feature1'].std()

# Print the transformed data
print("Transformed Data:")
print(df)

# Scatter plot of normalized data
plt.scatter(df['feature1'], df['normalized_feature1'])
plt.xlabel('Feature1')
plt.ylabel('Normalized Feature1')
plt.title('Scatter Plot of Feature1 vs Normalized Feature1')
plt.show()
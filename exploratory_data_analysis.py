import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a dataset
df = pd.read_csv('data.csv')

# Describe the data
print(df.describe())

# Histograms of all columns
df.hist(figsize=(10, 8))
plt.show()

# Scatter plot between two variables
sns.scatterplot(data=df, x='column1', y='column2')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
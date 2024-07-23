import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('./data/data.csv')

# Describe the data
print("Data Description:")
print(df.describe())

# Histograms of all numerical columns
df.hist(figsize=(10, 8))
plt.suptitle('Histograms of All Numerical Columns')
plt.show()

# Scatter plot between 'feature1' and 'feature2'
sns.scatterplot(data=df, x='feature1', y='feature2')
plt.title('Scatter Plot between feature1 and feature2')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Correlation matrix (only numerical columns)
numerical_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

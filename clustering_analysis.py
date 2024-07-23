import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./data/data.csv')

# Select numerical columns for clustering
data = df[['feature1', 'feature2']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(data)
df['cluster'] = kmeans.labels_

# Print the clustered data
print("Clustered Data:")
print(df)

# Plot the clusters
plt.scatter(df['feature1'], df['feature2'], c=df['cluster'], cmap='viridis')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.title('Clustering Analysis')
plt.show()

import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('./data/data.csv')

# Create an interactive scatter plot
fig = px.scatter(df, x='feature1', y='feature2', color='category', title='Interactive Scatter Plot of Feature1 vs Feature2')

# Show the plot
fig.show()

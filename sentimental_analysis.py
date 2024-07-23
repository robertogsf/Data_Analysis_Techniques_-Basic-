import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./data/text_data.csv')

# Define a function to get sentiment
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Apply sentiment analysis
df['sentiment'] = df['text'].apply(get_sentiment)

# Print the data with sentiment scores
print("Data with Sentiment Scores:")
print(df)

# Plot sentiment distribution
df['sentiment'].hist(figsize=(10, 6))
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

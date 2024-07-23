import pandas as pd
import matplotlib.pyplot as plt

# Load the time series dataset
df = pd.read_csv('data/time_series_data.csv', parse_dates=['date'], index_col='date')

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(df['value'], marker='o', linestyle='-', color='b')
plt.title('Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Display basic statistics
print("Basic Statistics:")
print(df['value'].describe())

# Rolling Mean and Standard Deviation
rolling_mean = df['value'].rolling(window=3).mean()
rolling_std = df['value'].rolling(window=3).std()

plt.figure(figsize=(10, 6))
plt.plot(df['value'], label='Original Data')
plt.plot(rolling_mean, label='Rolling Mean', color='orange')
plt.plot(rolling_std, label='Rolling Std Dev', color='red')
plt.title('Rolling Mean and Standard Deviation')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

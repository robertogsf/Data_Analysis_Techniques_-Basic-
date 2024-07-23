import pandas as pd
import matplotlib.pyplot as plt

# Load a time series dataset
df = pd.read_csv('time_series_data.csv', parse_dates=['date'], index_col='date')

# Plot the time series
df['value'].plot(figsize=(10, 6))
plt.title('Time Series')
plt.show()

# Decompose the time series
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['value'], model='additive')
result.plot()
plt.show()

import yfinance as yf
import pandas as pd

# Fetch Tesla stock data
tesla_data = yf.download('TSLA', start='2020-01-01', end='2023-01-01')

# Reset index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print(tesla_data.head())

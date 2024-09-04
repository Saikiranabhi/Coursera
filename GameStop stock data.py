# Fetch GameStop stock data
gme_data = yf.download('GME', start='2020-01-01', end='2023-01-01')

# Reset index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())

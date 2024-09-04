import matplotlib.pyplot as plt

def make_graph(df, title):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot Tesla stock data
make_graph(tesla_data, 'Tesla Stock Price')

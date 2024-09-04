import requests
from bs4 import BeautifulSoup

# Fetch the Tesla revenue data from a website (replace URL with the actual one)
url = 'https://example.com/tesla-revenue'  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Parse revenue data (depends on website structure)
# For demonstration, assuming you have a DataFrame
tesla_revenue = pd.DataFrame()  # Replace this with actual data extraction code

# Display the last five rows
print(tesla_revenue.tail())

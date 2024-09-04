# Fetch the GameStop revenue data from a website (replace URL with the actual one)
url = 'https://example.com/gme-revenue'  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Parse revenue data (depends on website structure)
# For demonstration, assuming you have a DataFrame
gme_revenue = pd.DataFrame()  # Replace this with actual data extraction code

# Display the last five rows
print(gme_revenue.tail())

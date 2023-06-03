import requests

# Specify the API endpoint
url = 'http://api.worldbank.org/v2/en/indicator'

# Specify the query parameters
params = {
    'format': 'json',  # Retrieve data in JSON format
    'source': '88',  # Food Prices for Nutrition
    'series': 'CoM.*,CoD.*,CoF.*,CoV.*',  # Cost of Meat, Dairy, Fruits, Vegetables
    'date': '2017',  # Year: 2017
    'per_page': 500,  # Number of results per page (maximum: 500)
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Process the data
    for entry in data[1]:
        country = entry['country']['value']
        indicator = entry['indicator']['value']
        value = entry['value']

        # Print the data or do further processing
        print('Country:', country)
        print('Indicator:', indicator)
        print('Value:', value)
        print()
else:
    print('Failed to retrieve data. Status code:', response.status_code)
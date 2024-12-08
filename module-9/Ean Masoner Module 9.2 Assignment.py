import requests

# Define the API endpoint
api_url = "http://api.open-notify.org/astros.json"

# Test the connection to the API and get the response
response = requests.get(api_url)

# Print out the response from the request, with no formatting
print("Response with no formatting:")
print(response.text)

# Print out the response with formatting
print("\nResponse with formatting:")
data = response.json()
print(f"There are {data['number']} astronauts in space right now:")
for person in data['people']:
    print(f"- {person['name']} on {person['craft']}")

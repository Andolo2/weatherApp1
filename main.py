import requests  # For updating req from API

API_KEY = "5f35ee86aacae6c71b37204194452b88"
URL = "https://api.openweathermap.org/data/2.5/weather" # Base url

city = input("Enter a city of your choice: ")

requests_url = f"{URL}?appid={API_KEY}&q={city}" # F-string, URL, and the query searches for data from the users input.

response = requests.get(requests_url) # Get request to URL

if response.status_code == 200: # Check if the https error code is 200 (OK) in case apikey has expired.
    data = response.json()
    weather = data["weather"][0]["description"] # Access the data from the api and sort out the information i need... (weather and temp)

    temprature = round(data["main"]["temp"] - 273.15) # The api returns the temp in kelvin.. Need to do a conversion to Celsius. Also rounds the number to a whole int.

    print("Today´s weather is: ", weather)
    print("And the temprature is: ", temprature, "°c")

else:
    print("Could not retrieve information, check API key ")

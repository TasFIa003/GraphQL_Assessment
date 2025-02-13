import requests
import time
import csv

#fetching country data from the GraphQL API
def fetchCountries():
    url = "https://countries.trevorblades.com/"
    query = """
    query {
      countries {
        name
        capital
        currency
      }
    }
    """
    response = requests.post(url, json={'query': query}) #sending request to API
    code= response.status_code
    if code == 200:
        # extracting relevant data
        return response.json().get("data", {}).get("countries", [])
    else:
        # logging error
        print(f"Error fetching countries: {code}")
        return []
# Function for posting a selected country's details to a REST API
def postCountry(country):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": f"Country: {country['name']}",
        "body": f"Capital: {country['capital']}, Currency: {country['currency']}",
        "userId": 1
    }
    
    attempts = 3 # retry attempts number
    delay = 1  # Initial delay in seconds
    
    for attempt in range(attempts):
        response = requests.post(url, json=payload)
        code= response.status_code

        if code == 201: #success case
            return response.json()
        elif code == 403: #forbidden error, skipping
            print("403 Forbidden -> Skipping request.")
            return None
        elif code == 500: # Internal server error.Retry the request with exponential backoff.
            print(f"500 Internal Server Error -> Retrying in {delay} seconds.")
            time.sleep(delay)
            delay *= 2  # Increase delay exponentially
        else:
            print(f"Unexpected error: {code}") # logging other errors
            return None

# function for saving all fetched country data to a csv file
def saveCountries(countries, filename="countries.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Country Name", "Capital", "Currency"]) # headers of CSV file
        for country in countries:
            writer.writerow([country["name"], country.get("capital", "N/A"), country.get("currency", "N/A")])


# Main function to automate the entire workflow
def main():
    countries = fetchCountries()
    if not countries:
        # If no data is fetched then exit
        print("No countries fetched.")
        return
    
    selectedCountry = countries[0]  # Selecting the first country
    print(f"Posting details of {selectedCountry['name']}")
    response = postCountry(selectedCountry) # posting country details
    
    if response:
        print("Posted successfully:", response)
    
    saveCountries(countries) # saving all data to CSV
    print("Countries saved to CSV successfully.")

if __name__ == "__main__":
    main()

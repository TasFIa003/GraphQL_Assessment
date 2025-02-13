import requests
import time
import csv

def fetch_countries():
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
    response = requests.post(url, json={'query': query})
    
    if response.status_code == 200:
        return response.json().get("data", {}).get("countries", [])
    else:
        print(f"Error fetching countries: {response.status_code}")
        return []

def post_country(country):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": f"Country: {country['name']}",
        "body": f"Capital: {country['capital']}, Currency: {country['currency']}",
        "userId": 1
    }
    
    retry_attempts = 3
    delay = 1  # Initial delay in seconds
    
    for attempt in range(retry_attempts):
        response = requests.post(url, json=payload)
        
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 403:
            print("403 Forbidden: Skipping request.")
            return None
        elif response.status_code == 500:
            print(f"500 Internal Server Error: Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
        else:
            print(f"Unexpected error: {response.status_code}")
            return None

def save_to_csv(countries, filename="countries.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Country Name", "Capital", "Currency"])
        for country in countries:
            writer.writerow([country["name"], country.get("capital", "N/A"), country.get("currency", "N/A")])

def main():
    countries = fetch_countries()
    if not countries:
        print("No countries fetched. Exiting...")
        return
    
    selected_country = countries[0]  # Selecting the first country
    print(f"Posting details of {selected_country['name']}...")
    response = post_country(selected_country)
    
    if response:
        print("Posted successfully:", response)
    
    save_to_csv(countries)
    print("Countries saved to CSV.")

if __name__ == "__main__":
    main()

# Candidate API Test
### This Python script interacts with a GraphQL API to fetch country data using a GraphQL API, selects a country, and posts its details to a REST API. It also handles errors and saves all country data to a CSV file.

## Features
* Fetches country data from the [GraphQL API](https://countries.trevorblades.com/).
* Posts a selected country's details to a REST API [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts).
* Handles HTTP errors such as 403: skipping requests, 500 internal server error with retrying with exponential backoff, and logging all errors for debugging.
* Saves all the data to a CSV `countries.csv`.
* Automates the workflow, chaining data fetching, processing, posting, and saving.    

## Requirements
* Python 3.x
* `requests` library (to handle API requests)


## Installation
* Install dependencies:
  ```
  pip install requests
  ```
* Run the script
  ```
  python script.py
  ```
### Note: `time` and `CSV` are built-in Python libraries, so do not need to install them separately.

## Workflow Execution
* The script queries the GraphQL API to retrieve country data.
* It extracts the country name, capital, and currency.
* It selects the first country from the list.
* It sends the country's details as a POST request to the REST API.
* It handles any errors encountered.
* It saves all country data into a countries.csv file.
* It logs relevant success and error messages to the console.

## Expected Output:
* Console output:
  * Fetched country details
  * Posted country details successfully (or logs errors if any occur).
  * Confirmation message for CSV file creation.
    
*  Generates a CSV file named `countries.csv` in the same directory which contains all the details of all fetched countries.

## Error Handling
* `403 Forbidden`: The requests are skipped.
* `500 Internal Server Error`: The requests retry with exponential backoff.
* Other errors are logged to the console.

## Further Improvements:
* Extending error handling for additional API failure cases.
* Storing API responses in a database instead of a CSV file.

  
## Notes
* Ensure a stable internet connection while running the script.
* Modify the script as needed for additional functionality or custom requirements. 


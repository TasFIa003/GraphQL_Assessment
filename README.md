# Candidate API Test
### This Python script interacts with a GraphQL API to fetch country data using a GraphQL API, selects a country, and posts its details to a REST API. It also handles errors and saves all country data to a CSV file.

## Features
1. Fetches country data from the [GraphQL API](https://countries.trevorblades.com/))
2. Posts a selected country's details to a REST API.
3. Handles HTTP errors such as 403: skipping requests, 500 internal server error with retrying with exponential backoff.
4. Saves all the data to a CSV "countries.csv".

## Requirements
* Python 3.x
* requests library

## Installation
* Install dependencies:
  ```
  pip install requests
  ```
* Run the script
  ```
  python script.py
  ```

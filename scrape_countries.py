import pandas as pd
import requests
import re

# Read the CSV file
watched_movies = pd.read_csv('watched.csv')

def get_country_of_origin(letterboxd_uri):
    url = f'{letterboxd_uri}'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text

        # Find all lines that contain "/films/country/"
        lines_containing_country = []
        for line in html_content.splitlines():
            if '/films/country' in line:
                lines_containing_country.append(line.strip())


        country_names=[]
        if lines_containing_country:
            for line in lines_containing_country:
                country_names.append(re.findall(r'/films/country/([^/]+)/', line))
            return country_names
        
        else:
            print("No lines containing '/films/country/' found.")
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return ''

# Initialize an empty list to accumulate countries
all_countries = []

# Iterate over each URI in watched_movies
for uri in watched_movies['Letterboxd URI']:
    countries_list = get_country_of_origin(uri)
    if countries_list:
        all_countries.append(countries_list)
    else:
        all_countries.append([])  # Append empty list if no countries found for robustness

# Convert the accumulated list of lists to a DataFrame
countries_df = pd.DataFrame(all_countries)

# Save the results to a CSV file
countries_df.to_csv('countries_of_origin.csv', index=False)

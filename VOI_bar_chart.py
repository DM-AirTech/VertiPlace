# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Thu August 10 14:18:00 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: Generates a bar chart for visualizing the mean VOI (VertiPort Operability Index) calculated on top 10 cities (by population) of a country.
IMPORTANT: Replace API_KEY with the API_KEY provided to you. 
"""

import pandas as pd
import subprocess
import numpy as np
import matplotlib.pyplot as plt

# read the CSV file
df = pd.read_csv('worldcities.csv')

# function to get top 10 cities by population for a given country
def get_top_cities(country):
    # filter rows for the given country
    country_data = df[df['country'] == country]
    
    # sort by population and get the top 10 cities
    top_cities = country_data.sort_values(by='population', ascending=False).head(10)
    
    # select only relevant columns
    top_cities = top_cities[['city', 'lat', 'lng', 'population']]
    
    return top_cities

def get_voi(city):
    lat = city['lat']
    lng = city['lng']

    result = subprocess.run(['python3', 'main.py', '--api_key', 'API_KEY', 
                             '--lat', str(lat), '--lon', str(lng), '--gust', '10.3', '--t_min', '-6.7', 
                             '--t_max', '42', '--rain', '25', '--hours', '12', '--seasons', '1'], 
                            stdout=subprocess.PIPE)

    output = result.stdout.decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if line.startswith('Operability'):
            voi = float(line.split('=')[1].strip('%\r').strip())
            return voi
    return None

countries = ['Spain', 'France', 'United Kingdom', 'Germany', 'Italy'] # replace with your country names

vois_avg = []
vois_min = []
vois_max = []

for country in countries:
    top_cities = get_top_cities(country)
    vois = []
    for _, city in top_cities.iterrows():
        voi = get_voi(city)
        if voi is not None:
            vois.append(voi)
    
    vois_avg.append(np.mean(vois))
    vois_min.append(min(vois))
    vois_max.append(max(vois))

error = [np.array(vois_avg) - np.array(vois_min), np.array(vois_max) - np.array(vois_avg)]

plt.bar(countries, vois_avg, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
plt.ylabel('VertiPort Operability Index (VOI)')
plt.title('mean VOI for the top 10 cities (by population) of different Countries')
plt.show()




# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Thu August 10 14:18:00 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: Generates radar charts for the impact of different factors on the VOI (VertiPort Operability Index)
IMPORTANT: Replace API_KEY with the API_KEY provided to you. 
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
# from sklearn.preprocessing import MinMaxScaler

# read the CSV file
df = pd.read_csv('worldcities.csv')

def get_voi(city, gust=15, t_min=-6.7, t_max=42, rain=25, w10=10, w100=12, hours="1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24", seasons="1,2,3,4"):
    lat = city['lat']
    lng = city['lng']
    result = subprocess.run(['python3', 'main.py', '--api_key', 'API_KEY', 
                             '--lat', str(lat), '--lon', str(lng), '--gust', str(gust), '--t_min', str(t_min), 
                             '--t_max', str(t_max), '--rain', str(rain), '--w10', str(w10), '--w100', str(w100), 
                             '--hours', str(hours), '--seasons', str(seasons)], 
                            stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if line.startswith('Operability'):
            voi = float(line.split('=')[1].strip('%\r').strip())
            return voi
    return None

def get_mean_voi(city_datas, **kwargs):
    total_voi = 0
    count = 0

    if isinstance(city_datas, pd.DataFrame):  # if city_datas is a DataFrame, iterate through its rows
        for index, city_data in city_datas.iterrows():
            total_voi += get_voi(city_data, **kwargs)
            count += 1
    else:  # else, assume city_datas is a list of Series
        for city_data in city_datas:
            total_voi += get_voi(city_data, **kwargs)
            count += 1

    return total_voi / count if count > 0 else None

def simulate_voi(city_datas, gust=15, t_min=-6.7, t_max=42, rain=25, w10=10, w100=12, deltas=[0,0.1,0.2]):
    parameters = {'gust': gust, 't_min': t_min, 't_max': t_max, 'rain': rain, 'w10': w10, 'w100': w100}
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    max_voi = 0  # initialize max_voi variable
    min_voi = float('inf')  # initialize min_voi variable

    for delta in deltas:
        voi_values = []
        labels = []

        for param, value in parameters.items():
            if value != 0:  # Skip parameters with zero values
                labels.append(param)
                voi_changed = get_mean_voi(city_datas, **{**parameters, param: value * (1 + delta)})
                min_voi = min(min_voi, voi_changed)  # update min_voi if necessary

        base_voi = min_voi * 0.9  # 90% of minimum VOI
        for param, value in parameters.items():
            if value != 0:  # Skip parameters with zero values
                voi_changed = get_mean_voi(city_datas, **{**parameters, param: value * (1 + delta)})
                voi_values.append(voi_changed - base_voi)
                max_voi = max(max_voi, voi_changed)  # update max_voi if necessary

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        voi_values += voi_values[:1]
        angles += angles[:1]
        labels += labels[:1]

        if delta == 0:
            ax.plot(angles, voi_values, alpha=0.6, lw=2, linestyle='solid', label='Initial mean VOI', marker='o')
        else:
            ax.plot(angles, voi_values, alpha=0.6, lw=2, linestyle='solid', label=f'delta={delta*100:.0f}%', marker='o')
    
    ax.set_thetagrids(np.degrees(angles), labels)

    ax.set_yticks(np.linspace(0, max_voi - base_voi, 5))  # set y ticks positions

    yticklabels = list(map(str, np.round(np.linspace(base_voi, max_voi, 5), 2)))  # convert map to list
    yticklabels = [f'{round(float(val), 1)}' for val in yticklabels]  # convert string to float, then round
    ax.set_yticklabels(yticklabels, fontsize=12)  # set the y tick labels with increased font size


    ax.spines['polar'].set_visible(False) 
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
    plt.show()


# single city
city_name = "London"
city_data = df[df['city'] == city_name].iloc[0]
simulate_voi([city_data])

# multiple cities
# city_names = ["London", "Los Angeles", "Abu Dhabi"]
# city_datas = [df[df['city'] == name].iloc[0] for name in city_names]
# simulate_voi(city_datas)

# # top 10 cities of a country
# country_name = "France"
# city_datas = df[df['country'] == country_name].nlargest(10, 'population')
# print(city_datas)
# simulate_voi(city_datas)

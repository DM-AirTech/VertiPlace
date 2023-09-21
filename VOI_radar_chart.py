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

def get_voi(city, api_key, **kwargs):
    lat = city['lat']
    lng = city['lng']
    
    cmd_args = ['python3', 'main.py', '--api_key', str(api_key), 
                '--lat', str(lat), '--lon', str(lng)]
    
    # Add all passed-in parameters to cmd_args at once
    for key, value in kwargs.items():
        cmd_args.append(f'--{key}')
        cmd_args.append(str(value))
    
    print(cmd_args)  # For debugging
    result = subprocess.run(cmd_args, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if line.startswith('Operability'):
            voi = float(line.split('=')[1].strip('%\r').strip())
            return voi
    return None

def get_mean_voi(city_datas, api_key, **kwargs):
    total_voi = 0
    count = 0
    print(kwargs)
    if isinstance(city_datas, pd.DataFrame):  # if city_datas is a DataFrame, iterate through its rows
        for index, city_data in city_datas.iterrows():
            total_voi += get_voi(city_data, api_key, **kwargs)
            count += 1
    else:  # else, assume city_datas is a list of Series
        for city_data in city_datas:
            total_voi += get_voi(city_data, api_key, **kwargs)
            count += 1

    return total_voi / count if count > 0 else None

def simulate_voi(city_datas, deltas, **kwargs):
    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(polar=True))
    max_voi = 0
    min_voi = float('inf')
    api_key = kwargs.get('api_key')

    original_params = {k: v for k, v in kwargs.items() if isinstance(v, (float, int))}

    for delta in deltas:
        voi_values = []
        labels = []

        # Apply delta to each parameter individually and record its effect
        for param in original_params.keys():
            temp_params = original_params.copy()
            temp_params[param] *= (1 + delta)
            
            # Update min and max VOI values
            voi_changed = get_mean_voi(city_datas, api_key, **temp_params)
            min_voi = min(min_voi, voi_changed)
            max_voi = max(max_voi, voi_changed)

            # Calculate base VOI and VOI change
            base_voi = min_voi * 0.9
            voi_values.append(voi_changed - base_voi)
            labels.append(param)

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

def generate_VOI_radar_chart(args):
    city_names = args.city.split(',')
    city_datas = [df[df['city'] == name.strip()].iloc[0] for name in city_names]
      # Convert args to a dictionary
    args_dict = vars(args)
    deltas = args.delta if args.delta is not None else [0, 0.1, 0.2]

    args_dict = {k: v for k, v in args_dict.items() if v is not None}
    # Remove keys that aren't needed for simulate_voi
    for key in ['city', 'visualize', 'lat', 'lon']:
        args_dict.pop(key, None)

    
    # Call simulate_voi with the remaining args
    simulate_voi(city_datas, deltas=deltas, **args_dict)


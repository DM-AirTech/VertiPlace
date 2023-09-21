# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 24 12:45:06 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: This module is responsible for handling and parsing command line arguments. 
It defines the requirements and specifications for the arguments, and prepares 
them for use in the main program.
"""


import argparse
from checks import float_range_1, float_range_2, float_range_3, float_range_4, float_range_5, float_range_6, binary_values
from checks import check_hours, check_seasons

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI (Python3) for VertiPlace2.1", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--api_key", type=str, help="API key for VertiPlace2.1 (contact: info@dm-airtech.com)")
    parser.add_argument("--lat", type=float, help="Latitude of the location (float value)")
    parser.add_argument("--lon", type=float, help="Longitude of the location (float value)")
    parser.add_argument("--w10", type=float_range_1, help="average wind resistance at 10m (in m/s)")
    parser.add_argument("--w100", type=float_range_1, help="average wind resistance at 100m (in m/s)")
    parser.add_argument("--gust", type=float_range_1, help="gust wind resistance (in m/s)")
    parser.add_argument("--rain", type=float_range_1, help="rain resistance (in m/s)")
    parser.add_argument("--t_min", type=float_range_2, help="minimum temperature resistance (in degrees)")
    parser.add_argument("--t_max", type=float_range_2, help="maximum temperature resistance (in degrees)")
    parser.add_argument("--p_alt", type=float_range_3, help="pressure altitude limit (in hPa)")
    parser.add_argument("--min_fl", type=float_range_4, help="minimum flight level above ground (in m)")
    parser.add_argument("--min_vis", type=float_range_5, help="minimum visibility (in m)")
    parser.add_argument("--min_cbh", type=float_range_6, help="minimum cloud base height above ground level (in m)")
    parser.add_argument("--icing", type=binary_values, help="accound for icing conditions (0=no or 1=yes)")
    parser.add_argument("--visualize", type=str, choices=["radar"], help="Visualize data with a radar chart")
    parser.add_argument("--city", type=str, help="Comma-separated list of city names for the analysis", default="London")
    parser.add_argument('--delta', type=float, nargs='+', help='List of delta values to consider')

    # parser.add_argument("--thunder", type=str)
    # parser.add_argument("--hail", type=str)
    # parser.add_argument("--blizz", type=str)
    parser.add_argument("--hours", type=check_hours, help="Comma-separated list of integers from 1 to 24 to represent hours of the day", default="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24")
    parser.add_argument("--seasons", type=check_seasons, help="Comma-separated list of integers from 1 to 4 to represent quarters of the year", default="1,2,3,4")

    return parser.parse_args()

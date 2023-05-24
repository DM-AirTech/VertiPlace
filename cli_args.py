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

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI (Python3) for VertiPlace2.1", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--api_key", type=str, required=True)
    parser.add_argument("--lat", type=str, required=True)
    parser.add_argument("--lon", type=str, required=True)
    parser.add_argument("--w10", type=str)
    parser.add_argument("--w100", type=str)
    parser.add_argument("--gust", type=str)
    parser.add_argument("--rain", type=str)
    parser.add_argument("--t_min", type=str)
    parser.add_argument("--t_max", type=str)
    parser.add_argument("--p_alt", type=str)
    parser.add_argument("--min_fl", type=str)
    parser.add_argument("--min_vis", type=str)
    parser.add_argument("--min_cbh", type=str)
    parser.add_argument("--icing", type=str)
    parser.add_argument("--thunder", type=str)
    parser.add_argument("--hail", type=str)
    parser.add_argument("--blizz", type=str)
    parser.add_argument("--hours", type=str, required=True)
    parser.add_argument("--seasons", type=str, required=True)

    return parser.parse_args()

# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 24 12:45:06 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: The entry point of the program. This module uses the parsed arguments, calls the 
necessary functions to make the API request, and handles the output of results.
The main coordination and execution of the program happen here.
"""

from url_builder import url_string_generator
from cli_args import parse_arguments
from checks import check_args

if __name__ == '__main__':
    from utils import process_output
    

    args = parse_arguments()
    check_args(args)
    output = url_string_generator(args.api_key, args.lat, args.lon, args.w10, args.w100, args.gust, args.rain, args.t_min, args.t_max, args.p_alt, args.min_fl, args.min_vis, args.min_cbh, args.icing, args.hours, args.seasons)
    output_list = process_output(output)
    print('Operability=' + output_list[1] + '%') 
    print('h3_index=' + output_list[0])
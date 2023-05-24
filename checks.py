# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 24 12:45:06 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: Checks the CLI arguments for the required conditions.
"""
import argparse

def check_args(args):
    """
    Args:
        args: The parsed arguments from argparse.ArgumentParser().

    Raises:
        argparse.ArgumentTypeError: If the arguments do not meet the required conditions.
    """
    
    if not (
        args.w10 or args.w100 or args.gust or args.rain 
        or (args.t_min and args.t_max) 
        or (args.p_alt and args.min_fl) 
        or args.min_vis or args.min_cbh or args.icing
    ):
        raise argparse.ArgumentTypeError("At least one of the following needs to be given in addition to the required fields: \
                                          'w10', 'w100', 'gust', 'rain', 't_min' & 't_max' (both together), 'p_alt' & 'min_fl' (both together), 'min_vis', 'min_cbh', 'icing'")

#check for the parameters w10, w100, gust, rain
def float_range_1(value):
    fvalue = float(value)
    if fvalue < 0 or fvalue > 50:
        raise argparse.ArgumentTypeError(f"Invalid float value: {value}. Expected a value between 0 and 50.")
    return fvalue

#check for t_min and t_max
def float_range_2(value):
    fvalue = float(value)
    if fvalue < -50 or fvalue > 100:
        raise argparse.ArgumentTypeError(f"Invalid float value: {value}. Expected a value between -50 and 100.")
    return fvalue

#check for p_alt
def float_range_3(value):
    fvalue = float(value)
    if fvalue < 200 or fvalue > 1200:
        raise argparse.ArgumentTypeError(f"Invalid float value: {value}. Expected a value between 200 and 1200.")
    return fvalue

#check for min_fl
def float_range_4(value):
    fvalue = float(value)
    if fvalue < 0 or fvalue > 6000:
        raise argparse.ArgumentTypeError(f"Invalid float value: {value}. Expected a value between 0 and 6000.")
    return fvalue

#check for min_vis
def float_range_5(value):
    fvalue = float(value)
    if fvalue < 0 or fvalue > 10000:
        raise argparse.ArgumentTypeError(f"Invalid float value: {value}. Expected a value between 0 and 10000.")
    return fvalue

#check for min_cbh
def float_range_6(value):
    fvalue = float(value)
    if fvalue < 0 or fvalue > 20000:
        raise argparse.ArgumentTypeError(f"Invalid float value: {value}. Expected a value between 0 and 20000.")
    return fvalue

#check for icing
def binary_values(value):
    ivalue = int(value)
    if ivalue < 0 or ivalue > 1:
        raise argparse.ArgumentTypeError(f"Invalid integer value: {value}. Expected a value 0 or 1.")
    return ivalue


def check_hours(value):
    try:
        hours = list(map(int, value.split(',')))
    except ValueError:
        raise argparse.ArgumentTypeError("hours should be a comma-separated list of integers from 1 to 24")

    if not all(1 <= hour <= 24 for hour in hours):
        raise argparse.ArgumentTypeError("All hour values should be in the range from 1 to 24")

    return value

def check_seasons(value):
    try:
        seasons = list(map(int, value.split(',')))
    except ValueError:
        raise argparse.ArgumentTypeError("seasons should be a comma-separated list of integers from 1 to 4")

    if not all(1 <= season <= 4 for season in seasons):
        raise argparse.ArgumentTypeError("All season values should be in the range from 1 to 4")

    return value

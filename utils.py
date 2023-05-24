# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 24 12:45:06 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: This module contains a set of utility functions responsible for calculating 
environmental parameters such as atmospheric pressure and altitude conversion. These functions 
are utilized in the main program to compute necessary parameters for constructing the API request.
"""

import math 

def process_output(output):
    output = output.replace("\\","").replace("\"","").replace('n', '') 
    output_list = output.split('_') 
    output_list[1] = float(output_list[1])*100 
    output_list[1] = str(output_list[1]) 
    return output_list

def ft2m(H): 
# Convert altitude in feet to meters    
    return round(H / 3.28084, 3) 
 
def m2ft(H): 
# Convert altitude in meters to feet 
    return round(H * 3.28084, 3) 
 
def Pamb(H, **kwargs): 
 
    QNH = kwargs.get('QNH', None) 
    TSL = kwargs.get('TSL', None) 
    Pstrat = 0.0 
    PSL = 0.0 
    Temp = 0.0 
    Htrop = 0.0 
    if QNH is None: 
      PSL = 1013.25 
    else: 
      PSL = QNH 
     
    if TSL is None: 
      Temp = 15 
      Htrop = 36089.24 
    else: 
      Temp = TSL 
      Htrop = 36089.24 + (Temp - 15) / 0.0019812 
     
    if (H < 65616.79 and H > -16404.19): 
      if H < Htrop: 
        Pamb = PSL * (1 - (0.0019812 / (273.15 + Temp)) * H) ** 5.2558797 
      else: 
        Pstrat = PSL * (1 - (0.0019812 / (273.15 + Temp)) * Htrop) ** 5.2558797 
        Pamb = Pstrat * math.exp(-0.00004806346 * (H - Htrop)) 
    else: 
      Pamb = "#WERT!" 
     
    return round(Pamb,3) 
 
def H(Pamb, **kwargs): 
 
    QNH = kwargs.get('QNH', None) 
    TSL = kwargs.get('TSL', None) 
    Pstrat = 0.0 
    PSL = 0.0 
    Temp = 0.0 
    Htrop = 0.0 
    if QNH is None: 
      PSL = 1013.25 
    else: 
      PSL = QNH 
     
    if TSL is None: 
      Temp = 15 
      Htrop = 36089.24 
    else: 
      Temp = TSL 
      Htrop = 36089.24 + (Temp - 15) / 0.0019812 
 
    Pstrat = PSL * (1 - (0.0019812 / (273.15 + Temp)) * Htrop) ** 5.2558797 
     
    if (Pamb > 54.749 and Pamb < 1776.87): 
      if Pamb > Pstrat: 
        H = (1 - (Pamb / PSL) ** 0.1902631) / (0.0019812 / (273.15 + Temp)) 
      else: 
        H = Htrop - 20805.8263 * math.log(Pamb / Pstrat) 
    else: 
      H = "#WERT!" 
     
    return round(H, 2) 
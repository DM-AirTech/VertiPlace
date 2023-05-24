# -*- coding: utf-8 -*-
"""
Company Name: DM-AirTech GmbH
Author: Harsh Panwar
Email: harsh@dm-airtech.com
Created on: Mon May 24 12:45:06 2023

Copyright (c) 2023, DM-AirTech GmbH

Description: This script holds the `url_string_generator` function which is used to 
construct a URL for API request. The function takes several weather-related parameters, 
constructs an API call, makes the request, and returns the response as a text string.
This function is essential for querying the VertiPlaceGWC API and receiving relevant data 
for further processing.
"""


import requests 
from utils import m2ft, ft2m, Pamb, H

def url_string_generator(api_key,lat, lon, w10, w100, gust, rain, t_min, t_max, p_alt, min_fl, min_vis, min_cbh, icing, hours, seasons):  
    if p_alt and min_fl: 
      pres_lim = str(Pamb(H(float(p_alt)) + m2ft(float(min_fl)))) 
    else: 
      pres_lim = "" 
 
    url_string='https://www.dm-airtech.eu/api/VP2API' 
    url_string= url_string + '?apikey=' + api_key #required 
    url_string= url_string + '&lat=' + str(lat) #required 
    url_string= url_string + '&lon=' + str(lon) #required 
    if w10: 
      url_string= url_string + '&max_speed10=' + str(w10) 
    if w100: 
      url_string= url_string + '&max_speed100=' + str(w100) 
    if gust: 
      url_string= url_string + '&max_gust=' + str(gust)
    if t_max: 
      url_string= url_string + '&max_temp=' + str(t_max) 
    if t_min: 
      url_string= url_string + '&min_temp=' + str(t_min)
    if rain: 
      url_string= url_string + '&max_rain=' + str(rain)
    if pres_lim: 
      url_string= url_string + "&preslim=" + str(pres_lim) 
    if min_cbh: 
      url_string= url_string + '&min_cbh=' + str(min_cbh)
    if min_vis: 
      url_string= url_string + '&min_vis=' + str(min_vis)
    if icing: 
      url_string= url_string + '&icing=' + str(icing) 
    # if thunder: 
    #   url_string= url_string + '&thunder=' + thunder 
    # if hail: 
    #   url_string= url_string + '&hail=' + hail 
    # if blizz: 
    #   url_string= url_string + '&blizz=' + blizz 
    url_string= url_string + '&hours=' + hours #req 
    url_string= url_string + '&seasons=' + seasons #req 
    x = requests.get(url_string) 
    return x.text 
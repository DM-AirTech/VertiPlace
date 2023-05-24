import requests 

def url_string_generator(api_key,lat, lon, w10, w100, gust, rain, t_min, t_max, p_alt, min_fl, min_vis, min_cbh, icing, thunder, hail, blizz, hours, seasons):  
    if p_alt and min_fl: 
      pres_lim = str(Pamb(H(float(p_alt)) + m2ft(float(min_fl)))) 
    else: 
      pres_lim = "" 
 
    url_string='https://www.dm-airtech.eu/api/VP2API' 
    url_string= url_string + '?apikey=' + api_key #required 
    url_string= url_string + '&lat=' + lat #required 
    url_string= url_string + '&lon=' + lon #required 
    if w10: 
      url_string= url_string + '&max_speed10=' + w10 
    if w100: 
      url_string= url_string + '&max_speed100=' + w100 
    if gust: 
      url_string= url_string + '&max_gust=' + gust 
    if t_max: 
      url_string= url_string + '&max_temp=' + t_max 
    if t_min: 
      url_string= url_string + '&min_temp=' + t_min 
    if rain: 
      url_string= url_string + '&max_rain=' + rain 
    if pres_lim: 
      url_string= url_string + "&preslim=" + pres_lim 
    if min_cbh: 
      url_string= url_string + '&min_cbh=' + min_cbh 
    if min_vis: 
      url_string= url_string + '&min_vis=' + min_vis 
    if icing: 
      url_string= url_string + '&icing=' + icing 
    if thunder: 
      url_string= url_string + '&thunder=' + thunder 
    if hail: 
      url_string= url_string + '&hail=' + hail 
    if blizz: 
      url_string= url_string + '&blizz=' + blizz 
    url_string= url_string + '&hours=' + hours #req 
    url_string= url_string + '&seasons=' + seasons #req 
    x = requests.get(url_string) 
    return x.text 
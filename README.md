# VertiPlace<sup>GWC</sup>

![Python](https://img.shields.io/badge/Python-3-blue)
![Version](https://img.shields.io/badge/Version-2.1-blue)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://uk.linkedin.com/company/dm-airtech)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fwww.dm-airtech.com/)](https://www.dm-airtech.com/)

## 1. Introduction
VertiPlace<sup>GWC</sup> is a software solution that correlates hourly weather data available at the climate scale, given geography and VTOL specifications, to query and perform customized Operability Analysis for the positioning of Vertiports.

Note: This GitHub repository focuses on the API of VertiPlace<sup>GWC</sup>. For access to the GUI, please visit our website directly.

![Screenshot 2023-05-24 140840](https://github.com/DM-AirTech/VertiPlace/assets/40840002/cbe33e91-6687-45ce-b7e6-52e404c624c7)


## 2. Obtaining API Key

To access the VertiPlace<sup>GWC</sup> data through the API, you will need an API key. Please contact our sales team at info@dm-airtech.com to obtain your API key.

## 3. Usage

To run the VertiPlace<sup>GWC</sup> Python API, follow the steps below:

1. Clone the VertiPlace repository from Github to your local machine by running the following command:
```bash
git clone https://github.com/DM-AirTech/VertiPlace.git
```
2. Install the required packages:

```bash
pip install -r requirements.txt
```
3. Change your current directory to the VertiPlace directory:
```bash
cd VertiPlace`
```
4. Run the main.py file from the terminal, supplying the necessary arguments. An example is shown below:
```
python3 main.py --api_key API_KEY --lat=34.052238 --lon=-118.243344 --gust=10.3 --t_min=-6.7 --t_max=42 --rain=25 --hours=12 --seasons=1     
```
Make sure to replace API_KEY with your actual API key.

The usage for each parameter can be found using the help command:
`python main.py --help`
```
CLI (Python3) for VertiPlace2.1

options:
  -h, --help         show this help message and exit
  --api_key API_KEY  API key for VertiPlace2.1 (contact: info@dm-airtech.com) (default: None)
  --lat LAT          Latitude of the location (float value) (default: None)
  --lon LON          Longitude of the location (float value) (default: None)
  --w10 W10          average wind resistance at 10m (in m/s) (default: None)
  --w100 W100        average wind resistance at 100m (in m/s) (default: None)
  --gust GUST        gust wind resistance (in m/s) (default: None)
  --rain RAIN        rain resistance (in m/s) (default: None)
  --t_min T_MIN      minimum temperature resistance (in degrees) (default: None)
  --t_max T_MAX      maximum temperature resistance (in degrees) (default: None)
  --p_alt P_ALT      pressure altitude limit (in hPa) (default: None)
  --min_fl MIN_FL    minimum flight level above ground (in m) (default: None)
  --min_vis MIN_VIS  minimum visibility (in m) (default: None)
  --min_cbh MIN_CBH  minimum cloud base height above ground level (in m) (default: None)
  --icing ICING      accound for icing conditions (0=no or 1=yes) (default: None)
  --hours HOURS      Comma-separated list of integers from 1 to 24 to represent hours of the day (default:
                     0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
  --seasons SEASONS  Comma-separated list of integers from 1 to 4 to represent quarters of the year (default: 1,2,3,4)
```
This will output a description and usage for each argument.

Remember that in addition to the required parameters (api_key, lat, lon, hours, seasons), you must provide at least one of the following: `w10, w100, gust, rain, t_min & t_max (both together), p_alt & min_fl (both together), min_vis, min_cbh, icing.`

## 4. Output
Below is an example of the output received based on the example input used in the previous section:
```
Operability=86.04%
h3_index=8529a1d7fffffff
```
## 4. Visualization
Run the VOI_bar_chart.py and VOI_radar_chart.py to visualize the bar and radar charts.
Here are some example charts generated:

<p float="left">
  <img src="https://github.com/DM-AirTech/VertiPlace/assets/40840002/ec73b9d4-29dc-46e9-8cf7-8a40acd7bd60" width="49%" />
  <img src="https://github.com/DM-AirTech/VertiPlace/assets/40840002/21d6d8fa-e2cc-4faa-89d1-a773d36c8cce" width="49%" /> 
</p>




## Support

For any questions, concerns, or technical support, please reach out to our dedicated support team at info@dm-airtech.com. 

---

© 2023 DM-AirTech. All rights reserved.

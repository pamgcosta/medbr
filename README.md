# medbr: Geographic Health Data Sets of Brazil

<img align="right" src="https://github.com/pamgcosta/medbr/assets/66846949/2cbfe684-a173-42dd-8bfc-c579438ceab3" alt="logo" width="320"> 
<p align="justify">medbr is a computational package for visualizing public health data in Brazil in geospatial format. The package includes a geospatial data functions available with variable parameters to obtain a geospatial visualization of the data. </p> 

The package is currently available in [Python](https:).
(Arrumar links)
| ***Python*** | ***Repo***|
|-----|----|
| [![PyPI version](https://badge.fury.io/py/geobr.svg)](https://badge.fury.io/py/geobr) <br />  [![Downloads](https://static.pepy.tech/badge/geobr)](https://pepy.tech/project/geobr) <br />  [![Downloads](https://static.pepy.tech/badge/geobr/month)](https://pepy.tech/project/geobr)  <br /> [![Lifecycle: maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg)](https://www.tidyverse.org/lifecycle/#maturing) <br /> [![Python build status](https://github.com/ipeaGIT/geobr/workflows/Python-CMD-check/badge.svg)](https://github.com/ipeaGIT/geobr/actions) |<img alt="GitHub stars" src="https://img.shields.io/github/stars/ipeaGIT/geobr.svg?color=orange"> <br /> <br />  [![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) |

## Installation Python
```bash
pip install medbr
```
*Windows users:*  

```bash
conda create -n geo_env
conda activate geo_env  
conda config --env --add channels conda-forge  
conda config --env --set channel_priority strict  
conda install python=3 geopandas
conda install python=3 folium  
pip install medbr
```
# Basic Usage

The syntax of all `medbr` functions operates on the same logic, making it intuitive to generate views. See some examples [here](https: ).

# Functions

|Function|Group|Description|Source|
|-----|-----|-----|-----|
|`medbr.facilities(cidade, type)`| Health Infrastructure | National Registry of Health Establishments (CNES). You can parameterize the city (default: Brazil) and the type of establishment (default: all) | CNES |
|`medbr.beds(state)`| Health Infrastructure | Plots the locations with hospital beds (2023) and their quantities. You can parameterize the state (default: Brazil) | Open Data Portal |
|`medbr.heatmap.covid(city, date initial, date final)`| COVID | Plot the heat map for the COVID vaccination campaign. Being able to parameterize the city (default: Brazil) and the time interval (default: the entire base) | Open Data Portal |
|`medbr.heatmap.vaccine.covid(city, date initial, date final, brand)`| COVID | Plot the heat map for the COVID vaccination campaign. Being able to parameterize the vaccine brand, the city (default: Brazil) and the time interval (default: the entire base) | Open Data Portal |
|`medbr.heatmap.vaccine.fm(city, date initial, date final, sex)`| COVID | Plot the heat map for the COVID vaccination campaign. Being able to parameterize the gender (female or male), the city (default: Brazil) and the time interval (default: the entire base) | Open Data Portal |
|`medbr.mortality(state, date initial, date final)`| Population Health | Plots the intensity map by city for the mortality rate. Being able to parameterize the state (default: Brazil) and the time interval (default: the entire base) | Open Data Portal |
|`medbr.birth(state, date initial, date final)`| Population Health | Plot the intensity map by city for the birth rate. Being able to parameterize the state (default: Brazil) and the time interval (default: the entire base) | Open Data Portal |
|`medbr.sanitation(state, illness)`| Population Health | Plots the intensity map by city for the National Basic Sanitation Survey (PNSB). Being able to parameterize the state (default: Brazil) and the type of disease affected (default: all) | Open Data Portal |
|`medbr.plancoverage(state, provider)`| Complementary Health | Plots the cities where the providers have coverage. Parameterize the state (default: Brazil) and the provider (default: all) | Open Data Portal |
|`medbr.beneficiaries(state, provider)`| Complementary Health | Plot the intensity map by city according to the concentration of beneficiaries. Parameterize the state (default: Brazil) and the provider (default: all) | Open Data Portal |

# Contributing to medbr
If you would like to contribute to medbr and add new functions or data sets, please check this [guide](https://) to propose your contribution.

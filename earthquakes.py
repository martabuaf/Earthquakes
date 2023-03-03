## Librerías

import numpy as np
import pandas as pd

import requests

import json
from pprint import pprint

import datetime
from time import sleep

import plotly.graph_objects as go

import io
import PIL
import gif

## Llamada a la API

endpoint = f"https://earthquake.usgs.gov/fdsnws/event/1/"

start, end = "2022-01-01" , "2023-01-01"

params = {"method"       : "query",
          "eventtype"    : "earthquake",
          "kmlcolorby"   : "depth",
          "format"       : "geojson",
          "starttime"    : start, 
          "endtime"      : end,
          "minmagnitude" : 4.0,
          "updatedafter" : None,
          "limit"        : "10000"}

#endpoint = f"https://earthquake.usgs.gov/fdsnws/event/1/[{method}[?{params}]]"

response = requests.get(url = endpoint, params = params)

data = response.json()

# Creo el DataFrame

df_eq = pd.DataFrame()

df_eq["Type"] = [item["properties"]['type'] for item in data["features"]]

df_eq["Magnitude"] = [item["properties"]['mag'] for item in data["features"]]

df_eq["Place"] = [item["properties"]['place'] for item in data["features"]]

df_eq["Time"] = [datetime.datetime.fromtimestamp(item["properties"]['time']/1000) for item in data["features"]]

df_eq["Updated"] = [datetime.datetime.fromtimestamp(item["properties"]['updated']/1000) for item in data["features"]]

df_eq["Ids"] = [item['id'] for item in data["features"]]

df_eq["Coords"] = [item['geometry']['coordinates'] for item in data["features"]]

df_eq["Felt"] = [item["properties"]['felt'] for item in data["features"]]

df_eq["CDI"] = [item["properties"]['cdi'] for item in data["features"]]

df_eq["MMI"] = [item["properties"]['mmi'] for item in data["features"]]

df_eq["Alert"] = [item["properties"]['alert'] for item in data["features"]]

df_eq["Tsunami"] = [item["properties"]['tsunami'] for item in data["features"]]

df_eq["sig"] = [item["properties"]['sig'] for item in data["features"]]

df_eq["rms"] = [item["properties"]['rms'] for item in data["features"]]

# Normalizo la columna de Magnitud

a, b = 10, 20

x, y = df_eq.Magnitude.min(), df_eq.Magnitude.max()

df_eq['Size'] = (df_eq.Magnitude - x) / (y - x) * (b - a) + a

# Elimino los datos de Magnitud que faltan y visualizo el gráfico

df_eq.dropna(subset = "Magnitude", inplace = True)

df_eq.to_csv("earthquakes_data.csv", index = False)

## Creo el gráfico

df_eq = pd.read_csv("earthquakes_data.csv")

latitude = [coord[1:-1].split(", ")[1] for coord in df_eq["Coords"]]

longitude = [coord[1:-1].split(", ")[0] for coord in df_eq["Coords"]]

marker = dict(size = df_eq["Size"],
              opacity = 0.5,
              reversescale = True,
              autocolorscale = False,
              symbol = 'circle',
              line = None,
              colorscale = "hot",
              cmin = df_eq.Magnitude.min(),
              color = df_eq["Magnitude"],
              cmax = df_eq.Magnitude.max(),
              colorbar_title = "Magnitude")

fig = go.Figure(go.Scattergeo(lat = latitude , lon = longitude, marker = marker))

fig.update_geos(projection_type="orthographic", resolution=50,
                showcoastlines=True, coastlinecolor="grey",
                showland=True, landcolor="lightgrey",
                showocean=True, oceancolor="lightsteelblue",
                showlakes=False, lakecolor="steelblue",
                showrivers=False, rivercolor="steelblue")
    
fig.update_layout(title = 'Registered earthquakes in 2020', height = 600, margin = {"r":0,"t":0,"l":0,"b":0})

fig.write_html("terremotos_global.html")

# Creo el GIF

frames = list()

for i in range(-180, 180, 4):
    
    fig.update_geos(projection_rotation_lon = i, projection_scale = 0.8)
    
    frames.append(PIL.Image.open(io.BytesIO(fig.to_image(format="png"))))
    
gif.options.matplotlib["dpi"] = 300

gif.save(frames, "earthquakes_global.gif", duration = 100)

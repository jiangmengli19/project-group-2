from bokeh.plotting import show, output_file, output_notebook
from shapely.geometry import Polygon
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper, LinearColorMapper
from bokeh.palettes import Reds 
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure, save
from bokeh.resources import CDN
from bokeh.models.widgets import Tabs, Panel


### Make interactive map to show density of confirmed cases in US

# Example: use the date set of 12-04-2020
# Note the data set is cumulative
df2 = pd.read_csv("files/12-04-2020.csv")
gdf = gpd.GeoDataFrame(df2, geometry=gpd.points_from_xy(df2.Long_, df2.Lat))
df4 = gpd.read_file("files/s_11au16.shp")

listName = df4["NAME"].tolist()
glist = gdf.Province_State.tolist()
gdff = gdf.copy()
for i in glist:
    if i not in listName:
        k = gdf[gdf["Province_State"]==i].index
        gdff = gdff.drop(k)

gdff = gdff.reset_index(drop=True)
gdffcopy = gdff.drop("geometry",axis=1).copy()
listgeometry = []

for i in range(len(gdffcopy)):
    s = gdffcopy.iloc[i].Province_State
    #df.index.get_loc(result.iloc[0].name)
    o = df4["NAME"].to_list().index(s)
    listgeometry.append(df4.iat[o,-1])

gdffcopy['geometry'] = pd.Series(listgeometry)


# compile data set and the shape file
gdffcopy.crs = df4.crs
gdffcopysourcesecond = GeoJSONDataSource(geojson=gdffcopy.to_json())

# Set the color palette 
color_mapper = LinearColorMapper(palette=Reds[3], low=max(df2.loc[:,'Confirmed']),
                                high=min(df2.loc[:,'Confirmed']))

# Add tools 
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

# US Choropleth Map for Covid-19 based on cumulative confirmed cases up to 12/04/2020
p = figure(title="Cumulative Confirmed Cases of US 12/04/2020", tools=TOOLS, 
           x_axis_location=None, y_axis_location=None, width=1600, height=600)

p.patches('xs', 'ys', fill_alpha=0.7, fill_color={'field': 'Confirmed', 'transform': color_mapper},
          line_color='white', line_width=0.5, source=gdffcopysourcesecond)

# Add hover tooltips
hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"

hover.tooltips = [("State", "@Province_State"),
                  ("Confirmed","@Confirmed"),
                  ("Recovered","@Recovered"),
                  ("Death","@Deaths")]

p.add_tools(hover)

show(p)


output_file("12-04-USA.html")





from bokeh.plotting import figure, output_file, show
from pathlib import Path
import random
import pandas as pd

import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Dropdown
from bokeh.layouts import column
from bokeh.io import curdoc


# count = 10
# x = range(count)
# y = random.sample(range(0, 101), count)

# p = figure()    # figure is a type of plot

# # using various glyph methods to create scatter
# # plots of different marker shapes
# p.circle  (x, y, size=30, color='red', legend_label='circle')
# p.line    (x, y, width=2, color='blue', legend_label='line')
# p.triangle(x, y, size=10, color='gold', legend_label='triangle')

# output_file('my_first_graph.html')    # name the output file

# show(p)    #show the graph

# class Endpoints:
#     available_seasons = ['2022', '2021', '2020', '2019S']
#     seasons = 'seasons'
#     constructors = 'constructors'
#     drivers = 'drivers'
#     races = 'races'

# class Datasets:
#     seasons = 'seasons'
#     constructors = 'constructors'
#     drivers = 'drivers'
#     races = 'races'
#     circuits = 'circuits'
#     laptimes = 'laptimes'

from data import data

cs = {}
for constructor in data.constructorRef.unique():
    total = data.loc[(data.constructorRef == constructor)]
    lst = []
    for y in total.year.unique():
        sum = total[total.year == y].points.sum()
        num_races = total[total.year == y].size
        lst.append([y, sum])
    if len(lst) < 4:
        continue
    df = pd.DataFrame(data=lst, columns=['Year', 'Total Points'])
    print(df)
    cs[constructor.capitalize()] = df

    
#   df.plot.scatter(x='year', y='total points', title=, sharex=True, xlim=(2011, 2020), ylim=(0, 1000), s=100, c='blue', figsize=(12, 7), xlabel='Year', ylabel='Total Points')

# create the data source
first_cs = list(cs.keys())[0]

df = cs[first_cs]

print(df)

source = ColumnDataSource(df)

# display a Dropdown menu
menu = Dropdown(label="Constructor", menu=[(c, c) for c in cs.keys()])

# callback when the Dropdown menu is selected

def update_plot(event):
    df = cs[event.item]
    p.title.text = f'{event.item}'
    source.data = df


menu.on_click(update_plot)

# called when the Select item changes in valu
# update the date source


p = figure(width=1500)
p.line("Year", "Total Points", source=source, color='green', width=3)
p.title.text = f'{first_cs} Stock Prices'
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Total Points'

curdoc().theme = 'night_sky'
curdoc().title = "Intro"
curdoc().add_root(column(menu, p))



# plt.rc('font', size=10)          # controls default text sizes
# plt.rc('axes', titlesize=15)     # fontsize of the axes title
# plt.rc('axes', labelsize=15)     # fontsize of the x and y labels
# plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
# plt.rc('legend', fontsize=15)    # legend fontsize
# plt.rc('figure', titlesize=15)   # fontsize of the figure title
# for constructor in r.constructorRef.unique():
#   total = r.loc[(r.constructorRef == constructor)]
#   lst = []
#   for y in total.year.unique():
#     sum = total[total.year == y].points.sum()
#     num_races = total[total.year == y].size
#     lst.append([y, sum])
#   df = pd.DataFrame(data=lst, columns=['year', 'total points'])
#   df.plot.scatter(x='year', y='total points', title=constructor.capitalize(), sharex=True, xlim=(2011, 2020), ylim=(0, 1000), s=100, c='blue', figsize=(12, 7), xlabel='Year', ylabel='Total Points')















# import pandas as pd
# import fastf1 as ff1
# from fastf1 import plotting
# from matplotlib import pyplot as plt
# from matplotlib.pyplot import figure
# from matplotlib.collections import LineCollection
# from matplotlib import cm
# import numpy as np
# import pandas as pd
# # Setup plotting
# plotting.setup_mpl()

# # Enable the cache
# ff1.Cache.enable_cache('../cache') 

# # Get rid of some pandas warnings that are not relevant for us at the moment
# pd.options.mode.chained_assignment = None

# # Load the session data
# race = ff1.get_session(2021, 'Russia', 'R')

# # Get the laps
# laps = race.load_laps(with_telemetry=True)


























# # Calculate RaceLapNumber (LapNumber minus 1 since the warmup lap is included in LapNumber)
# laps['RaceLapNumber'] = laps['LapNumber'] - 1

# # Starting from lap 45 it started raining
# laps = laps.loc[laps['RaceLapNumber'] >= 45]


# # Get all drivers
# drivers = pd.unique(laps['Driver'])

# telemetry = pd.DataFrame()

# # Telemetry can only be retrieved driver-by-driver
# for driver in drivers:
#     driver_laps = laps.pick_driver(driver)
    
#     # Since we want to compare distances, we need to collect telemetry lap-by-lap to reset the distance
#     for lap in driver_laps.iterlaps():
#         driver_telemetry = lap[1].get_telemetry().add_distance()
#         driver_telemetry['Driver'] = driver
#         driver_telemetry['Lap'] = lap[1]['RaceLapNumber']
#         driver_telemetry['Compound'] = lap[1]['Compound']
    
#         telemetry = telemetry.append(driver_telemetry)



# # Only keep required columns
# telemetry = telemetry[['Lap', 'Distance', 'Compound', 'Speed', 'X','Y']]

# # Everything that's not intermediate will be "slick"
# telemetry['Compound'].loc[telemetry['Compound'] != 'INTERMEDIATE'] = 'SLICK'


# # We want 25 mini-sectors
# num_minisectors = 25

# # What is the total distance of a lap?
# total_distance = max(telemetry['Distance'])

# # Generate equally sized mini-sectors 
# minisector_length = total_distance / num_minisectors

# minisectors = [0]

# for i in range(0, (num_minisectors - 1)):
#     minisectors.append(minisector_length * (i + 1))



# # Assign minisector to every row in the telemetry data
# telemetry['Minisector'] =  telemetry['Distance'].apply(
#   lambda z: (
#     minisectors.index(
#       min(minisectors, key=lambda x: abs(x-z)))+1
#   )
# )

# average_speed = telemetry.groupby(['Lap', 'Minisector', 'Compound'])['Speed'].mean().reset_index()

# # Select the compound with the highest average speed
# fastest_compounds = average_speed.loc[average_speed.groupby(['Lap', 'Minisector'])['Speed'].idxmax()]

# # Get rid of the speed column and rename the Compound column
# fastest_compounds = fastest_compounds[['Lap', 'Minisector', 'Compound']].rename(columns={'Compound': 'Fastest_compound'})

# # Join the fastest compound per minisector with the full telemetry
# telemetry = telemetry.merge(fastest_compounds, on=['Lap', 'Minisector'])

# # Order the data by distance to make matploblib does not get confused
# telemetry = telemetry.sort_values(by=['Distance'])

# # Assign integer value to the compound because that's what matplotlib wants
# telemetry.loc[telemetry['Fastest_compound'] == "INTERMEDIATE", 'Fastest_compound_int'] = 1
# telemetry.loc[telemetry['Fastest_compound'] == "SLICK", 'Fastest_compound_int'] = 2


# def generate_minisector_plot(lap, save=False, details=True):
#     single_lap = telemetry.loc[telemetry['Lap'] == lap]

#     x = np.array(single_lap['X'].values)
#     y = np.array(single_lap['Y'].values)

#     points = np.array([x, y]).T.reshape(-1, 1, 2)
#     segments = np.concatenate([points[:-1], points[1:]], axis=1)
#     compound = single_lap['Fastest_compound_int'].to_numpy().astype(float)

#     cmap = cm.get_cmap('ocean', 2)
#     lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
#     lc_comp.set_array(compound)
#     lc_comp.set_linewidth(2)

#     plt.rcParams['figure.figsize'] = [12, 5]
    
#     if details:
#         title = plt.suptitle(
#             f"2021 Russian GP \n Lap {lap} - Slicks vs. Inters"
#         )
        
#     plt.gca().add_collection(lc_comp)
#     plt.axis('equal')
#     plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
    
#     if details:
#         cbar = plt.colorbar(mappable=lc_comp, boundaries=np.arange(1, 4))
#         cbar.set_ticks(np.arange(1.5, 9.5))
#         cbar.set_ticklabels(['Inters', 'Slicks'])
    
#     if save:
#         plt.savefig(f"img/minisectors_lap_{lap}.png", dpi=300)

#     plt.show()

    
# generate_minisector_plot(46, save=True, details=False)



# import json
# from bokeh.models import GeoJSONDataSource 
# from bokeh.plotting import figure, curdoc
# from bokeh.layouts import column
 
 
# # Read the country borders shapefile into python using Geopandas 
# shapefile = 'data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
# gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

# # Rename the columns
# gdf.columns = ['country', 'country_code', 'geometry']
 

# # Convert the GeoDataFrame to GeoJSON format so it can be read by Bokeh
# merged_json = json.loads(gdf.to_json())
# json_data = json.dumps(merged_json)
# geosource = GeoJSONDataSource(geojson=json_data)


# # Make the plot
# TOOLTIPS = [
# ('UN country', '@country')
# ]

# p = figure(title='World Map', plot_height=600 , plot_width=950, tooltips=TOOLTIPS,
# x_axis_label='Longitude', y_axis_label='Latitude')

# p.patches('xs','ys', source=geosource, fill_color='white', line_color='black',
# hover_fill_color='lightblue', hover_line_color='black')
 
# # This final command is required to launch the plot in the browser
# curdoc().add_root(column(p))

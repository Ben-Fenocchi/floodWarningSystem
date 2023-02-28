from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#get list of stations
#run stations through stations_highest_rel_level for x stations
#for each of these stations check the station's relative level,
#check relative level against criteria, putting each town that station belongs to in the relative list.

def run():
    stations = build_station_list()
    update_water_levels(stations)
    #only run data for top 50 stations as these are the most at risk, there are too many to run all stations
    necessaryStations = stations_highest_rel_level(stations,50)
    Risk_severe = []
    Risk_high = []
    Risk_moderate = []
    Risk_low = []
    towns = []
    for station in necessaryStations:
        print(station[0].town,station[1])
        if station[0].town not in towns:
            towns.append(station[0].town)
        dates,levels = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=1))
        x = matplotlib.dates.date2num(dates) # dates as floats
        y = levels
        gradient = np.polyfit(x, y, 1) 
        gradient = gradient[0]
        if station[0].town not in Risk_severe:
            if station[1] > 1.1:
                Risk_severe.append(station[0].town)
            elif station[1] > 1:
                if station[0].town not in Risk_severe: 
                    if gradient > 0.1:
                        Risk_severe.append(station[0].town)
                    elif station[0].town not in Risk_high:
                        Risk_high.append(station[0].town)
            elif station[1] > 0.9:
                if station[0].town not in Risk_high:
                    if gradient > 0.1:
                        Risk_high.append(station[0].town)
                    elif station[0].town not in Risk_moderate:
                        Risk_moderate.append(station[0].town)
            else:
                if station[0].town not in Risk_moderate: 
                    if gradient > 0.1:
                        if station[1] >0.7:
                            Risk_moderate.append(station[0].town)
                        elif station[0].town not in Risk_low:
                            Risk_low.append(station[0].town)
                    elif station[0].town not in Risk_low:
                        Risk_low.append(station[0].town)
    for item in Risk_low:
        if item in Risk_moderate: Risk_low.remove(item)
        if item in Risk_high: Risk_low.remove(item)    
        if item in Risk_severe: Risk_low.remove(item)  
    for item in Risk_moderate:
        if item in Risk_high: Risk_moderate.remove(item)    
        if item in Risk_severe: Risk_moderate.remove(item)  
    for item in Risk_high:  
        if item in Risk_severe: Risk_high.remove(item)  
    print("severe: ", Risk_severe)
    print("high: ", Risk_high)
    print("moderate: ", Risk_moderate)
    print("low: ", Risk_low)
if __name__ == "__main__":
    print("*** Task 2G***")
    run()
    
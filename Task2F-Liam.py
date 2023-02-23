from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit 
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    necessaryStations = stations_highest_rel_level(stations,5)
    necessaryStations = necessaryStations[:5]
    #takes the highest 5 stations

    for data in necessaryStations:
        dates,levels = fetch_measure_levels(data[0].measure_id, datetime.timedelta(days=2))
        plot_water_level_with_fit(data[0], dates, levels, 4)



if __name__ == "__main__":
    print("*** Task 2F ***")
    run()
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import datetime

def run():
    stations = build_station_list()
    necessaryStations = stations_highest_rel_level(stations,5)
    necessaryStations = necessaryStations[:5]
    #takes the highest 5 stations

    for station in necessaryStations:
        dates,levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=10))
        plot_water_levels(station,dates,levels)


if __name__ == "__main__":
    print("*** Task 2E ***")
    run()

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list
    update_water_levels(stations)
    tol = 0.8
    highRiskStations = stations_level_over_threshold(stations,tol)
    for data in highRiskStations:
        print(data[0].name,data[1])

'''
I think there is a problem in update water levels function, line 81 where it says for station in stations
Apparently something is wrong with this but I have no idea what
'''

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
from floodsystem.stationdata import build_station_list
from floodsystem.flood import  stations_highest_rel_level
from floodsystem.stationdata import update_water_levels





def run():
    stations = build_station_list()
    update_water_levels(stations)
    greatestTenLevels = stations_highest_rel_level(stations,10)
    for x in greatestTenLevels:
        print(x[0].name, x[1] )




if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
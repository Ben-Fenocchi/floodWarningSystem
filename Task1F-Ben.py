from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""
    """
    build a list of all stations with inconsistent typical range data. Print a list of station 
    names, in alphabetical order, for stations with inconsistent data.
    """
    stations = build_station_list()
    inconsistencies = inconsistent_typical_range_stations(stations)
    stationNames = []
    for x in inconsistencies:
        stationNames.append(x.name)
    stationNames.sort()
    print(stationNames)




if __name__ == "__main__":
    print("*** Task 1F: CUED Part IB Flood Warning System ***")
    run()
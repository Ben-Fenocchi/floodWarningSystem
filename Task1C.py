from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key


def run():
    print("task 1C start")
    camCityCentre = (52.2053, 0.1218)
    radius = 10
    stations = build_station_list()
    stations_list = []
    StationsWithinRadius = stations_within_radius(stations,camCityCentre, radius)
    for Stations in StationsWithinRadius:
        stations_list.append(Stations.name)
    stations_list.sort()
    print(stations_list)
    print("task 1C End")
  
  
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IC Flood Warning System ***")
    run()

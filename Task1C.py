from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    print("task 1C start")
    camCityCentre = (52.2053, 0.1218)
    radius = 10
    stations = build_station_list()
    StationsWithinRadius = stations_within_radius(stations,camCityCentre, radius)
    StationsWithinRadius.sort()
    for Stations in StationsWithinRadius:
        print(Stations)
        print("task 1C End")
  
  
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IC Flood Warning System ***")
    run()

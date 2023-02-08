from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
  #Provide a program file Task1C.py that uses the function geo.stations_within_radius to build a list of stations
  #within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). Print the names of the stations,
  #listed in alphabetical order. Representative output:
  camCityCentre = (52.2053, 0.1218)
  radius = 10
  stations = build_station_list()
  StationsWithinRadius = stations_within_radius(stations,camCityCentre, radius)
  StationsWithinRadius.sort
  for Stations in StationsWithinRadius:
    print(Stations)
  
  
  
  
  
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IC Flood Warning System ***")
    run()

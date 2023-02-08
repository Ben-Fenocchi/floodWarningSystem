from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation


def run():
    """Requirements for Task 1B"""
    """
    prints a list of tuples (station name, town, distance)
    for the 10 closest and the 10 furthest stations from the Cambridge city centre
    """

    camCityCentre = (52.2053, 0.1218)
    stations = build_station_list() # collects list of stations
    stationsByDistance = stations_by_distance(stations,camCityCentre)  #returns list of stations and their distances

    closestStations = []
    furthestStations = []
    closest = stationsByDistance[:10]
    furthest = stationsByDistance[-10:]
    #print(closest)
    #print(furthest)
    
    for item in closest:
        currentTuple = tuple((item[0].name, item[0].town, item[1]))
        closestStations.append(currentTuple)        

    furthest = stationsByDistance[-10:]
    for item in furthest:
        currentTuple = tuple((item[0].name, item[0].town, item[1]))
        furthestStations.append(currentTuple)


    print(closestStations)
    print(furthestStations)
    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IB Flood Warning System ***")
    run()
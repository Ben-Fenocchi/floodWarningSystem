from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river



def run():
    """Requirements for Task 1D"""
    """
    Uses geo.rivers_with_station to print how many rivers have at least one monitoring station (Representative result: 843) 
    and prints the first 10 of these rivers in alphabetical order. 

    Uses geo.stations_by_river to print the names of the stations 
    located on the following rivers in alphabetical order
    """
    stations = build_station_list()

    riverStations = rivers_with_station(stations)
    riverStations.sort()#sorts to alphabetical so i dont have to later
    counter = 0
    riversWithMoreThanOneStation = []

    for river in riverStations:#goes through all the rivers with stations
        for station in stations:#looks for all the stations on this river
            if station.river == river:
                counter+=1#if the station is on the river then add to a counter
        if counter >1 :#if there is more than one station on the river
            riversWithMoreThanOneStation.append(river)#add it to the list
        counter = 0#reset for the next list

    print(len(riversWithMoreThanOneStation),"rivers with multiple stations")
    print("The first ten are",riversWithMoreThanOneStation[:10])



    riverStationDict = stations_by_river(stations)
    list = []
    for x in riverStationDict["River Aire"]:
        list.append(x.name)
        list.sort()
    print(list)
    list = []
    for x in riverStationDict["River Cam"]:
        list.append(x.name)
        list.sort()
    print(list)
    list = []
    for x in riverStationDict["River Thames"]:
        list.append(x.name)
        list.sort()
    print(list)





    


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IB Flood Warning System ***")
    run()
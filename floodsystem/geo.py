# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def rivers_with_station(stations):
    rivers = []
    for station in stations:
        river = station.river
        if not river in rivers:
            rivers.append(river)
    return(rivers)#returns a list of the rivers that have stations with no duplicates

def stations_by_river(stations):
    riverNames = rivers_with_station(stations)#retrieves a list of the rivers with stations
    riverDict = {}
    stationsOnRiver = []
    for river in riverNames:#goes through all the rivers
        for station in stations:#looks for all stations on this river
            if station.river == river:#if it finds a station on the river
                stationsOnRiver.append(station)#adds it to a list of stations for this river
        riverDict[river] = stationsOnRiver#adds it to the dictionary
        stationsOnRiver = []#resets the list for the next river
    return(riverDict)



def stations_by_distance(stations, p):
    """
    takes list of station objects and a co-ordinate p as an input
    then returns a list of tuples (station,distance)
    """
    stationsByDistanceList = []
    for station in stations:
        distance = haversine(station.coord,p)#inputs to this are lat and long tuples for each place
        data = [station,distance]
        stationsByDistanceList.append(data)

    return sorted_by_key(stationsByDistanceList,-1)#list of lists to sort, index of sublist sorting by, -1 puts to the end which is where my distance haversine is


def stations_within_radius(stations, centre, r):

     StationsWithinRadius = []
     for station in stations:
         distance = haversine(station.coord, centre)
         if distance <= r:
              StationsWithinRadius.append(station)
     return StationsWithinRadius

def rivers_by_station_number(stations, N):

   riverNames = rivers_with_station(stations)
   riverList = []
   for river in riverNames:
      count = 0
      for station in stations:
          if station.river == river:
             count = count + 1
      data = [river, count]
      riverList.append(data)
   riverList = sorted_by_key(riverList,-1,True)
   final_value = riverList[N-1][-1]
   print(final_value)
   count = N
   while riverList[count][-1] == final_value:
       count = count + 1
   riverList = riverList[0:count]
   return riverList

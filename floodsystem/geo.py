# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

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
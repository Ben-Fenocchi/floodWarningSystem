def stations_level_over_threshold(stations, tol):
    highRiskList = []
    for station in stations:
        relativeLevel = station.relative_water_level()

        if relativeLevel is None:
            pass
        elif relativeLevel> tol:
            thisTuple = (station,relativeLevel)
            highRiskList.append(thisTuple)        
    highRiskList.sort(key=lambda tup: tup[1], reverse=True)#sorts in reverse order by second element in the subset
    return highRiskList

def stations_highest_rel_level(stations, N):
    highRiskList = stations_level_over_threshold(stations,0)#setting tol to zero so get a list of pretty much all stations and their relative levels
    highestRelStations = highRiskList[:N]
    #this list is automatically sorted in descending relative level order from the way the stations_level_over_threshold is built
    return(highestRelStations)
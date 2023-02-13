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

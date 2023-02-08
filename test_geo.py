from floodsystem.geo import rivers_with_station, stations_by_river, stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation


testStation1 = MonitoringStation("test ID","test m-ID","CamStation",(1,1),(0,0),"river Cam","Cambridge")
testStation2 = MonitoringStation("test ID","test m-ID","OxfStation",(1,1),(0,0),"river Ox","Oxford")
testStation3 = MonitoringStation("test ID","test m-ID","LonStation",(1,1),(0,0),"river Thames","London")
testStation4 = MonitoringStation("test ID","test m-ID","LonStation2",(1,1),(0,0),"river Thames","London")


def test_rivers_with_station():#the rivers with stations function should filter out the second london station
    stationList = (testStation1,testStation2,testStation3,testStation4)
    result = rivers_with_station(stationList)
    assert result == ("river Cam", "river Ox", "river Thames")



from floodsystem.geo import rivers_with_station, stations_by_river, stations_by_distance, stations_within_radius, rivers_by_station_number
from floodsystem.station import MonitoringStation
#from haversine import haversine, Unit
print("test")

testStation1 = MonitoringStation("test ID","test m-ID","CamStation",(1,1),(0,0),"river Cam","Cambridge")
testStation2 = MonitoringStation("test ID","test m-ID","OxfStation",(1,2),(0,0),"river Ox","Oxford")
testStation3 = MonitoringStation("test ID","test m-ID","LonStation",(1,2),(0,0),"river Thames","London")
testStation4 = MonitoringStation("test ID","test m-ID","LonStation2",(1,2),(0,0),"river Thames","London")



def test_rivers_with_station():#the rivers with stations function should filter out the second london station
    stationList = (testStation1,testStation2,testStation3,testStation4)
    result = rivers_with_station(stationList)
    assert result == ["river Cam","river Ox","river Thames"]

def test_stations_by_river():
    stationList = (testStation1,testStation2,testStation3)
    result = stations_by_river(stationList)
    assert type(result) is dict

def test_stations_by_distance():
    result = stations_by_distance((testStation1,testStation2),(0,0))
    assert result == [[testStation1,157.2495984740402],[testStation2,248.62965826824876]]


def test_stations_within_radius():
    stationList = (testStation1,testStation2,testStation3)
    result = stations_within_radius(stationList,(0,0),157.3)
    assert result == [testStation1]
    
def test_rivers_by_station_number():
    stationList = (testStation1,testStation2,testStation3,testStation4)
    number_rivers = 1
    result = rivers_by_station_number(stationList, number_rivers)
    assert result == [('river Thames', 2)]
    


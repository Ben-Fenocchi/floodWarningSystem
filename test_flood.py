from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

testStation1 = MonitoringStation("test ID","test m-ID","CamStation",(1,1),(0,1.0),"river Cam","Cambridge")
testStation2 = MonitoringStation("test ID","test m-ID","OxfStation",(1,2),(0,1.0),"river Ox","Oxford")
testStation3 = MonitoringStation("test ID","test m-ID","LonStation",(1,2),(0,1.0),"river Thames","London")
testStation4 = MonitoringStation("test ID","test m-ID","LonStation2",(1,2),(0,1.0),"river Thames","London")

testStation1.latest_level = 0# this is the low range
testStation2.latest_level = 0.5 #this is the mid range
testStation3.latest_level = 0.81# this is slightly over 0.8 of high range
testStation4.latest_level = 0.8

stationList = [testStation1,testStation2,testStation3,testStation4]

def test_stations_level_over_threshold():
    highRiskStations = stations_level_over_threshold(stationList,0.79)
    print(highRiskStations)
    assert highRiskStations == [(testStation3,0.81),(testStation4,0.8)]

def test_stations_highest_rel_level():
    highRiskFour = stations_highest_rel_level(stationList,4)
    assert len(highRiskFour) == 4#checks returns the top 4 as it should
    assert highRiskFour[0][1] > highRiskFour[1][1]#checks sorted in descending order


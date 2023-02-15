from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation

testStation4 = MonitoringStation("test ID","test m-ID","LonStation2",(1,2),(0,1.0),"river Thames","London")
dates = [12,13,14,15,16,17]
levels = [1.0,1.29,1.3,2.7,2.45,4.56]

def test_plot_water_levels():
    result = plot_water_levels(testStation4,dates,levels)
    #This test checks that the function will accept the expected datatypes, as otherwise an error will
    #be thrown up causing the test to fail
    
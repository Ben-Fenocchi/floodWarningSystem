from floodsystem.analysis import polyfit
from floodsystem.station import MonitoringStation

dates = [12,13,14,15,16,17]
levels = [1.0,1.29,1.3,2.7,2.45,4.56]
p=4

def test_polyfit():
    item1,item2 = polyfit(dates,levels,p)
    assert item2 == 1.3888888888888888e-10
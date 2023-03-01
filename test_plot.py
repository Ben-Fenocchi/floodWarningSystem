from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import pytest

testStation4 = MonitoringStation("test ID","test m-ID","LonStation2",(1,2),(0,1.0),"river Thames","London")
dates = [12,13,14,15,16,17]
levels = [1.0,1.29,1.3,2.7,2.45,4.56]

def test_plot_water_levels():
    with pytest.raises(TypeError):
        plot_water_levels(testStation4,"dates",levels)
        
    

p = 2
def test_plot_water_level_with_fit():
    with pytest.raises(TypeError):
        plot_water_level_with_fit(testStation4,"dates",levels,p)

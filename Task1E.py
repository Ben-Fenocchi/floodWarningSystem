from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.utils import sorted_by_key

def run():
    number = 9
    stations = build_station_list()
    print(rivers_by_station_number(stations, number))
    
    
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

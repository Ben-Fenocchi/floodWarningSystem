# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


inconsistentStation1= MonitoringStation("test ID","test m-ID","CamStation",(1,1),None,"river Cam","Cambridge")
inconsistentStation2=  MonitoringStation("test ID","test m-ID","OxStation",(1,1),(1,0),"river Ox","Oxford")
consistentStation =  MonitoringStation("test ID","test m-ID","LonStation",(1,1),(0,0),"river Thames","London")

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    stationList = (inconsistentStation1,inconsistentStation2,consistentStation)
    result = inconsistent_typical_range_stations(stationList)
    assert result == [inconsistentStation1,inconsistentStation2]
    assert type(result) is list 

def test_relative_water_level():
    testStation=  MonitoringStation("test ID","test m-ID","OxStation",(1,1),(0,1),"river Ox","Oxford")
    testStation.latest_level = 0.5
    result = testStation.relative_water_level()
    assert result == 0.5

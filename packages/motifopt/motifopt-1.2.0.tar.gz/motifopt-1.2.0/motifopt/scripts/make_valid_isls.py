# The MIT License (MIT)
#
# Copyright (c) 2019 Debopam Bhattacherjee
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import ephem
import math
import sys
import util
# Generate a satellite from orbital elements
# Check parent script 02_get_sat_positions_at_time.sh for the arguments supplied
def read_sat_positions(sat_pos_file):
    """
    Reads satellite positions from input file
    :param sat_pos_file: input file containing satellite positions at a particular instant of time
    """
    global G
    global sat_positions
    global orb_0_sat_positions
    sat_positions = {}
    orb_0_sat_positions = {}
    cnt = 0
    lines = [line.rstrip('\n') for line in open(sat_pos_file)]
    for i in range(len(lines)):
        val = lines[i].split(",")
        sat_positions[int(val[0])] = {
            "orb_id": int(val[1]),
            "orb_sat_id": int(val[2]),
            "lat_deg": float(val[3]),
            "lat_rad": math.radians(float(val[3])),
            "long_deg": float(val[4]),
            "long_rad": math.radians(float(val[4])),
            "alt_km": float(val[5])
        }
        ####NUM_SATS_PER_ORBIT 20
        if cnt < 20 / 4 and int(val[1]) == 0:  # we need first quadrant of satellites
            orb_0_sat_positions[int(val[0])] = {
                "orb_id": int(val[1]),
                "orb_sat_id": int(val[2]),
                "lat_deg": float(val[3]),
                "lat_rad": math.radians(float(val[3])),
                "long_deg": float(val[4]),
                "long_rad": math.radians(float(val[4])),
                "alt_km": float(val[5])
            }
            cnt += 1
EARTH_RADIUS = 6371
def compute_isl_length(sat1, sat2, sat_positions):
    """
    Computes ISL length between pair of satellites. This function can also be used to compute
    city-satellite up/down-link length.
    :param sat1: Satellite 1 with position information (latitude, longitude, altitude)
    :param sat2: Satellite 2 with position information (latitude, longitude, altitude)
    :param sat_positions: Collection of satellites along with their current position data
    :return: ISl length in km
    """
    x1 = (EARTH_RADIUS + sat_positions[sat1]["alt_km"]) * math.cos(sat_positions[sat1]["lat_rad"]) * math.sin(
        sat_positions[sat1]["long_rad"])
    y1 = (EARTH_RADIUS + sat_positions[sat1]["alt_km"]) * math.sin(sat_positions[sat1]["lat_rad"])
    z1 = (EARTH_RADIUS + sat_positions[sat1]["alt_km"]) * math.cos(sat_positions[sat1]["lat_rad"]) * math.cos(
        sat_positions[sat1]["long_rad"])
    x2 = (EARTH_RADIUS + sat_positions[sat2]["alt_km"]) * math.cos(sat_positions[sat2]["lat_rad"]) * math.sin(
        sat_positions[sat2]["long_rad"])
    y2 = (EARTH_RADIUS + sat_positions[sat2]["alt_km"]) * math.sin(sat_positions[sat2]["lat_rad"])
    z2 = (EARTH_RADIUS + sat_positions[sat2]["alt_km"]) * math.cos(sat_positions[sat2]["lat_rad"]) * math.cos(
        sat_positions[sat2]["long_rad"])
    dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2) + math.pow((z2 - z1), 2))
    return dist
satPositionsFile = "../input_data/constellation_40_40_53deg/data_sat_position/sat_positions_0.txt"
read_sat_positions(satPositionsFile)

valid_isls=[]
for s1 in sat_positions:
    for s2 in sat_positions:
        d=compute_isl_length(s1, s2, sat_positions)
        if d<=5012 and s1!=s2:
            valid_isls.append([str(s1)+','+str(s2)+','+str(d)+'\n'])

with open('vISLS.txt', 'w') as f:
    for line in valid_isls:
        f.writelines(line)
f.close()


cityPositionsFile = "../input_data/data_cities/cities.txt"

def read_city_positions(city_pos_file):
    """
    eads city coordinates and population
    :param city_pos_file: file containing city coordinates and population
    :param graph: The graph to populate
    :return: collection of cities with coordinates and populations, updated graph
    """
    global city_positions
    city_positions = {}
    lines = [line.rstrip('\n') for line in open(city_pos_file)]
    for i in range(len(lines)):
        val = lines[i].split(",")
        city_positions[int(val[0])] = {
            "lat_deg": float(val[2]),
            "long_deg": float(val[3]),
            "pop": float(val[4])
        }
    return city_positions

def compute_isl_length2(c1, sat2, sat_positions,city_positions):
    """
    Computes ISL length between pair of satellites. This function can also be used to compute
    city-satellite up/down-link length.
    :param sat1: Satellite 1 with position information (latitude, longitude, altitude)
    :param sat2: Satellite 2 with position information (latitude, longitude, altitude)
    :param sat_positions: Collection of satellites along with their current position data
    :return: ISl length in km
    """
    x2 = (EARTH_RADIUS + 0 * math.cos(math.radians(city_positions[c1]["lat_deg"]))) * math.sin(math.radians(city_positions[c1]["long_deg"]))
    y2 = (EARTH_RADIUS + 0 * math.sin(math.radians(city_positions[c1]["lat_deg"])))
    z2 = EARTH_RADIUS
    x1 = (EARTH_RADIUS + sat_positions[sat2]["alt_km"]) * math.cos(sat_positions[sat2]["lat_rad"]) * math.sin(sat_positions[sat2]["long_rad"])
    y1 = (EARTH_RADIUS + sat_positions[sat2]["alt_km"]) * math.sin(sat_positions[sat2]["lat_rad"])
    z1 = (EARTH_RADIUS + sat_positions[sat2]["alt_km"]) * math.cos(sat_positions[sat2]["lat_rad"]) * math.cos(sat_positions[sat2]["long_rad"])
    dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2) + math.pow((z2 - z1), 2))
    return dist

city_positions=read_city_positions(cityPositionsFile)
valid_cities=[]
for c1,c1pos in city_positions.items():
    print(city_positions[c1])
    print(c1)
    for s1 in sat_positions:
        print(s1)
        d=compute_isl_length2(c1,s1, sat_positions,city_positions)
        if d<=5012 and s1!=s2:
            valid_cities.append([str(c1)+','+str(s1)+','+str(d)+'\n'])

with open('vCITIES.txt', 'w') as f:
    for line in valid_cities:
        f.writelines(line)
f.close()

#0,1,1080.9474877367868

#print(sat_positions[0])
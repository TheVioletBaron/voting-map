"""
Casey Edmonds-Estes
Project 4
11/13/18
"""

import sys
import csv
import math
from region import Region
from plot import Plot

def mercator(lat):
    """project latitude 'lat' according to Mercator"""
    lat_rad = (lat * math.pi) / 180
    projection = math.log(math.tan((math.pi / 4) + (lat_rad / 2)))
    return (180 * projection) / math.pi

def to_point(coords):
    """Turns a pair of latitudes and longitudes into a pair of mercatored latitudes and longitudes"""
    coord_list = []
    i = 0
    while i <= len(coords):
        try:
            temp = (float(coords[i]), mercator(float(coords[i + 1])))
        except:
            break
        i += 2
        coord_list.append(temp)
    return coord_list


def main(results, boundaries, output, width, style):
    """
    Draws an image.
    This function creates an image object, constructs Region objects by reading
    in data from csv files, and draws polygons on the image based on those Regions

    Args:
        results (str): name of a csv file of election results
        boundaries (str): name of a csv file of geographic information
        output (str): name of a file to save the image
        width (int): width of the image
        style (str): either 'GRAD' or 'SOLID' 
    """
    with open(results, 'r') as result:
        with open(boundaries, 'r') as boundary:
            bnd = csv.reader(boundary)
            res = csv.reader(result)
            bnd_list_with_blanks = [to_point(i[2:]) for i in bnd]
            lat_longs = [j for j in bnd_list_with_blanks if j != []]
            region_list = []
            res_list = [i for i in res]
            for i in range(len(res_list)):
                try:
                    region_list.append(Region(lat_longs[i], float(res_list[i][2]), float(res_list[i][3]), float(res_list[i][4])))
                except:
                    pass

            long_list = []
            lat_list = []
            for i in region_list:
                for j in i.coords:
                    long_list.append(j[1])
                    lat_list.append(j[0])
            big_plot = Plot(1024, min(long_list), min(lat_list), max(long_list), max(lat_list))
            for i in region_list:
                big_plot.draw(i, 'GRAD')
            big_plot.save(str(output))
    

if __name__ == '__main__':
    results = sys.argv[1]
    boundaries = sys.argv[2]
    output = sys.argv[3]
    width = int(sys.argv[4])
    style = sys.argv[5]
    main(results, boundaries, output, width, style)

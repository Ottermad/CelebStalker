import csv

def closest_hotel(location):
    with open('//Users/charliethomas/CelebStalker2/CelebStalker/app/hotels/Hotels.csv', 'r', encoding = "ISO-8859-1") as f:
        reader = csv.reader(f)
        first = True
        header  = None
        closest = None
        for row in reader:
            if first:
                first = False
                header = row
                continue
            if is_close(location, [row[14], row[13]]):
                closest = row
                break
    return parse_hotel(closest, header)

def is_close(location1, location2):
    lat_is_close = False
    lng_is_close = False
    location1 = [float(x) for x in location1]
    location2 = [float(x) for x in location2]
    if abs(location1[0] - location2[0]) < 0.1:
        lat_is_close = True
    if abs(location1[1] - location2[1]) < 0.1:
        lng_is_close = True
    return lat_is_close and lng_is_close


def parse_hotel(row, header):
    length = len(row)
    data = {}
    for num in range(0, length):
        x = header[num]
        y = row[num]
        data[x] = y
    return data

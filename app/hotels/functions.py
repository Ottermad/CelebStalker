import csv

def closest_hotel(location):
    with open('/Users/charliethomas/CelebStalker2/CelebStalker/app/hotels/Hotels.csv', 'r', encoding = "ISO-8859-1") as f:
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
    print("LOCATION1", location1)
    print("LOCATION2", location2)
    try:
        location1 = [float(x) for x in location1]
        location2 = [float(x) for x in location2]
        if abs(location1[0] - location2[0]) < 0.4:
            lat_is_close = True
        if abs(location1[1] - location2[1]) < 0.4:
            lng_is_close = True
    except:
        None
    return lat_is_close and lng_is_close


def parse_hotel(row, header):
    try:
        length = len(row)
        data = {}
        for num in range(0, length):
            x = header[num]
            y = row[num]
            data[x] = y
        return data
    except:
        return "Error"

def compute_l1_norm(location1, location2):
    '''Calculate the L1 norm between two points'''
    return abs(location1.x-location2.x) + abs(location1.y-location2.y)

def ride_length(ridedata, vehicle):
    '''Calculate the length of the ride from car's current location to
    destination, via the start point'''
    car_coord = vehicle.position
    ride_start = ridedata.start
    ride_end = ridedata.end
    distance = compute_l1_norm(car_coord, ride_start) + \
               compute_l1_norm(ride_start, ride_end)
    return distance

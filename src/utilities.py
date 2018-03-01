# Calculate the L1 norm between two points
def compute_l1_norm(location1, location2):
    return abs(location1.x-location2.x) + abs(location1.y-location2.y)

# Calculate the length of the ride from car's current location to destination, via the start point
def ride_length(ridedata, vehicle):
    car_coord = vehicle.position
    ride_start = ridedata.start
    ride_end = ridedata.end
    distance = compute_l1_norm(car_coord, ride_start) + compute_l1_norm(ride_start, ride_end)
    return distance
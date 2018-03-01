def compute_l1_norm(location1, location2):
    '''Calculate the L1 norm between two points'''
    return abs(location1.x-location2.x) + abs(location1.y-location2.y)

def ride_length(ride):
    '''Calculate length of ride'''
    return compute_l1_norm(ride.start, ride.end)

def get_priority(ride, t):
    '''Calculate the priorty for a ride, given the current timestep'''
    bonus = B if ride.start_time < t else 0
    return bonus + ride_length(ride)

def sort_rides_by_priority(rides, t):
    '''Given a list of rides, sort it in place'''
    priority_map = lambda r: get_priority(r, t)
    rides.sort(key=priority_map, reverse=True)


original_data = None
working_Data = None

def load_data():
    # TO DO - LOAD DATA
    pass

def cull_rides(rides, timestep):
    # Expecting to receive a list of rides. Returns rides for which the start times hasn't passed
    free_rides = []
    for ride in rides:
        if ride.start_time > timestep:
            free_rides.append(ride)
    return free_rides

def available_cars(vehicles):
    available_cars = []
    for vehicle in vehicles:
        if vehicle.status != "occupied":
            available_cars.append(vehicle)
    return available_cars

def allocate_rides_to_cars():
    pass

def update_positions():
    pass

def run_simulation():
    timestep = 0

    while True:
        # remove impossible rides (doesn't mutate input)
        cull_rides()
        # generate a list of free cars (doesn't mutate input)
        available_cars()
        # allocate the free cars
        allocate_rides_to_cars()
        # update positions
        update_positions()
        # increment timestep
        timestep+=1

if __name__ == "__main__":
    load_data()
    run_simulation()

original_data = None
working_Data = None

def load_data():
    # TO DO - LOAD DATA
    pass

def cull_rides():
    pass

def allocate_rides_to_cars():
    pass

def update_positions():
    pass

def run_simulation():
    timestep = 0

    while True:
        # remove impossible rides
        cull_rides()
        # allocate the free cars
        allocate_rides_to_cars()
        # update positions
        update_positions()
        # increment timestep
        timestep+=1

if __name__ == "__main__":
    load_data()
    run_simulation()
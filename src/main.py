from src.file_utils import read_data
original_data = None
working_data = None

def load_data(filename):
    original_data = read_data(filename)
    pass

# RAFI
def cull_rides():
    pass

# MRINANK
def allocate_rides_to_cars():
    # get assigned and unassigned cars, clear flags (set all to unassigned)
    # get sorted routes
    # for each sorted route
    # assign the nearest unassigned car for each route, update the flag
    pass

# Mrinank
def update_status():
    # if route position matches car position, busy
    pass

# Harry
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
        update_status()
        update_positions()
        # increment timestep
        timestep+=1

if __name__ == "__main__":
    load_data("data/a_example.in")
    run_simulation()
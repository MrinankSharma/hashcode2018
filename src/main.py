from src.file_utils import read_data
from src.utilities import compute_l1_norm

original_data = None
working_data = None

def load_data(filename):
    original_data = read_data(filename)
    pass

# RAFI
def cull_rides():
    pass

# MRINANK
def allocate_rides_to_cars(cars, rides, timestep):
    # get assigned and unassigned cars, clear flags (set all to unassigned)
    cars = get_available_cars(cars)
    # get sorted routes
    sorted_routes = sort_rides_by_priority(rides, timestep)
    # for each sorted route
    # assign the nearest unassigned car for each route, update the flag
    for route in sorted_routes:
        closestCar = getClosestCar(route)



def getClosestCar(route, cars):
    closestCar = None
    closest_distance = 1000
    for car in cars:
        if car.status == "unassigned":
            d = compute_l1_norm(car.position , route.start)
            if d<closest_distance:
                closest_distance = d
                closestCar = car
                
    closestCar.current_ride = route
    closestCar.status = "assigned"
    return closestCar

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
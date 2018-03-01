<<<<<<< HEAD
from data import Coord
from src.file_utils import read_data
import numpy as np

original_data = None
working_data = None

def load_data(filename):
    original_data = read_data(filename)

def move_one_towards(current_position, destination):
    dx = destination.x - current_position.x
    if abs(dx) > 0:
        return Coord(current_position.x + np.sign(dx), current_position.y)
    else:
        return Coord(current_position.x, current_position.y + np.sign(destination.y - current_position.y))


    pass


=======
from src.file_utils import read_data
from src.utilities import compute_l1_norm

original_data = None
working_data = None

def load_data(filename):
    original_data = read_data(filename)
    pass

>>>>>>> c3c85638ba746b972b851f5a9feb0474cd6f3d81
# RAFI
def cull_rides():
    pass

<<<<<<< HEAD

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
=======
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
>>>>>>> c3c85638ba746b972b851f5a9feb0474cd6f3d81
    pass

# Harry

# mutates cars
def update_positions(cars):
    for car in cars:
        if car.occupied_by is not None:
            car.position = move_one_towards(car.position, car.occupied_by.end)
        elif car.assigned_to is not None:
            car.position = move_one_towards(car.position, car.assigned_to.start)


def run_simulation():
    timestep = 0
    cars = []

    while True:
        # remove impossible rides
        cull_rides()
        # allocate the free cars
        free_cars = allocate_rides_to_cars(cars)
        # update positions
<<<<<<< HEAD
        update_positions(cars)
        update_status()
=======
        update_status()
        update_positions()
>>>>>>> c3c85638ba746b972b851f5a9feb0474cd6f3d81
        # increment timestep
        timestep+=1


if __name__ == "__main__":
    load_data("data/a_example.in")
    run_simulation()
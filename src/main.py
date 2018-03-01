from data import Coord
from src.file_utils import read_data
from src.utilities import compute_l1_norm
import numpy as np

original_data = None
working_data = None

def load_data(filename):
    original_data = read_data(filename)
  
# RAFI
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
        # remove impossible rides (doesn't mutate input)
        cull_rides()
        # generate a list of free cars (doesn't mutate input)
        available_cars()
        # allocate the free cars
        free_cars = allocate_rides_to_cars(cars)
        # update positions
        # increment timestep
        timestep+=1


if __name__ == "__main__":
    load_data("data/a_example.in")
    run_simulation()
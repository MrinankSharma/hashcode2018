from data import Coord
import numpy as np


original_data = None
working_Data = None


def move_one_towards(current_position, destination):
    dx = destination.x - current_position.x
    if abs(dx) > 0:
        return Coord(current_position.x + np.sign(dx), current_position.y)
    else:
        return Coord(current_position.x, current_position.y + np.sign(destination.y - current_position.y))


def load_data():
    # TO DO - LOAD DATA
    pass


def cull_rides():
    pass


def allocate_rides_to_cars():
    pass


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
        update_positions(cars)
        # increment timestep
        timestep+=1


if __name__ == "__main__":
    load_data()
    run_simulation()
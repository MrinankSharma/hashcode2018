# coding=utf-8

import numpy as np

# File format
# The first line of the input file contains the following integer numbers separated by single spaces:
# ● R – number of rows of the grid ( 1 ≤ R ≤ 1 0000)
# ● C – number of columns of the grid ( 1 ≤ C ≤ 1 0000)
# ● F – number of vehicles in the fleet ( 1 ≤ F ≤ 1 000)
# ● N – number of rides ( 1 ≤ N ≤ 1 0000)
# ● B – per-ride bonus for starting the ride on time ( 1 ≤ B ≤ 1 0000)
# ● T – number of steps in the simulation ( 1 ≤ T ≤ 1 0 9 )
#
# N subsequent lines of the input file describe the individual rides, from ride 0 to ride N − 1 . Each line
# contains the following integer numbers separated by single spaces:
# ● a – the row of the start intersection ( 0 ≤ a < R )
# ● b – the column of the start intersection ( 0 ≤ b < C )
# ● x – the row of the finish intersection ( 0 ≤ x < R )
# ● y – the column of the finish intersection ( 0 ≤ y < C )
# ● s – the earliest start ( 0 ≤ s < T )
# ● f – the latest finish ( 0 ≤ f ≤ T ) , ( f ≥ s + | x − a | + | y − b |)
# ○ note that f can be equal to T – this makes the latest finish equal to the end of the simulation


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class RideData:
    def __init__(self, start, end, start_time, finish_time, original_index):
        self.start = start
        self.end = end
        self.start_time = start_time
        self.finish_time = finish_time
        self.original_index = original_index

    def __str__(self):
        return f"from: {self.start}, to: {self.end}"


# rides is an array of RideData
class Data:
    def __init__(self, row_count, column_count, vehicle_count, start_on_time_bonus, step_count, rides):
        self.row_count = row_count
        self.column_count = column_count
        self.vehicle_count = vehicle_count
        self.start_on_time_bonus = start_on_time_bonus
        self.step_count = step_count
        self.rides = rides


# position is a Coord
class Vehicle:


    def __init__(self):
        self.position = Coord(0, 0)
        # status is occupied, unassigned or assigned.
        self.status = "unassigned"

        # of PREVIOUSLY COMPLETED RIDES
        self.rideHistory = []
        # no ride right at the start
        self.current_ride = None

    def updateStatus(self):
        if self.current_ride:
            if self.position == self.current_ride.start:
                self.status = "occupied"
            elif self.position == self.current_ride.end:
                self.status = "unassigned"
                self.current_ride = None

            # otherwise don't change
        else:
            self.status = "unassigned"

    def move(self):
        if self.current_ride is not None:
            destination = None
            if self.status == "assigned":
                destination = self.current_ride.start
            elif self.status == "occupied":
                destination = self.current_ride.end
            else:
                assert False

            dx = destination.x - self.position.x
            dy = destination.y - self.position.y

            if abs(dx) > 0:
                self.position.x += np.sign(dx)
            else:
                self.position.y += np.sign(dy)



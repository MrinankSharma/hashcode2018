# coding=utf-8

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


class RideData:
    def __init__(self, start, end, start_time, finish_time, original_index):
        self.start = start
        self.end = end
        self.start_time = start_time
        self.finish_time = finish_time
        self.original_index = original_index

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
    # of PREVIOUSLY COMPLETED RIDES
    rideHistory = []

    # no ride right at the start
    current_ride = None

    def __init__(self, position):
        self.position = position



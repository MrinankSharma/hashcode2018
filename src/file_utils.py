# coding=utf-8
import os.path
from data import Data, RideData, Coord


def parse_ride(ride, index):
    # ● a – the row of the start intersection ( 0 ≤ a < R )
    # ● b – the column of the start intersection ( 0 ≤ b < C )
    # ● x – the row of the finish intersection ( 0 ≤ x < R )
    # ● y – the column of the finish intersection ( 0 ≤ y < C )
    # ● s – the earliest start ( 0 ≤ s < T )
    # ● f – the latest finish ( 0 ≤ f ≤ T ) , ( f ≥ s + | x − a | + | y − b |)
    # ○ note that f can be equal to T – this makes the latest finish equal to the end of the simulation

    [a, b, x, y, s, f] = map(int, ride.split(' '))
    return RideData(
        start=Coord(a, b),
        end=Coord(x, y),
        start_time=s,
        finish_time=f,
        original_index=index
    )


def read_data(file_name):
    with open(os.path.join('..', 'data', file_name), 'r') as f:
        params = map(int, next(f).split(' '))
        [row_count, col_count, vehicle_count, ride_count, start_on_time_bonus, step_count] = params

        rides = []

        for index in range(0, ride_count):
            object = parse_ride(next(f), index)
            rides.append(object)

        assert ride_count == len(rides)

    f.close()

    return Data(
        row_count=row_count,
        column_count=col_count,
        vehicle_count=vehicle_count,
        start_on_time_bonus=start_on_time_bonus,
        step_count=step_count,
        rides=rides,
    )

def write_data(file_name, data):
    '''Write the output data to file, assuming that we have all the vehicles in a list'''
    myStr = []
    for vehicle in data:
        myStr += generate_line(vehicle)
    # Remove final newline
    myStr = myStr[:-1]
    myStr = ''.join(myStr)

    try:
        os.mkdir('../output')
    except OSError:
        pass

    with open(os.path.join('..', 'output', file_name), 'w') as f:
        f.write(myStr)

    f.close()

def generate_line(vehicle):
    '''Generate a line of the output string, applicable to one vehicle'''
    rideHistory = vehicle.rideHistory
    string = [str(len(rideHistory))," "]
    for ride in vehicle.rideHistory:
        string.append(str(ride.original_index))
        string.append(" ")
    # Remove final space and add a newline
    string = string[:-1]
    string.append("\n")
    return string

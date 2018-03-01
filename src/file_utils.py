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
            rides.append(parse_ride(next(f), index))

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
    str = "the output, RAPHI will create this"

    try:
        os.mkdir('../output')
    except OSError:
        pass

    with open(os.path.join('..', 'output', file_name), 'w') as f:
        f.write(str)

    f.close()

data = read_data("a_example.in")
write_data("Hia.txt", data)
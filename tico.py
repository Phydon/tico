import sys
import re
from datetime import datetime as dt


def main():
    inp = get_args()

    times = []
    for arg in inp:
        check_format(arg)
        times.append(str_to_dt(to_time_str(arg)))

    delta = get_delta(times)

    datetime_str = dt_to_str(delta)

    print(datetime_str)


def get_args():
    if len(sys.argv[:]) <= 1:
        print(f"Usage: {sys.argv[0]} <TIME> <TIME> <...>")
        sys.exit(1)

    # only pairs are allowed -> so number of timestamps should be an even number
    if len(sys.argv[:]) % 2 == 0:
        print("ERROR - Invalid number of arguments: Enter valid time pairs")
        sys.exit(1)

    return sys.argv[1:]


def check_format(inp: str):
    rex = re.compile(r"^[0-9]{4}$")

    if not rex.match(inp):
        print(f"ERROR - invalid input: '{inp}' - Format per timestamp should be '0000'")
        sys.exit(1)


def to_time_str(inp: str) -> str:
    assert len(inp) == 4, "Invalid input length"
    assert len([i for i in inp if not i.isdigit()]) == 0, "Found non-integers in input"

    time_lst = [inp[i : i + 2] for i in range(0, len(inp), 2)]

    return str(time_lst[0] + ":" + time_lst[1])


def str_to_dt(time_str: str) -> dt:
    try:
        return dt.strptime(time_str, "%H:%M")
    except ValueError as err:
        # handle case when given time format isn't valid -> e.g. '2501 1234'
        print(f"ERROR - Invalid input: '{time_str}' - {err}")
        sys.exit(1)


def get_delta(times: list[dt]) -> dt:
    assert len(times) % 2 == 0, "Odd number of times found -> pairs needed"

    # calculate delta between pairs and add delta together
    delta = dt.strptime("00:00", "%H:%M")
    for i in range(0, len(times), 2):
        delta += times[i + 1] - times[i]

        if i == len(times) - 2:
            break

    return delta


def dt_to_str(datetime: dt) -> str:
    return datetime.strftime("%H:%M")


if __name__ == "__main__":
    main()

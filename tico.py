# TODO accept multiple time pairs and calculate overall timedelta
# TODO e.g. teimdelta from 06:01 - 08:04 + 08:15 - 12:04 + 12:45 - 15:00
import sys
import re
from datetime import datetime as dt
from datetime import timedelta as td


def main():
    inp = get_args()

    # TODO accept more than one input time-pair (e.g.: '0600 1200')
    # TODO get input pairs if more than 2 pairs provided
    # TODO check for each pair of time strings
    # TODO e.g.: pair 1: '0600 1200'; pair2: '1300 1330'
    check_format(inp)

    inp = inp.split()
    inp1 = inp[0]
    inp2 = inp[1]

    time_str1 = to_time_str(inp1)
    time_str2 = to_time_str(inp2)

    time1 = str_to_dt(time_str1)
    time2 = str_to_dt(time_str2)

    delta = get_delta(time1, time2)

    delta_datetime = td_to_dt(delta)

    datetime_str = dt_to_str(delta_datetime)

    print(datetime_str)


def get_args():
    if len(sys.argv[:]) <= 1:
        print(f"Usage: {sys.argv[0]} <TIME> <TIME> <...>")
        sys.exit(1)

    return " ".join(sys.argv[1:])


def check_format(inp: str):
    rex = re.compile(r"^[0-9]{4}(\s)+[0-9]{4}$")

    if not rex.match(inp):
        print(f"ERROR - invalid input: '{inp}' - Format should be '0000 0000'")
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
        # INFO handle case when given time format isn't valid
        # INFO e.g. '2501 1234'
        print(f"ERROR: Invalid input: '{time_str}' - {err}")
        sys.exit(1)


def get_delta(t1: dt, t2: dt) -> td:
    return t2 - t1


def td_to_dt(td) -> dt:
    # INFO handle negative timedelta
    if "-" in str(td):
        print(
            f"ERROR: Invalid datetime order - negative timedelta calculated: '{str(td)}'"
        )
        sys.exit(1)

    return dt.strptime(str(td), "%H:%M:%S")


def dt_to_str(datetime: dt) -> str:
    return datetime.strftime("%H:%M")


if __name__ == "__main__":
    main()

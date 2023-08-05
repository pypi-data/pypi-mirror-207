import re
import urllib.request
from functools import cache

import advent
from advent.errors import handle_error


@cache
def get_puzzle_input(year: int, day: int) -> str:
    """Get your puzzle input for a given year and day"""

    req = urllib.request.Request(advent.URL.format(year, day), headers=advent.HEADERS)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as err:
        handle_error(err)
    data = response.read().decode()
    return data


def get_ints(string: str) -> list[int]:
    """Return a list of integers found in a string"""

    ints = [int(n) for n in re.findall(r"\d+", string)]
    return ints

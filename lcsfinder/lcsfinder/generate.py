"""Automatically generate data used for benchmarking."""

import random
import string

from lcsfinder.constants import CONSTANTS


def generate_data(data_type: str, size: int) -> tuple:
    """Generate two strings of the same size for a doubling experiment."""
    if size <= 0:
        raise ValueError("Size must be a positive integer.")

    if data_type == CONSTANTS.DATA_TYPE_INTS:
        # Generate two strings of random integers
        str1 = "".join(
            str(random.randint(CONSTANTS.RANDOM_MIN, CONSTANTS.RANDOM_MAX))
            for _ in range(size)
        )
        str2 = "".join(
            str(random.randint(CONSTANTS.RANDOM_MIN, CONSTANTS.RANDOM_MAX))
            for _ in range(size)
        )
    elif data_type == CONSTANTS.DATA_TYPE_CHARS:
        # Generate two strings of random characters
        str1 = "".join(random.choices(string.ascii_letters, k=size))
        str2 = "".join(random.choices(string.ascii_letters, k=size))
    else:
        raise ValueError("DataType must be 'ints' or 'chars'")

    return str1, str2


# implement all of the generation functions so that your program can
# generate data according to the requirements in the README.md file. Please
# note that you should be able to generate:
# - strings that contain characters
# - strings that contain numbers
# The strings must always be of the same size. The size of the strings must
# follow the rules associated with running a doubling experiment. You should
# generate the strings and then confirm that it works through test cases.

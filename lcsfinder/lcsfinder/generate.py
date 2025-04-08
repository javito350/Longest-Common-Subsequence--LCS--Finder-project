"""Automatically generate data used for benchmarking."""

import random
import string

from lcsfinder.constants import CONSTANTS


def generate_data(data_type: str, size: int) -> tuple:
    """Generate two strings of the same size for a doubling experiment."""
    if size <= 0:
        raise ValueError("Size must be a positive integer.")  # Validating size

    if data_type == CONSTANTS.DATA_TYPE_INTS:
        # Generate two strings of random integers
        str1 = "".join(
            str(random.randint(CONSTANTS.RANDOM_MIN, CONSTANTS.RANDOM_MAX))
            for _ in range(size)
        )
        str2 = "".join(
            str(random.randint(CONSTANTS.RANDOM_MIN, CONSTANTS.RANDOM_MAX))
            for _ in range(size)  # Generating random integers
        )
    elif data_type == CONSTANTS.DATA_TYPE_CHARS:
        # Generate two strings of random characters
        str1 = "".join(random.choices(string.ascii_letters, k=size))
        str2 = "".join(random.choices(string.ascii_letters, k=size))
    else:
        raise ValueError("DataType must be 'ints' or 'chars'")

    return str1, str2  # Generating two strings of the same size

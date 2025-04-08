"""Define constants with dataclasses."""

from dataclasses import dataclass


@dataclass(frozen=True)
class LCSFinderConstants:
    """Constants for the LCSFinder benchmarking tool."""

    START_SIZE: int = 10  # Initial size of the input strings for benchmarking
    RUNS: int = 5  # Number of benchmarking runs
    DOUBLING: bool = True
    DATA_TYPE_INTS: str = "ints"  # Data type for integers
    DATA_TYPE_CHARS: str = "chars"  # Data type for characters
    RANDOM_MIN: int = 0  # Minimum value for random integers
    RANDOM_MAX: int = 100  # Maximum value for random integers


# Create a global instance of the constants
CONSTANTS = LCSFinderConstants()

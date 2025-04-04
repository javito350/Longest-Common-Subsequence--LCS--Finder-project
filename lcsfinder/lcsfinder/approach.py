"""Configuration of the benchmarking tool and its approaches."""

from enum import Enum


class AlgorithmType(str, Enum):
    """Define the type of the LCS algorithm to use for benchmarking."""

    recursive = "recursive"
    dynamic = "dynamic"
    calculate = "calculate"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class DataType(str, Enum):
    """Define the type of data used in the LCS algorithm."""

    ints = "ints"
    chars = "chars"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class BenchmarkingStrategy(str, Enum):
    """Define the benchmarking strategy."""

    double = "double"
    order_of_magnitude = "order_of_magnitude"

    def __str__(self):
        """Define a default string representation."""
        return self.value


# All all of the enums that you need to define the configuration
# of the approach through the command-line interface of the tool.

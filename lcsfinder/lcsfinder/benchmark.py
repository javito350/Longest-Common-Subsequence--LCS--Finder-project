"""Run a benchmark on a function that can automatically find the LCS."""

import timeit
from dataclasses import dataclass
from typing import Callable, List

from lcsfinder.approach import AlgorithmType, BenchmarkingStrategy, DataType
from lcsfinder.generate import generate_data


class BenchmarkData:
    """A class to represent the benchmark data."""

    def __init__(self, run_count: int, input_size: int, execution_time: float):
        """Initialize the benchmark data."""
        self.run_count = run_count
        self.input_size = input_size
        self.execution_time = execution_time


@dataclass
class BenchmarkConfig:
    """Configuration for the benchmarking function."""

    algorithm_type: AlgorithmType
    data_type: DataType
    benchmarking_strategy: BenchmarkingStrategy
    startsize: int
    runs: int


def benchmarking(
    config: BenchmarkConfig, lcs_function: Callable
) -> List[BenchmarkData]:
    """Benchmarking function for LCS algorithms."""
    benchmark_data_list = []

    for run_count in range(1, config.runs + 1):
        # Determine input size based on the benchmarking strategy
        if config.benchmarking_strategy == BenchmarkingStrategy.double:
            input_size = config.startsize * (2 ** (run_count - 1))
        elif (
            config.benchmarking_strategy
            == BenchmarkingStrategy.order_of_magnitude
        ):
            input_size = config.startsize * (10 ** (run_count - 1))
        else:
            raise ValueError("Unsupported benchmarking strategy")

        # Generate input data
        str1, str2 = generate_data(config.data_type, input_size)

        # Measure execution time of the LCS function
        time = min(
            timeit.repeat(lambda: lcs_function(str1, str2), repeat=3, number=1)
        )

        # Store the benchmark data
        benchmark_data_list.append(BenchmarkData(run_count, input_size, time))

    return benchmark_data_list


def find_maximum(data: List[BenchmarkData]) -> BenchmarkData:
    """Return the benchmark data with the maximum execution time."""
    return max(data, key=lambda x: x.execution_time)


def find_minimum(data: List[BenchmarkData]) -> BenchmarkData:
    """Return the benchmark data with the minimum execution time."""
    return min(data, key=lambda x: x.execution_time)


def find_average(data: List[BenchmarkData]) -> float:
    """Return the average execution time."""
    return sum(item.execution_time for item in data) / len(data) # return average time of all runs

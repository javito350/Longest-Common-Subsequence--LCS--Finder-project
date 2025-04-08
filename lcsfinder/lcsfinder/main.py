"""Conduct experiments to evaluate performance of LCS computation."""

import typer
from rich.console import Console
from rich.table import Table

from lcsfinder.approach import AlgorithmType, BenchmarkingStrategy, DataType
from lcsfinder.benchmark import (
    BenchmarkConfig,
    benchmarking,
    find_average,
    find_maximum,
    find_minimum,
)
from lcsfinder.lcs import lcs_calculate, lcs_dynamic, lcs_recursive

# Create a Typer object to support the command-line interface
cli = typer.Typer()

# Create a console for display of rich text
console = Console()


@cli.command()
def main(
    algorithmtype: AlgorithmType = typer.Option(AlgorithmType.recursive),
    datatype: DataType = typer.Option(DataType.ints),
    strategy: BenchmarkingStrategy = typer.Option(BenchmarkingStrategy.double),
    startsize: int = typer.Option(10),
    runs: int = typer.Option(5),
):
    """Evaluate the performance of LCS algorithms."""
    # Display details about the configuration of the benchmarking tool
    console.print(
        "\n[bold red]Benchmarking Tool for LCS Computation[/bold red]\n"
    )
    console.print(f"Algorithm: {algorithmtype}")
    console.print(f"Data type: {datatype}")
    console.print(f"Benchmarking strategy: {strategy}")
    console.print(f"Number of runs: {runs}\n")

    # Select the appropriate LCS function
    if algorithmtype == AlgorithmType.recursive:
        lcs_function = lcs_recursive
    elif algorithmtype == AlgorithmType.dynamic:
        lcs_function = lcs_dynamic
    elif algorithmtype == AlgorithmType.calculate:
        lcs_function = lcs_calculate
    else:
        console.print(
            "[bold red]Error:[/bold red] Unsupported algorithm type."
        )
        return

    try:
        # Perform the benchmarking operation
        config = BenchmarkConfig(
            algorithm_type=algorithmtype,
            data_type=datatype,
            benchmarking_strategy=strategy,
            startsize=startsize,
            runs=runs,
        )

        results = benchmarking(config, lcs_function)

        # Display the benchmarking results in a table
        table = Table(title="Benchmark Results")
        table.add_column("Run", justify="right")
        table.add_column("Size", justify="right")
        table.add_column("Time (seconds)", justify="right")

        for result in results:
            table.add_row(
                str(result.run_count),
                str(result.input_size),
                f"{result.execution_time:.6f}",
            )

        console.print(table)

        # Calculate statistics
        min_result = find_minimum(results)
        max_result = find_maximum(results)
        avg_time = find_average(results)

        # Display the statistics
        console.print("\n[bold]Benchmark Statistics[/bold]:")
        console.print(
            f"Minimum execution time: {min_result.execution_time:.6f} seconds "
            f"(Run {min_result.run_count}, Size {min_result.input_size})"
        )
        console.print(
            f"Maximum execution time: {max_result.execution_time:.6f} seconds "
            f"(Run {max_result.run_count}, Size {max_result.input_size})"
        )
        console.print(
            f"Average execution time: {avg_time:.6f} seconds across {runs} runs"
        )

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

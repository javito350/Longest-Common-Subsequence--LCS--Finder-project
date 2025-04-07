# Finding the Longest Common Subsequence

## Javier Bejarano

## Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."

I adhered to the Allegheny College Honor Code while completing this project.

**IMPORTANT:** If you do not type the required sentence then the course
instructor will not know that you adhered to the Allegheny College Honor Code
while completing the project.

## References

Copilot.

## Program Output

### Report at least two examples of program output from when you ran the `systemsense` program

#### First output from running the `systemsense` program

```text
output
Displaying System Information

╭─────────────────────────────────────────  System Information Panel ─────────────────────────────────────────╮
│ ╭──────────────────┬────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ System Parameter │ Parameter Value                                                                        │ │
│ ├──────────────────┼────────────────────────────────────────────────────────────────────────────────────────┤ │
│ │ battery          │ 62.00% battery life remaining, unknown seconds remaining                               │ │
│ │ cpu              │ AMD64                                                                                  │ │
│ │ cpucores         │ 8                                                                                      │ │
│ │ cpufrequencies   │ Min: 0.0 Mhz, Max: 2112.0 Mhz                                                          │ │
│ │ datetime         │ 2025-01-23 21:49:47                                                                    │ │
│ │ disk             │ Using 96.58 GB of 475.84 GB                                                            │ │
│ │ hostname         │ DESKTOP-MEH0K09                                                                        │ │
│ │ memory           │ 31.88 GB                                                                               │ │
│ │ platform         │ Windows                                                                                │ │
│ │ pythonversion    │ 3.12.1                                                                                 │ │
│ │ runningprocesses │ 294                                                                                    │ │
│ │ swap             │ Total: 2.00 GB, Used: 0.08 GB, Free: 1.92 GB                                           │ │
│ │ system           │ 64bit                                                                                  │ │
│ │ systemload       │ System load information is not available on Windows.                                   │ │
│ │ virtualenv       │ Virtual environment at:                                                                │ │
│ │                  │   │ │
│ ╰──────────────────┴────────────────────────────────────────────────────────────────────────────────────────╯ │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


Displaying Benchmark Results

╭─────────────────────────────────────── Benchmark Information Panel ────────────────────────────────────────╮
│ ╭──────────────────────────────┬────────────────────────────────────────────────────────────────╮             │
│ │ Benchmark Name               │ Benchmark Results (sec)                                        │             │
│ ├──────────────────────────────┼────────────────────────────────────────────────────────────────┤             │
│ │ benchmark_addition           │ [1.945940500125289, 1.9330923995003104, 2.015283400192857]     │             │
│ │ benchmark_exponentiation     │ [3.7314814999699593, 3.6686081998050213, 3.693094700574875]    │             │
│ │ benchmark_multiplication     │ [1.5873325001448393, 1.5692357998341322, 1.5867868000641465]   │             │
│ │ rangelist                    │ [0.22485849913209677, 0.20735279936343431, 0.2036055000498891] │             │
│ │ time_benchmark_concatenation │ [5.881490300409496, 5.487309699878097, 6.508231399580836]      │             │
│ ╰──────────────────────────────┴────────────────────────────────────────────────────────────────╯             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Second output from running the `systemsense` program

```text
output
Displaying System Information

╭──────────────────────────────────────────── System Information Panel ─────────────────────────────────────────────╮
│ ╭──────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────╮  │
│ │ System Parameter │ Parameter Value                                                                              │  │
│ ├──────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────┤  │
│ │ battery          │ No battery is present                                                                        │  │
│ │ cpu              │ x86_64                                                                                       │  │
│ │ cpucores         │ 2                                                                                            │  │
│ │ cpufrequencies   │ Min: 0.0 Mhz, Max: 0.0 Mhz                                                                   │  │
│ │ datetime         │ 2025-01-24 02:39:20                                                                          │  │
│ │ disk             │ Using 47.39 GB of 71.61 GB                                                                   │  │
│ │ hostname         │ fv-az1131-112                                                                                │  │
│ │ memory           │ 7.75 GB                                                                                      │  │
│ │ platform         │ Linux                                                                                        │  │
│ │ pythonversion    │ 3.12.8                                                                                       │  │
│ │ runningprocesses │ 129                                                                                          │  │
│ │ swap             │ Total: 3.00 GB, Used: 0.00 GB, Free: 3.00 GB                                                 │  │
│ │ system           │ 64bit                                                                                        │  │
│ │ systemload       │ 1min: 0.61328125, 5min: 0.36767578125, 15min: 0.15576171875                                  │  │
│ │ virtualenv       │ │  │
│ ╰──────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────╯  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


Displaying Benchmark Results

╭───────────────────────────────────────────  Benchmark Information Panel ───────────────────────────────────────────╮
│ ╭──────────────────────────────┬────────────────────────────────────────────────────────────────╮                    │
│ │ Benchmark Name               │ Benchmark Results (sec)                                        │                    │
│ ├──────────────────────────────┼────────────────────────────────────────────────────────────────┤                    │
│ │ benchmark_addition           │ [1.499241847999997, 1.4721593159999884, 1.4720247559999962]    │                    │
│ │ benchmark_exponentiation     │ [3.0969970730000114, 3.1163217720000205, 3.050101438000013]    │                    │
│ │ benchmark_multiplication     │ [1.2175857599999915, 1.192235927000013, 1.2040489809999997]    │                    │
│ │ rangelist                    │ [0.1430895459999988, 0.15392396999999391, 0.14262091899999518] │                    │
│ │ time_benchmark_concatenation │ [3.8086325510000165, 3.8252644309999937, 3.868314713000018]    │                    │
│ ╰──────────────────────────────┴────────────────────────────────────────────────────────────────╯                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Use three fenced code blocks to provide output from all different runs of `lcsfinder` for the three algorithms

#### Provide the command the output for the runs of the `lcsfinder` and the first algorithm

- TODO: Provide the complete command-lines for your uses of the `lcsfinder` program
- TODO: Provide your own example of a command(s) and the output that it produces
- TODO: Make sure that each run is for a unique configuration of the tool
- TODO: Make sure that each run is only for the use of the tool with the specified algorithm

- `poetry run lcsfinder --algorithmtype recursive --startsize 1 --runs 2 --datatype ints --strategy double`

```text
output
Benchmarking Tool for LCS Computation

Algorithm: recursive
Data type: ints
Benchmarking strategy: double
Number of runs: 2

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    1 │       0.000006 │
│   2 │    2 │       0.000015 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000006 seconds (Run 1, Size 1)
Maximum execution time: 0.000015 seconds (Run 2, Size 2)
Average execution time: 0.000010 seconds across 2 runs
```

- `poetry run lcsfinder --algorithmtype recursive --startsize 2 --runs 3 --datatype chars --strategy double`

```text 
output
Benchmarking Tool for LCS Computation

Algorithm: recursive
Data type: chars
Benchmarking strategy: double
Number of runs: 3

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    2 │       0.000005 │
│   2 │    4 │       0.000032 │
│   3 │    8 │       0.005739 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000005 seconds (Run 1, Size 2)
Maximum execution time: 0.005739 seconds (Run 3, Size 8)
Average execution time: 0.001925 seconds across 3 runs
```

- `poetry run lcsfinder --algorithmtype recursive --startsize 1  --runs 2  --datatype chars --strategy order_of_magnitude`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: recursive
Data type: chars
Benchmarking strategy: order_of_magnitude
Number of runs: 2

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    1 │       0.000006 │
│   2 │   10 │       0.046317 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000006 seconds (Run 1, Size 1)
Maximum execution time: 0.046317 seconds (Run 2, Size 10)
Average execution time: 0.023162 seconds across 2 runs
```

#### Provide the command output for the runs of the `lcsfinder` and the second algorithm

- TODO: Provide the complete command-lines for your uses of the `lcsfinder` program
- TODO: Provide your own example of a command(s) and the output that it produces
- TODO: Make sure that each run is for a unique configuration of the tool
- TODO: Make sure that each run is only for the use of the tool with the specified algorithm

- `poetry run lcsfinder --algorithmtype dynamic --startsize 1 --runs 2 --datatype ints --strategy double`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: dynamic
Data type: ints
Benchmarking strategy: double
Number of runs: 2

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    1 │       0.000003 │
│   2 │    2 │       0.000003 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000003 seconds (Run 1, Size 1)
Maximum execution time: 0.000003 seconds (Run 2, Size 2)
Average execution time: 0.000003 seconds across 2 runs
```

- `poetry run lcsfinder --algorithmtype dynamic --startsize 2 --runs 3 --datatype chars --strategy double`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: dynamic
Data type: chars
Benchmarking strategy: double
Number of runs: 3

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    2 │       0.000016 │
│   2 │    4 │       0.000013 │
│   3 │    8 │       0.000036 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000013 seconds (Run 2, Size 4)
Maximum execution time: 0.000036 seconds (Run 3, Size 8)
Average execution time: 0.000022 seconds across 3 runs
```

- `poetry run lcsfinder --algorithmtype dynamic --startsize 2  --runs 2  --datatype chars --strategy order_of_magnitude`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: dynamic
Data type: chars
Benchmarking strategy: order_of_magnitude
Number of runs: 2

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    2 │       0.000006 │
│   2 │   20 │       0.000179 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000006 seconds (Run 1, Size 2)
Maximum execution time: 0.000179 seconds (Run 2, Size 20)
Average execution time: 0.000093 seconds across 2 runs
```

#### Provide the command output for the runs of the `lcsfinder` and the third algorithm

- TODO: Provide the complete command-lines for your uses of the `lcsfinder` program
- TODO: Provide your own example of a command(s) and the output that it produces
- TODO: Make sure that each run is for a unique configuration of the tool
- TODO: Make sure that each run is only for the use of the tool with the specified algorithm

- `poetry run lcsfinder --algorithmtype calculate --startsize 1 --runs 2 --datatype ints --strategy double`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: calculate
Data type: ints
Benchmarking strategy: double
Number of runs: 2

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    1 │       0.000013 │
│   2 │    2 │       0.000032 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000013 seconds (Run 1, Size 1)
Maximum execution time: 0.000032 seconds (Run 2, Size 2)
Average execution time: 0.000022 seconds across 2 runs
```

- `poetry run lcsfinder --algorithmtype calculate --startsize 2 --runs 3 --datatype chars --strategy double`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: calculate
Data type: chars
Benchmarking strategy: double
Number of runs: 3

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    2 │       0.000008 │
│   2 │    4 │       0.000027 │
│   3 │    8 │       0.000457 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000008 seconds (Run 1, Size 2)
Maximum execution time: 0.000457 seconds (Run 3, Size 8)
Average execution time: 0.000164 seconds across 3 runs
```

- `poetry run lcsfinder --algorithmtype calculate --startsize 2  --runs 2  --datatype chars --strategy order_of_magnitude`

```text
output

Benchmarking Tool for LCS Computation

Algorithm: calculate
Data type: chars
Benchmarking strategy: order_of_magnitude
Number of runs: 2

       Benchmark Results       
┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Run ┃ Size ┃ Time (seconds) ┃
┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │    2 │       0.000008 │
│   2 │   20 │       2.189447 │
└─────┴──────┴────────────────┘

Benchmark Statistics:
Minimum execution time: 0.000008 seconds (Run 1, Size 2)
Maximum execution time: 2.189447 seconds (Run 2, Size 20)
Average execution time: 1.094728 seconds across 2 runs
```

## Data Tables

### Benchmark Results Summary

| Algorithm   | Data Type | Strategy           | Start Size | Runs | Min Time (s) | Max Time (s) | Avg Time (s) |
|-------------|-----------|--------------------|------------|------|--------------|--------------|--------------|
| Recursive   | Ints      | Double             | 1          | 2    | 0.000006     | 0.000015     | 0.000010     |
| Recursive   | Chars     | Double             | 2          | 3    | 0.000005     | 0.005739     | 0.001925     |
| Recursive   | Chars     | Order of Magnitude | 1          | 2    | 0.000006     | 0.046317     | 0.023162     |
| Dynamic     | Ints      | Double             | 1          | 2    | 0.000003     | 0.000003     | 0.000003     |
| Dynamic     | Chars     | Double             | 2          | 3    | 0.000013     | 0.000036     | 0.000022     |
| Calculate   | Ints      | Double             | 1          | 2    | 0.000013     | 0.000032     | 0.000022     |
| Calculate   | Chars     | Order of Magnitude | 2          | 2    | 0.000008     | 2.189447     | 1.094728     |

TODO: You must add instrumentation using tools like `timeit` to ensure that the
`lcsfinder` calculates and reports the time overhead data that you will need
to complete the entire experiment. Before you conduct your experiments, please
carefully confirm that `lcsfinder` calculates and reports the time overhead
values in a correct fashion.

TODO: Use Markdown to provide one or more data tables that summarize the results
from running the `lcsfinder` program in all possible different configurations.

## Performance Analysis

TODO: Use several paragraphs and/or a list to explain each of the unique
configurations for which it is possible to run the `lcsfinder` program. Please
note that, for this algorithm engineering project, you are required to run the
`lcsfinder` tool in all possible valid configurations so that you can carefully
study the performance of all the key algorithms that you implemented in the
`lcs.py` file. You need to make sure that you specified values for `--startsize`
and `--runs` that ensure the `lcsfinder` will report performance results that
help you to accurately characterize the worst-case time complexity of the each
algorithm for finding the longest common subsequence of two strings. Your
performance analysis should also investigate whether or not the use of `int` or
`char` data influences the performance of the algorithms that find the LCS.

TODO: Make sure that your responses explain WHY certain configurations are faster!

TODO: It is not sufficient to ONLY explain WHICH configuration is faster!

TODO: It is not sufficient to ONLY discuss the empirical results! You must also
state and explain the worst-case time complexities for each of the stated
methods!

I have tested the `lcsfinder` program with the following configurations:

- **Recursive Algorithm with Ints**: This configuration was the fastest, with a minimum execution time of 0.000006 seconds and a maximum execution time of 0.000015 seconds. The average execution time was 0.000010 seconds across 2 runs. The recursive algorithm is efficient for small input sizes, but its performance degrades significantly as the input size increases due to its exponential time complexity of O(2^n).

- **Recursive Algorithm with Chars**: This configuration had a minimum execution time of 0.000005 seconds and a maximum execution time of 0.005739 seconds, with an average execution time of 0.001925 seconds across 3 runs. The performance of the recursive algorithm is significantly affected by the input size, as seen in the maximum execution time of 0.005739 seconds for a size of 8.

- **Recursive Algorithm with Order of Magnitude**: This configuration had a minimum execution time of 0.000006 seconds and a maximum execution time of 0.046317 seconds, with an average execution time of 0.023162 seconds across 2 runs. The order of magnitude strategy significantly increased the input size, leading to a much longer execution time.

- **Dynamic Algorithm with Ints**: This configuration was the fastest among the dynamic algorithm configurations, with a minimum execution time of 0.000003 seconds and a maximum execution time of 0.000003 seconds. The average execution time was 0.000003 seconds across 2 runs. The dynamic programming approach is more efficient than the recursive approach for larger input sizes, with a time complexity of O(n^2).
- **Dynamic Algorithm with Chars**: This configuration had a minimum execution time of 0.000013 seconds and a maximum execution time of 0.000036 seconds, with an average execution time of 0.000022 seconds across 3 runs. The dynamic programming approach is still efficient for larger input sizes, but the performance is slightly slower than the integer configuration due to the overhead of handling character data.

- **Dynamic Algorithm with Order of Magnitude**: This configuration had a minimum execution time of 0.000006 seconds and a maximum execution time of 0.000179 seconds, with an average execution time of 0.000093 seconds across 2 runs. The order of magnitude strategy significantly increased the input size, leading to a longer execution time.

- **Calculate Algorithm with Ints**: This configuration had a minimum execution time of 0.000013 seconds and a maximum execution time of 0.000032 seconds, with an average execution time of 0.000022 seconds across 2 runs. The calculate algorithm is similar to the dynamic programming approach, but it may have additional overhead due to the calculation of intermediate values.

- **Calculate Algorithm with Chars**: This configuration had a minimum execution time of 0.000008 seconds and a maximum execution time of 0.000457 seconds, with an average execution time of 0.000164 seconds across 3 runs. The performance of the calculate algorithm is slightly slower than the integer configuration due to the overhead of handling character data.

- **Calculate Algorithm with Order of Magnitude**: This configuration had a minimum execution time of 0.000008 seconds and a maximum execution time of 2.189447 seconds, with an average execution time of 1.094728 seconds across 2 runs. The order of magnitude strategy significantly increased the input size, leading to a much longer execution time.

## Professional Development

### Overall, what are the trade-offs associated with using a different algorithmic approaches to finding the longest common subsequence?

TODO: Provide a one-paragraph response that answers this question in your own words.

### What is challenging about designing an experiment to evaluate the performance of LCS finding?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Take Home Points

TODO: Provide a two to three sentence statement about the key takeaways from
conducting this experiment. Please note that the course instructor will display
some student takeaways on the course website and use them to facilitate
follow-on class discussions. The takeways that you write should be specifically
connected to the system that you implemented and the experiments that you
conducted.

# 🔬 Finding the Longest Common Subsequence

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue. svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## 📌 Project Overview

This project implements `lcsfinder`, a benchmarking suite designed to empirically evaluate three algorithmic approaches to solving the **Longest Common Subsequence (LCS)** problem. As a mathematical and computational study, it validates the theoretical transition from **exponential time complexity O(2ⁿ)** in naive recursion to **polynomial time complexity O(n·m)** using dynamic programming.

The tool performs **doubling experiments** with timing instrumentation to analyze algorithm performance across different data types (`int` and `char`) and input sizes. 

---

## ✨ Table of Contents

- [Implemented Algorithms](#-implemented-algorithms)
- [Key Features](#-key-features)
- [Installation & Setup](#-installation--setup)
- [Usage Examples](#-usage-examples)
- [Program Specification](#-program-specification)
- [Research Questions](#-research-questions)
- [Project Structure](#-project-structure)
- [Seeking Assistance](#-seeking-assistance)

---

## 🛠️ Implemented Algorithms

The `lcsfinder` benchmarks three distinct strategies:

1. **Recursive**:  Naive recursive implementation demonstrating the "overlapping subproblems" issue with exponential growth
2. **Dynamic**:  Memoization/tabulation approach using a 2D state-space matrix to eliminate redundant calculations
3. **Calculate**:  Optimized implementation for comparison against built-in language optimizations

Each algorithm is tested with both integer and character data types. 

---

## 🎯 Key Features

- **Doubling Experiments**: Systematically increases input size (N, 2N, 4N, ...) to empirically verify Big-O complexity
- **Timing Instrumentation**: Uses Python's `timeit` package for high-precision performance measurement
- **Flexible Data Types**: Supports both `int` and `char` sequence generation
- **Multiple Strategies**: Configurable growth strategies (doubling, order-of-magnitude, etc.)
- **Statistical Analysis**: Computes minimum, maximum, and average execution times across runs
- **Formatted Output**: Clean, justified output with consistent decimal precision

---

## 🚀 Installation & Setup

### Prerequisites

This project uses **Poetry** for dependency management and requires **Python 3.12. 8+**.

### Option 1: Using `devenv` (Recommended)

1. Install [`devenv`](https://devenv.sh/getting-started/) (Windows users should install WSL2 first)
2. Clone this repository: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
3. Initialize the development environment:
   ```bash
   devenv shell
   ```
4. Verify installation:
   ```bash
   python --version  # Should show 3.12.8+
   poetry --version  # Should show 2.0.0+
   ```
5. Install dependencies:
   ```bash
   poetry install
   ```

### Option 2: Using `mise` or Manual Installation

If `devenv` doesn't work, install Python 3.12.8+ and Poetry 2.0.0+ manually using [`mise`](https://mise.jdx.dev/) or your preferred method, then run:

```bash
poetry install
```

---

## 💻 Usage Examples

### Basic Usage

```bash
poetry run lcsfinder --help
```

### Dynamic Programming with Integer Data

```bash
poetry run lcsfinder --algorithmtype dynamic --startsize 1 --runs 5 --datatype ints --strategy double
```

**Expected Output:**

```text
Benchmarking Tool for Finding the LCS

Type of algorithm: dynamic
Data stored in list:  ints
Benchmarking strategy: double
Number of runs: 5

Run 1 of 5 for dynamic algorithm using size  1 took  0.0000010220 seconds
Run 2 of 5 for dynamic algorithm using size  2 took  0.0000043790 seconds
Run 3 of 5 for dynamic algorithm using size  4 took  0.0000224020 seconds
Run 4 of 5 for dynamic algorithm using size  8 took  0.0007647710 seconds
Run 5 of 5 for dynamic algorithm using size 16 took  1.3258309710 seconds

Minimum execution time:  0.0000010220 seconds for run 1 with size 1
Maximum execution time:  1.3258309710 seconds for run 5 with size 16

Average execution time:  0.2653247090 seconds across runs 1 through 5
```

### Recursive Algorithm with Character Data

```bash
poetry run lcsfinder --algorithmtype recursive --startsize 1 --runs 4 --datatype chars --strategy double
```

⚠️ **Warning**: The recursive implementation has exponential time complexity.  Use small `--runs` values to avoid prohibitively long execution times.

### Calculate Algorithm Comparison

```bash
poetry run lcsfinder --algorithmtype calculate --startsize 2 --runs 6 --datatype ints --strategy double
```

---

## 📊 Program Specification

### Command-Line Arguments

| Argument | Description | Values |
|----------|-------------|--------|
| `--algorithmtype` | Algorithm to benchmark | `recursive`, `dynamic`, `calculate` |
| `--startsize` | Initial input size | Positive integer |
| `--runs` | Number of experimental runs | Positive integer |
| `--datatype` | Type of data to generate | `ints`, `chars` |
| `--strategy` | Input growth strategy | `double` (default), custom strategies |

### Output Requirements

- **Diagnostic Information**: Algorithm type and all command-line parameters
- **Per-Run Results**: Size, execution time (formatted to 10 decimal places)
- **Statistical Summary**:  Minimum, maximum, and average execution times
- **Clean Formatting**: Right-aligned numbers, consistent decimal places

---

## 🔬 Research Questions

This project is designed to answer: 

1. How does execution time scale for recursive vs. dynamic implementations as input size doubles?
2. What is the empirical crossover point where dynamic programming becomes significantly faster? 
3. How does data type (`int` vs. `char`) affect algorithm performance?
4. Can we observe the theoretical O(2ⁿ) vs.  O(n·m) complexity difference in practice?

---

## 📁 Project Structure

```text
lcsfinder/
├── lcsfinder/           # Main source code (implement TODO markers here)
├── tests/               # Automated test suite
├── writing/
│   └── reflection.md    # Technical writing and analysis
├── config/
│   └── gatorgrade.yml   # Automated grading configuration
├── pyproject.toml       # Poetry configuration
└── README.md            # This file
```

---

## 🧠 Mathematical Foundation

The LCS problem exhibits **optimal substructure** and **overlapping subproblems**, making it ideal for dynamic programming.  The recurrence relation is:

```
LCS(X[1.. m], Y[1..n]) = 
  ⎧ LCS(X[1..m-1], Y[1..n-1]) + 1           if X[m] = Y[n]
  ⎨ max(LCS(X[1.. m-1], Y[1.. n]),
  ⎩     LCS(X[1..m], Y[1..n-1]))            otherwise
```

By storing solutions in a 2D table, we reduce time complexity from O(2ⁿ) to O(n·m).

---

## 🆘 Seeking Assistance

This project requires independent research and problem-solving. Not every implementation detail is covered in lectures—this is intentional to develop your skills as an algorithm engineer.

**Resources:**
- [Python timeit documentation](https://docs.python.org/3/library/timeit.html)
- [Measure execution time with timeit](https://note.nkmk.me/en/python-timeit-measure/)
- Office hours with course instructor
- Student technical leaders

**Before Submission:**
- ✅ Run `gatorgrade --config config/gatorgrade.yml` to verify requirements
- ✅ Complete all responses in `writing/reflection.md`
- ✅ Delete all `TODO` markers and replace with meaningful comments
- ✅ Ensure code runs for all specified configurations


## 📜 License

This project is part of an academic assignment.  Please consult your instructor regarding usage and sharing policies.

---

**🎯 Ready to benchmark?  Run your first experiment:**

```bash
poetry run lcsfinder --algorithmtype dynamic --startsize 1 --runs 5 --datatype ints --strategy double
```

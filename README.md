[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/EVrbCoMT)
# :microscope: Finding the Longest Common Subsequence

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## :sparkles: Table of Contents

<!---toc start-->

* [:microscope: Finding the Longest Common Subsequence](#microscope-finding-the-longest-common-subsequence)
  * [:sparkles: Table of Contents](#sparkles-table-of-contents)
  * [:sparkles: Introduction](#sparkles-introduction)
  * [:thumbsup: Seeking Assistance](#thumbsup-seeking-assistance)
  * [:airplane: Project Overview](#airplane-project-overview)
  * [:tada: Program Specification](#tada-program-specification)

<!---toc end-->

## :sparkles: Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course website for the due date or
ask the course instructor for more information about the due date or check the
due date by clicking the appropriate box inside of this file. Please note that
the content provided in the `README.md` file for this GitHub repository is an
overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project.

## :thumbsup: Seeking Assistance

Even though the course instructor will have covered all the concepts central to
this project before you start to work on it, please note that not every detail
needed to successfully complete the assignment will have been covered during
prior classroom sessions. This is by design as an important skill that you must
practice as an algorithm engineer is to search for and then understand and
ultimately apply the technical content found in additional resources.

## :airplane: Project Overview

This project invites you to implement and use a program called `lcsfinder` that
conducts an experiment to evaluate the performance of three different algorithms
(i.e., `recursive`, `dynamic`, and `calculate`) that determine the longest
common subsequence (LCS) of two strings that can contain either `int` or `char`
data. The `lcsfinder` program should also include "timing instrumentation" that
records the cost associated with the aforementioned algorithms for finding a
longest common subsequence. For instance, the `lcsfinder` could use the
[timeit](https://docs.python.org/3/library/timeit.html) package to measure the
performance of different LCS finding algorithms, following the pattern in the
article [measure execution time with timeit in
Python](https://note.nkmk.me/en/python-timeit-measure/). In summary, the
specific algorithms and configurations that your `lcsfinder` program should
evaluate include these and that you should experimentally evaluate with
well-defined research questions are as follows:

- `recursive` LCS finder with both `int` and `char` data
- `dynamic` LCS finder with both `int` and `char` data
- `calculate` LCS finder with both `int` and `char` data

After cloning this repository to your computer, please take the following steps
to get started on the project:

- To install the necessary software for running the `lcsfinder` program
that you will create as a part of this project, you may consider installing and
using the [`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind
that it is not necessary for you to install the `cachix` program that may be
referenced by these installation instructions. Please note that students who
are using Windows 11 should first install Windows subsystem for Linux (`wsl2`)
before attempting to install `devenv`. Once you have installed `devenv` and
cloned this repository to your computer, you can `cd` into the directory that
contains the `pyproject.toml` file and then type `devenv shell`. It is
important to note that the first time you run this command it may complete
numerous steps and take a considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains a recent version of Python and Poetry! You can verify
that you have the correct version of these two programs by typing:
  - `python --version`
  - `poetry --version`
- If you do not see a recent version of Python after typing the two
aforementioned commands, then it is possible that some part of the installation
process did not work correctly. If that occurs, then please read the following
suggestions and talk with the course instructor and a student technical leader
about what to do next.
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop using a
tool like [`mise`](https://mise.jdx.dev/). With that said, please make sure
that you use the most recent version of Python and Poetry to complete this
project and, whenever possible, those versions match the ones chosen in GitHub
Actions. This means that, to ensure that the results from running the
experiments are consistent and, as best as is possible, comparable to the
results from other computers, you should use exactly the same version of Python
and Poetry on your laptop and in GitHub Actions. For instance, when you run
`lcsfinder` in GitHub Actions, you should normally see that it is using
at least Poetry version `2.0.0` and Python version `3.12.8`.
- Before moving to the next step, you may need to again type `poetry install`
in order to avoid the appearance of warnings when you next run the
`lcsfinder` program. Now you can type the command `poetry run
lcsfinder --help` and explore how to use the program.

## :tada: Program Specification

Before implementing the program so that it adheres to the following
requirements and produces the expected output, please note that the program
will not work unless you add the required source code at the designated `TODO`
markers. With that said, after you complete a correct implementation of all the
`lcsfinder`'s features you can run it with the command `poetry run lcsfinder
--algorithmtype dynamic --startsize 1 --runs 5 --datatype ints --strategy
double` and see that it produces output like the following. Please note that
while the following example illustrates the type of output that the `lcsfinder`
might produce it (a) may offer empirical results that are different than those
that you see on your own laptop and (b) is only for a single example
configuration for how you can run the `lcsfinder` program.

```text
Benchmarking Tool for Finding the LCS

Type of list: dynamic
Data stored in list: ints
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

Some key aspects of the output that your implementation of the `lcsfinder`
should preserve are as follows:

- The output should include diagnostic information that explains the type of
algorithm (i.e., `recursive` or `dynamic` or `calculate`) and all the other
command-line arguments that the user specified.
- The `lcsfinder` program should be able to automatically generate either `char`
or `int` data. When it generates this data it must always ensure that the
letters or the numbers that are generated according the constraints of a
doubling experiment. This means that, for instance, it must always generate
inputs that are of the size dictated by the current run of the doubling
experiment.
- Although the `lcsfinder` program should be able to use a default `strategy` of
a doubling experiment, you are also invited to implement and use additional
strategies such as one that would increase the input size by an order of
magnitude. With that said, please bear in mind the worst-case time complexity of
the algorithms you are studying as you implement and run your benchmarks with
the chosen strategy --- be careful, in particular, about the fact that some
configurations of some algorithms may take a prohibitively long time to run!
- The output should have labels for each specific run that also shows the total
number of runs requested by the user.
- Each line that shows a performance result should include the size of the input
and then the amount of time in seconds that it took to perform the operation.
- The output should be formatted and justified so that it is easy to read, with
numbers aligned to the right and with a consistent number of decimal places.
- After the display of the execution times that arise from each run of the
benchmark, the output should show the minimum, maximum, and average execution
time values across the runs of the benchmark.

Please note that your implementation of the `lcsfinder` program should work for
all the specified experimental configurations in the introduction to the
project and in the `writing/reflection.md` file. If you study the files in the
`lcsfinder/` directory you will see that they have many `TODO` markers that
designate the functions you must implement so as to ensure that `lcsfinder`
runs the desired experiment and produces the correct output. Once you complete a
task associated with a `TODO` marker, make sure that you delete it and revise
the prompt associated with the marker into a meaningful comment.

It is important to note that, at minimum, your experimentation with the
`lcsfinder` must always operate according to the principles of a doubling
experiment. This means that the `lcsfinder` must systematically increase the
size of the instance of the `str` variables that are passed into the function
that can find the longest common subsequence. Ultimately, you should design your
own experiment and state and run experiments to answer your own research
questions, focusing on these key issues to ensure that you meet the baseline
requirements:

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker and
the entire prompt and then add your own comments to demonstrate that you
understand all the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional website.

# Two-Stage Stochastic Problem Solver for INDUSTRY - MANUFACTURING

This repository hosts the solution code for the **`Problem 1`** from the
assignment of **`MATHEMATICAL MODELING (CO2011) - HCMUT 2023`**, focusing on the
**`INDUSTRY - MANUFACTURING`** problem. The code implements a two-stage
stochastic problem-solving algorithm that optimizes pre-order and production
decisions under uncertainty.

## Overview

The algorithm is designed to address a **stochastic two-stage problem**, which
is a common challenge in the field of industrial manufacturing. The goal is to
make informed decisions in the **first stage** (pre-order) without complete
knowledge of future events, and then adjust those decisions in the **second
stage** (production) once the uncertainty is resolved.

The solution utilizes the **GAMS Python API** (`GAMSPy`) to model the problem
and compute the optimal strategy, taking into account the probabilistic nature
of demand and other uncertain parameters.

By leveraging the power of mathematical optimization and stochastic modeling,
this code helps students and professionals in the manufacturing industry to
visualize robust strategies that can withstand the unpredictability of
real-world scenarios.

## Description

The project consists of two main files: `main.py` and `helper.py`. The `main.py`
file defines the sets, parameters, variables, equations, and model for the
optimization problem. The `helper.py` file contains functions to print the
optimal results and scenario-specific outcomes.

## Getting Started

### Dependencies

- Python 3.10.11
- GAMSPy: A Python API for GAMS that allows for modeling and solving
  optimization problems.
- NumPy: A fundamental package for scientific computing with Python.

### Installing

- Clone the repository to your local machine.
- Ensure that you have Python and the required libraries installed.

### Executing program

- Run the `main.py` file in your Python environment.
- Input the required data when prompted by the program.

```bash
python main.py
```

## Authors

- **Nguyễn Ngọc Đình Khoa** - Team Leader, Work Distribution, Problem
  Understanding, Documentation
- **Lê Phong Hào** - Assistant Leader, Documentation
- **Lê Hà Nguyên Khánh** - Documentation
- **Phạm Trần Đăng Khoa** - Code Prototype, Source Code Documentation
- **Huỳnh Thanh Duy** - Source Code Completion, Input Implementation

## Acknowledgments

- Heartfelt thanks to all team members for their contributions and dedication to
  the project.
- Special appreciation to **Nguyễn Ngọc Đình Khoa** for leading the team and
  guiding the project's direction.
- Gratitude to **Lê Phong Hào** and **Lê Hà Nguyên Khánh** for their efforts in
  documenting and understanding the problem.
- A big thank you to **Huỳnh Thanh Duy** for his work on finalizing the source
  code.
- Kudos to everyone involved for their hard work and collaboration.

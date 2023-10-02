# Gas Behavior Analysis Tool

This repository contains a Python program designed to analyze the behavior of various gases using different equations of state. The program allows for calculations of medium complexity and generates corresponding graphs to compare results and analyze gas behavior.

## Introduction

The program utilizes the Van der Waals, Berthelot (real gases), and ideal gas equations of state to perform calculations and generate graphs for different gases. By inputting temperatures, volume limits, and mole numbers, users can visualize and compare the behavior of gases.

## Features

- Calculation of gas behavior using Van der Waals, Berthelot, and ideal gas equations of state.
- Graphical representation of isotherms for the selected gases.
- Comparison of gas behavior for different temperatures and conditions.
- Numerical calculation of critical volume, critical temperature, and critical pressure using the Van der Waals equation.

## Getting Started

1. Clone the repository to your local machine.
2. Run the Python script `Ideal-Gas.py` in your preferred Python environment.

## Usage

1. Upon running the script, follow the prompts to provide input values for gas analysis:
   - Enter the maximum volume (L/mol) for evaluation.
   - Input three temperatures (K) separated by commas for analysis.
   - Choose a gas for evaluation.
   - Enter the number of moles of the selected gas.
2. The program will generate graphs of isotherms for the selected gas and temperatures.
3. Users will be prompted to save the generated graphs if desired.
4. The program will proceed to calculate critical volume, temperature, and pressure using the Van der Waals equation and compare them with theoretical values.

## Supported Gases

The program supports the following gases:
- Air
- NH3
- CO2
- H2
- CH4
- CO
- N2
- O2

## Note

This program is intended for educational purposes and provides insights into gas behavior using different equations of state. The accuracy of results may vary based on the chosen equations and assumptions.

# Pyton Challenge ReadMe
This is a repo with files for the Miami Data Analytics Challenge 3.

## Overview

This project contains two Python scripts: `PyBank` for financial analysis and `PyPoll` for election analysis. Each script processes CSV data, calculates key metrics, and outputs the results to both the terminal and a CSV file.

---

## PyBank (Financial Analysis)

### Functionality:
- Reads monthly financial data from a CSV file.
- Calculates:
  - Total months
  - Total profit/loss
  - Average monthly change
  - Greatest increase and decrease in profits
- Outputs results to both the terminal and `budget_analysis.csv`.

---

## PyPoll (Election Analysis)

### Functionality:
- Reads election data from a CSV file.
- Calculates:
  - Total votes
  - Vote count and percentage for each candidate
  - Winner based on popular vote
- Outputs results to both the terminal and `election_analysis.csv`.

---

## Requirements

- **CSV files** (located in `Resources` directory)

---

## How to Run

1. Place the CSV files in the `Resources` directory.
2. Run the scripts in terminal (mac) or gitbash (windows):
   
   python pybank.py
   python pypoll.py

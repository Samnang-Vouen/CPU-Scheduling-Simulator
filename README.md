# CPU Scheduling Simulator

## Description
This project is a Python-based CPU Scheduling Simulator that implements and compares four scheduling algorithms:
- **First-Come, First-Served (FCFS)**
- **Shortest-Job-First (SJF)**
- **Shortest-Remaining-Time (SRT)**
- **Round Robin (RR)**

The program allows users to enter process details (arrival time and burst time) and select a scheduling algorithm. It then calculates and displays the Gantt Chart, Waiting Times, Turnaround Times, and their respective averages.

## Requirements
- Python 3.x

## How to Run
1. Clone this repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the script using:
   ```sh
   python scheduling_simulator.py
   ```
5. Follow the on-screen instructions to input process details and select a scheduling algorithm.

## Features
- Handles multiple processes with varying arrival and burst times.
- Implements multiple scheduling algorithms for comparison.
- Displays Gantt Chart, Waiting Times, and Turnaround Times.
- Computes and prints average waiting and turnaround times.

## Example
```
CPU Scheduling Algorithms
1. First-Come, First-Served (FCFS)
2. Shortest-Job-First (SJF)
3. Shortest-Remaining-Time (SRT)
4. Round Robin (RR)
5. Exit
Select an option: 1
Enter number of processes (≥ 1): 4
Enter arrival time of P1 (≥ 0): 0
Enter burst time of P1 (> 0): 1
Enter arrival time of P2 (≥ 0): 0
Enter burst time of P2 (> 0): 2
Enter arrival time of P3 (≥ 0): 0
Enter burst time of P3 (> 0): 3
Enter arrival time of P4 (≥ 0): 0
Enter burst time of P4 (> 0): 4

Gantt Chart:
1 (0-1) → 2 (1-3) → 3 (3-6) → 4 (6-10)

Waiting Times: [0, 1, 3, 6]
Turnaround Times: [1, 3, 6, 10]
Average Waiting Time: 2.50
Average Turnaround Time: 5.00
```

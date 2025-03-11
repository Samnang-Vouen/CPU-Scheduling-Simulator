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

Test Cases

Test Case 1 (FCFS)

Input:

Number of Processes: 3
Process 1: Arrival Time = 0, Burst Time = 5
Process 2: Arrival Time = 2, Burst Time = 3
Process 3: Arrival Time = 4, Burst Time = 2

Output:

Gantt Chart: P1 (0-5) → P2 (5-8) → P3 (8-10)
Waiting Times: [0, 3, 4]
Turnaround Times: [5, 6, 6]
Average Waiting Time: 2.33
Average Turnaround Time: 5.67

Test Case 2 (SJF)

Input:

Number of Processes: 3
Process 1: Arrival Time = 0, Burst Time = 5
Process 2: Arrival Time = 1, Burst Time = 2
Process 3: Arrival Time = 2, Burst Time = 3

Output:

Gantt Chart: P1 (0-5) → P2 (5-7) → P3 (7-10)
Waiting Times: [0, 4, 5]
Turnaround Times: [5, 6, 8]
Average Waiting Time: 3.00
Average Turnaround Time: 6.33

Test Case 3 (SRT)

Input:

Number of Processes: 3
Process 1: Arrival Time = 0, Burst Time = 6
Process 2: Arrival Time = 2, Burst Time = 4
Process 3: Arrival Time = 4, Burst Time = 2

Output:

Gantt Chart: P1 (0-2) → P2 (2-4) → P3 (4-6) → P1 (6-10)
Waiting Times: [4, 0, 2]
Turnaround Times: [10, 4, 4]
Average Waiting Time: 2.00
Average Turnaround Time: 6.00

Test Case 4 (Round Robin, Quantum = 2)

Input:

Number of Processes: 3
Process 1: Arrival Time = 0, Burst Time = 5
Process 2: Arrival Time = 1, Burst Time = 3
Process 3: Arrival Time = 2, Burst Time = 6
Time Quantum = 2

Output:

Gantt Chart: P1 (0-2) → P2 (2-4) → P3 (4-6) → P1 (6-8) → P3 (8-10) → P1 (10-11)
Waiting Times: [6, 2, 4]
Turnaround Times: [11, 5, 10]
Average Waiting Time: 4.00
Average Turnaround Time: 8.67


import heapq
from collections import deque

def get_valid_int(prompt, min_value=0):
    """Helper function to get a valid integer input >= min_value"""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Error: Value must be at least {min_value}. Try again.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def fcfs_scheduling(processes):
    """First-Come, First-Served (FCFS) Scheduling Algorithm"""
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time, waiting_time, turnaround_time = 0, [], []
    gantt_chart = []
    
    for pid, arrival, burst in processes:
        if time < arrival:
            time = arrival  # Idle time handling
        waiting_time.append(time - arrival)
        gantt_chart.append((pid, time, time + burst))
        time += burst
        turnaround_time.append(time - arrival)
    
    return gantt_chart, waiting_time, turnaround_time

def sjf_scheduling(processes):
    """Shortest-Job-First (SJF) Scheduling Algorithm"""
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival, then burst time
    min_heap = []
    time, waiting_time, turnaround_time = 0, {}, {}
    gantt_chart, completed = [], set()
    
    while len(completed) < len(processes):
        for p in processes:
            if p[1] <= time and p[0] not in completed:
                heapq.heappush(min_heap, (p[2], p[0], p[1]))  # Push process by burst time
        
        if min_heap:
            burst, pid, arrival = heapq.heappop(min_heap)
            waiting_time[pid] = time - arrival
            gantt_chart.append((pid, time, time + burst))
            time += burst
            turnaround_time[pid] = time - arrival
            completed.add(pid)
        else:
            time += 1  # Increment time if no process is available
    
    return gantt_chart, list(waiting_time.values()), list(turnaround_time.values())

def srt_scheduling(processes):
    """Shortest Remaining Time (SRT) Scheduling Algorithm"""
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    n = len(processes)
    remaining_time = {p[0]: p[2] for p in processes}  # Track remaining burst time
    completion_time = {}
    waiting_time = {}
    turnaround_time = {}
    gantt_chart = []
    time = 0
    completed = 0
    last_pid = None

    while completed < n:
        available_processes = [p for p in processes if p[1] <= time and remaining_time[p[0]] > 0]
        
        if available_processes:
            available_processes.sort(key=lambda x: (remaining_time[x[0]], x[1]))  # Sort by remaining time
            pid, arrival, _ = available_processes[0]

            if last_pid != pid:
                gantt_chart.append((pid, time, time + 1))  # Record execution

            remaining_time[pid] -= 1
            time += 1

            if remaining_time[pid] == 0:
                completed += 1
                completion_time[pid] = time
                turnaround_time[pid] = completion_time[pid] - arrival
                waiting_time[pid] = turnaround_time[pid] - [p[2] for p in processes if p[0] == pid][0]
            
            last_pid = pid  # Update last executed process
        else:
            time += 1  # Idle time if no process is available
    
    return gantt_chart, list(waiting_time.values()), list(turnaround_time.values())

def rr_scheduling(processes, quantum):
    """Round Robin (RR) Scheduling Algorithm"""
    queue = deque(sorted(processes, key=lambda x: x[1]))  # Sort by arrival time
    time, waiting_time, turnaround_time = 0, {}, {}
    gantt_chart, remaining_time = [], {p[0]: p[2] for p in processes}
    
    while queue:
        pid, arrival, burst = queue.popleft()
        start = max(time, arrival)
        execute_time = min(quantum, remaining_time[pid])
        gantt_chart.append((pid, start, start + execute_time))
        time = start + execute_time
        remaining_time[pid] -= execute_time
        
        if remaining_time[pid] == 0:
            turnaround_time[pid] = time - arrival
            waiting_time[pid] = turnaround_time[pid] - burst
        else:
            queue.append((pid, arrival, burst))  # Re-add process to queue if not completed
    
    return gantt_chart, list(waiting_time.values()), list(turnaround_time.values())

def print_results(gantt_chart, waiting_time, turnaround_time):
    """Displays the scheduling results"""
    print("\nGantt Chart:")
    for i, entry in enumerate(gantt_chart):
        if i < len(gantt_chart) - 1:
            print(f"{entry[0]} ({entry[1]}-{entry[2]})", end=" → ")
        else:
            print(f"{entry[0]} ({entry[1]}-{entry[2]})", end=" ")
    print("\n\nWaiting Times:", waiting_time)
    print("Turnaround Times:", turnaround_time)
    print(f"Average Waiting Time: {sum(waiting_time)/len(waiting_time):.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/len(turnaround_time):.2f}")

def main():
    """Main function for user input and execution"""
    while True:
        print("\nCPU Scheduling Algorithms")
        print("1. First-Come, First-Served (FCFS)")
        print("2. Shortest-Job-First (SJF)")
        print("3. Shortest-Remaining-Time (SRT)")
        print("4. Round Robin (RR)")
        print("5. Exit")

        choice = input("Select an option: ")
        valid_choices = {'1', '2', '3', '4', '5'}
        
        while choice not in valid_choices:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")
            choice = input("Select an option: ")
        
        if choice == '5':
            print("Exiting program. Goodbye!")
            break
        
        n = get_valid_int("Enter number of processes (≥ 1): ", min_value=1)
        processes = []

        for i in range(n):
            pid = i + 1
            arrival = get_valid_int(f"Enter arrival time of P{pid} (≥ 0): ", min_value=0)
            burst = get_valid_int(f"Enter burst time of P{pid} (> 0): ", min_value=1)
            processes.append((pid, arrival, burst))
        
        if choice == '1':
            gantt_chart, wt, tat = fcfs_scheduling(processes)
        elif choice == '2':
            gantt_chart, wt, tat = sjf_scheduling(processes)
        elif choice == '3':
            gantt_chart, wt, tat = srt_scheduling(processes)
        elif choice == '4':
            quantum = get_valid_int("Enter time quantum (> 0): ", min_value=1)
            gantt_chart, wt, tat = rr_scheduling(processes, quantum)
        
        print_results(gantt_chart, wt, tat)

if __name__ == "__main__":
    main()

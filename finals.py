import time
# temp
class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def calculate_waiting_time(processes):
    for i in range(len(processes)):
        for j in range(i):
            processes[i].waiting_time += processes[j].burst_time

def calculate_turnaround_time(processes):
    for i in range(len(processes)):
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time

def calculate_average_waiting_time(processes):
    total_wait_time = 0
    for i in range(len(processes)-1):
        total_wait_time += processes[i].turnaround_time
    return total_wait_time / len(processes)


def shortest_job_first(processes):
    # Sort the processes by burst time in ascending order.
    processes.sort(key=lambda process: process.burst_time)

    # Calculate the waiting time and turnaround time for each process.
    calculate_waiting_time(processes)
    calculate_turnaround_time(processes)

    # Print the results.
    print("Process ID | Burst Time | Waiting Time | Turnaround Time")
    print("---------- | ---------- | ------------ | ---------------")
    for process in processes:
        time.sleep(process.waiting_time)
        print(f"{(process.pid).rjust(5):10} | {repr(process.burst_time).rjust(5):10} | {repr(process.waiting_time).rjust(6):12} | {repr(process.turnaround_time).rjust(8):10}")

    #Calculate average wait time
    avg_wait_time = calculate_average_waiting_time(processes)
    print(f'Average waiting time is: {avg_wait_time}')
        

# Create a list of processes.
processes = [
    # Process('P1', 6),
    # Process('P2', 8),
    # Process('P3', 7),
    # Process('P4', 3),
    Process('P1', 5),
    Process('P2', 3),
    Process('P3', 7),
    Process('P4', 2),
]

# Schedule the processes using the SJF algorithm.
shortest_job_first(processes)
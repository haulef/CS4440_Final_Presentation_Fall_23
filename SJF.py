import time
from Process import Process


def calculate_waiting_time(processes):
    for i in range(len(processes)):
        for j in range(i):
            processes[i].waiting_time += processes[j].burst_time

def calculate_turnaround_time(processes):
    for i in range(len(processes)):
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time

"""
def calculate_average_waiting_time(processes):
    total_wait_time = 0
    for i in range(len(processes)-1):
        total_wait_time += processes[i].turnaround_time
    return total_wait_time / len(processes)
"""

class SJF:
    def __init__(self) -> None:
        self.processes = []

    
    def add(self, p_list):
        for p in p_list:
            self.processes.append(p)

    def run(self):
        # Sort the processes by burst time in ascending order.
        self.processes.sort(key=lambda process: process.burst_time)

        # Calculate the waiting time and turnaround time for each process.
        calculate_waiting_time(self.processes)
        calculate_turnaround_time(self.processes)

        # Print the results.
        table_str = ""
        while len(self.processes) > 0:
            process = self.processes.pop(0)
            print(f"{process.id} running for {process.burst_time}")
            time.sleep(process.burst_time)
            table_str += f"{(process.id).rjust(5):10} | {repr(process.burst_time).rjust(5):10} | {repr(process.waiting_time).rjust(6):12} | {repr(process.turnaround_time).rjust(8):10}\n"

        # Print results
        print("Process ID | Burst Time | Waiting Time | Turnaround Time")
        print("---------- | ---------- | ------------ | ---------------")
        print(table_str)

        #Calculate average wait time
        """
        avg_wait_time = calculate_average_waiting_time(self.processes)
        print(f'Average waiting time is: {avg_wait_time} burst_time')
        """
        
"""
# Create a list of processes.
processes = [
    # Process('P1', 6),
    # Process('P2', 8),
    # Process('P3', 7),
    # Process('P4', 3),
    Process('P1', 5, 0),
    Process('P2', 3, 0),
    Process('P3', 7, 0),
    Process('P4', 2, 0),
]

# Schedule the processes using the SJF algorithm.
queue = SJF(processes)
queue.run()
"""
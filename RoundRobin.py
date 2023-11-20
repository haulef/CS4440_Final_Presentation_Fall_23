import time;
from Process import Process

# This class contains the instance variables that nessesary for 
# process scheduling. Priority level is not required by round robin
# but I included it just in case we want to use it.


# This class contains the round robin algorithm and instance variables 
# which contain the processes and the quantum time.
class RoundRobin:
    def __init__(self, qtime) -> None:
        self.processes = []
        self.qtime = qtime

    def add(self, p_list):
        for p in p_list:
            self.processes.append(p)

    # This works by keeping track of the processes that are finished.
    # The algorithm loops through each process and checks if it is finished.
    # If it is finished, it will continue to the next process.
    # if the prosses' burst time is less than or equal to the quantum time, 
    # it will run for the remaining burst time and the process is marked as 
    # done. If it is greater than the quantum time, it will run for the 
    # quantum time seconds.
    def run(self) -> None:
        completed = []
        total_turnaround = 0

        while len(self.processes) > 0:
            process = self.processes.pop(0)
            
            #print(f'Process: {process.id} Switched In!')
            process.waiting_time += total_turnaround - process.turnaround_time
            process.turnaround_time = total_turnaround

            if process.burst_time <= self.qtime:
                print(f'Process: {process.id} is running for {process.burst_time}')
                time.sleep(1*process.burst_time)
                total_turnaround += process.burst_time
                process.burst_time = 0
                print(f'Process: {process.id} is Done!')
                completed.append(process)
            else:
                print(f'Process: {process.id} is running for {self.qtime}')
                time.sleep(1*self.qtime)
                process.burst_time = process.burst_time - self.qtime
                self.processes.append(process)
                total_turnaround += self.qtime
                print(f'Process: {process.id} Switched Out!')

        self._print(completed)
        

    def _print(self, complete):
        print("Process ID | Waiting Time")
        print("---------- | ------------")
        for p in complete:
            print( f"{(p.id).rjust(5):10} | {repr(p.waiting_time).rjust(6):12}" )


def main():
    # processes = [Process('P1', 8, 0), Process('P2', 4, 0),
    #              Process('P3', 2, 0), Process('P4', 9, 0),
    #              Process('P5', 17, 0), Process('P6', 8, 0),
    #              Process('P7', 16, 0)]

    # processes = [Process('P1', 24, 0), Process('P2', 3, 0), 
    #              Process('P3', 3, 0)]

    processes = [Process('P1', 10, 0), Process('P2', 5, 0), 
                 Process('P3', 2, 0), Process('P4', 24, 0),
                 Process('P5', 7, 0), Process('P6', 5, 0)]

    roundRobin = RoundRobin(processes, 5)
    roundRobin.run()





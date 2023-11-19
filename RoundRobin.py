import time;
from Process import Process

# This class contains the instance variables that nessesary for 
# process scheduling. Priority level is not required by round robin
# but I included it just in case we want to use it.


# This class contains the round robin algorithm and instance variables 
# which contain the processes and the quantum time.
class RoundRobin:
    def __init__(self, processes, qtime) -> None:
        self.processes = processes
        self.qtime = qtime

    # This works by keeping track of the processes that are finished.
    # The algorithm loops through each process and checks if it is finished.
    # If it is finished, it will continue to the next process.
    # if the prosses' burst time is less than or equal to the quantum time, 
    # it will run for the remaining burst time and the process is marked as 
    # done. If it is greater than the quantum time, it will run for the 
    # quantum time seconds.
    def run(self) -> None:
        while len(self.processes) > 0:
            process = self.processes.pop(0)
            
            #print(f'Process: {process.name} Switched In!')

            if process.burst_time <= self.qtime:
                print(f'Process: {process.name} is running for {process.burst_time}')
                time.sleep(1*process.burst_time)
                process.burst_time = 0
                print(f'Process: {process.name} is Done!')
            else:
                print(f'Process: {process.name} is running for {self.qtime}')
                time.sleep(1*self.qtime)
                process.burst_time = process.burst_time - self.qtime
                self.processes.append(process)
            
            print(f'Process: {process.name} Switched Out!')
            


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


main()


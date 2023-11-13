import time;

# This class contains the instance variables that nessesary for 
# process scheduling. Priority level is not required by round robin
# but I included it just in case we want to use it.
class MyProcess:
    def __init__(self, name, burstTime, priorityLevel) -> None:
        self.name = name
        self.burstTime = burstTime
        self.priorityLevel = priorityLevel
        self.isDone = False


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
        pDone = 0 # number of processes that are done
        i = 0 # used to index the list of processes
        
        while pDone < len(self.processes):
            process = self.processes[i % len(self.processes)]
            if process.isDone:
                i += 1
                continue
            
            print(f'Process: {process.name} Switched In!')

            if process.burstTime <= self.qtime:
                print(f'Process: {process.name} is running for {process.burstTime}')
                time.sleep(1*process.burstTime)
                process.isDone = True
                pDone += 1
                process.burstTime = 0
                print(f'Process: {process.name} is Done!')
            else:
                print(f'Process: {process.name} is running for {self.qtime}')
                time.sleep(1*self.qtime)
                process.burstTime = process.burstTime - self.qtime
            
            print(f'Process: {process.name} Switched Out!')
            i += 1


def main():
    # processes = [MyProcess('P1', 8, 0), MyProcess('P2', 4, 0),
    #              MyProcess('P3', 2, 0), MyProcess('P4', 9, 0),
    #              MyProcess('P5', 17, 0), MyProcess('P6', 8, 0),
    #              MyProcess('P7', 16, 0)]

    processes = [MyProcess('P1', 24, 0), MyProcess('P2', 3, 0), 
                 MyProcess('P3', 3, 0)]

    roundRobin = RoundRobin(processes, 4)
    roundRobin.run()


main()


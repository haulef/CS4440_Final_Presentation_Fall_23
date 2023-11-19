from tabulate import tabulate


class Process:
    def __init__(self, process_id: int, burst_time: int):
        self.process_id = process_id
        self.burst_time = burst_time

    def __str__(self):
        return f"P{self.process_id}\nburst_time: {self.burst_time}"


class Queue:
    def __init__(self):
        self.processes = []

    # adds element to the list
    def add(self, process: Process):
        self.processes.append(process)

    # returns queue list
    def getQueueList(self) -> list:
        return self.processes

    # returns element of the queue using index
    def getProcess(self, index: int) -> Process:
        return self.processes[index]

    def __str__(self) -> str:
        if not self.processes:
            return "No Processes on queue"

        return f"{len(self.processes)} process on queue..."


def run(processes):
    # intial header for table
    # each tuple represents a row
    data = [("Process", "Burst Time (sec)", "Waiting Time", "Turnaround Time")]
    waiting_time = 0
    turnaround_time = 0

    # iterate thru list of process
    for process in processes:
        turnaround_time += waiting_time + process.burst_time
        # add current process, burst_time, waiting_time and turnaround_time
        data.append(
            (process.process_id, process.burst_time, waiting_time, turnaround_time)
        )

        # add current wait_time to calculate total
        # Previous: P1 waiting time -> 25 <- P2 start time
        waiting_time += process.burst_time

    # caculate average_waiting_time, average_turnaround_time using sum of waiting_time, turnaround_time
    average_waiting_time = waiting_time / len(processes)
    average_turnaround_time = turnaround_time / len(processes)

    # using tabulate library and list of all the process_id, burst_time, wait time and turnaround time
    print(tabulate(data, tablefmt="simple"))

    # print average and total time
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")
    print(f"Total Time: {waiting_time}")


if __name__ == "__main__":
    process_queue = Queue()
    process_queue.add(Process(1, 25))
    process_queue.add(Process(2, 10))
    process_queue.add(Process(3, 15))

    run(process_queue.getQueueList())

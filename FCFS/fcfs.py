from tabulate import tabulate
import time


class Process:
    def __init__(self, process_id: str, burst_time: int):
        self.process_id = process_id
        self.burst_time = burst_time


class fcfs_queue:
    def __init__(self):
        self.queue = []

    # adds element to the list
    def add(self, process: Process):
        self.queue.append(process)

    # returns queue list
    def getQueueList(self) -> list:
        return self.queue

    # will run the cpu scheduling
    def run(self):
        # Access element of queue list using for loop
        for process in self.queue:
            # print out the process_id and burst_time
            print(
                f"Process: {process.process_id} is running for {process.burst_time} seconds"
            )
            # wait time will correspond to process burst_time in seconds
            time.sleep(process.burst_time)
            print(f"{process.process_id} is done!")

        print("All process are complete")
        self.show_table()

    def show_table(self):
        if not self.queue:
            return "No Processes on queue"
        # intial header for table
        # each tuple represents a row
        data = [("Process", "Burst Time (sec)", "Waiting Time (sec)")]
        waiting_time = 0

        # iterate thru list of process
        for process in self.queue:
            # add current process, burst_time, waiting_time and turnaround_time
            data.append((process.process_id, process.burst_time, waiting_time))

            # add current wait_time to calculate total
            # Previous: P1 waiting time -> 25 <- P2 start time
            waiting_time += process.burst_time

        # caculate average_waiting_time, average_turnaround_time using sum of waiting_time, turnaround_time
        average_waiting_time = waiting_time / len(self.getQueueList())

        # using tabulate library and list of all the process_id, burst_time, wait time and turnaround time
        print(tabulate(data, tablefmt="simple"))

        # print average and total time
        print(f"\nAverage Waiting Time: {average_waiting_time} seconds")
        print(f"Total Time: {waiting_time} seconds")


""""
if __name__ == "__main__":
    process_queue = fcfs_queue()
    process_queue.add(Process("P1", 5))
    process_queue.add(Process("P2", 6))
    process_queue.add(Process("P3", 8))

    process_queue.run()
"""

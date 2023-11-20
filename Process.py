class Process:
    def __init__(self, id, burst_time, priority) -> None:
        self.id = id
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
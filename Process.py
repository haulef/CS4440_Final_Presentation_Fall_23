class Process:
    def __init__(self, name, burst_time, priority) -> None:
        self.name = name
        self.burst_time = burst_time
        self.priority = priority
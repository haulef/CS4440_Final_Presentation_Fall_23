import random
from RoundRobin import RoundRobin

class Process:
    def __init__(self, id, burstTime, priority) -> None:
        self.id = id
        self.burstTime = burstTime
        self.priority = priority


def input_interface(queues):
    index = 0
    user_in = ""
    while user_in != "exit":
        user_in = input("Enter number of random generated processes, 'exit' to leave: ")

        #switching queues
        if user_in == "fcfs":
            index = 0
        elif user_in == "sjf":
            index = 1
        elif user_in == "rr":
            index = 2
        #generate a random set of processes
        else:
            p_list = []
            for i in range(0, int(user_in) ):
                p_list.push( Process("P"+str(i), random.randint(1, 11), random.randint(1, 6)) )
            queues[index].add(p_list)
            queues[index].run()
        


def main():
    
    input_interface([
        RoundRobin()
    ])
    pass
main()
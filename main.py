import random
from RoundRobin import RoundRobin
from SJF import SJF
from fcfs import fcfs_queue
from Process import Process


def input_interface(queues):
    index = 0
    user_in = ""

    print("type the following to switch queue type")
    print("\'fcfs\' : First Come First Serve")
    print("\'sjf\' : Shortest Job First")
    print("\'rr\' : Round Robin")
    while user_in != "exit":
        user_in = input("Enter the number of random generated processes, 'exit' to leave: ")

        #switching queues
        if user_in == "fcfs":
            index = 0
        elif user_in == "sjf":
            index = 1
        elif user_in == "rr":
            index = 2
        #generate a random set of processes
        elif user_in.isnumeric():
            p_list = []
            for i in range(0, int(user_in) ):
                p_list.append( Process("P"+str(i), random.randint(1, 11), random.randint(1, 6)) )
            # print set of processes
            print("===== Processes =====")
            print("Process ID | Burst Time | ")
            print("---------- | ---------- | ")
            for p in p_list:
                print(f"{(p.id).rjust(5):10} | {repr(p.burst_time).rjust(5):10} | ")
            queues[index].add(p_list)
            queues[index].run()
        


def main():
    input_interface([
        fcfs_queue(),
        SJF(),
        RoundRobin(5)
    ])
    
main()
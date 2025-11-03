# Task Scheduling using Shortest Job First (SJF)

# List of tasks and their burst times
tasks = {
    'T1': 5,
    'T2': 3,
    'T3': 8,
    'T4': 6
}

# Sort tasks by burst time (ascending order)
sorted_tasks = sorted(tasks.items(), key=lambda x: x[1])

# Variables to calculate waiting and turnaround times
waiting_time = 0
turnaround_time = 0
total_waiting = 0
total_turnaround = 0

print("Task\tBurst Time\tWaiting Time\tTurnaround Time")

for task, burst in sorted_tasks:
    turnaround_time = waiting_time + burst
    print(f"{task}\t{burst}\t\t{waiting_time}\t\t{turnaround_time}")
    total_waiting += waiting_time
    total_turnaround += turnaround_time
    waiting_time += burst

# Average waiting and turnaround time
n = len(tasks)
print("\nAverage Waiting Time:", total_waiting / n)
print("Average Turnaround Time:", total_turnaround / n)

# Given a list of processes that can run in parallel.
# Each process is represented by a triplet [id, startTime, endTime].

# A process's exclusive time is the time spent to execute this process.
# Note that this does not include the time while multiple processes run simultaneously.
# Return the exclusive time of each process in the form [id, duration].

# Example:
#
#   Input:
#       [[1, 150, 300], [2, 100, 200], [3, 300, 350]]
#   Output:
#       [[1, 100], [2, 50], [3, 50]]
#
#
#   Input:
#       [[1, 150, 400], [2, 100, 200], [3, 300, 350]]
#   Output:
#       [[1, 150], [2, 50]]


from collections import defaultdict
from functools import cmp_to_key


def exclusive_time(procs):
    """
    This problem could be solved using sweep line algorithm.
    Another way is priority queue.
    """

    # split time series of processes into separate sorted events:
    # (id, kind, time)
    id, kind, time = 0, 1, 2
    events = []
    for proc in procs:
        events.append((proc[0], "start", proc[1]))
        events.append((proc[0], "end", proc[2]))

    # order events based on time and event kind,
    # if time is same 'end' should come before 'start'
    def comparator(a, b):
        # if same time
        if a[time] == b[time]:
            return 1 if a[kind] == "start" else -1
        return -1 if a[time] < b[time] else 1

    events = sorted(events, key=cmp_to_key(comparator))

    results = defaultdict(int)
    active_procs = set()
    last_time = events[0][time]  # start time of the entire series

    for event in events:

        if event[kind] == "start":

            # the process is not single any more
            # we need to update it's singleton running time
            if len(active_procs) == 1:
                single = list(active_procs)[0]
                results[single] += event[time] - last_time

            active_procs.add(event[id])

        else:

            # the active process has finished
            if len(active_procs) == 1:
                single = list(active_procs)[0]
                results[single] += event[time] - last_time

            active_procs.remove(event[id])

        last_time = event[time]

    # ignoring zero time processes
    return sorted([(k, v) for k, v in results.items() if v != 0])

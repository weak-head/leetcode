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


def exclusive_time(procs):
    """
    Sweep line.

    Time: O(n * log n)
    Space: O(n)
        n - number of elements in the list
    """
    events = []
    for proc, start, end in procs:
        events.append((start, 1, proc))
        events.append((end, 0, proc))
    events.sort()  # end goes before start

    active_time = defaultdict(int)
    active = set()
    last_time = None
    for time, kind, proc in events:
        if kind == 0:  # end
            if len(active) == 1:
                active_time[proc] += time - last_time
            active.remove(proc)
        else:  # start
            if len(active) == 1:
                p = list(active)[0]
                active_time[p] += time - last_time
            active.add(proc)
        last_time = time

    return sorted([(k, v) for k, v in active_time.items() if v != 0])

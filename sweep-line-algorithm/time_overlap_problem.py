# ---
# title: Time Overlap Problem
# tags: [CodingChallenges, Python, TwoPointerAlgorithm, SweepLineAlgorithm]
# created: '2023-03-10'
# ---

# # Time Overlap Problem

# This document contains the solution for a problem that finds the maximum overlap in a set of time intervals using two pointer algorithm and sweep line algorithm.

# ## Problem Description
# Given a list of timelines where each timeline consists of a start time and an end time, find out the maximum overlap among these timelines.

# ## Solution

# ```python
from datetime import datetime, timedelta

def count_max_overlap(timelines):
    breakpoint()
    sort_by_start_time(timelines)
    current_end_time = timelines[0][0].timestamp() + 1
    max_overlap = 0
    current_overlap = 0
    
    for timeline in timelines:
        if timeline[0].timestamp() > current_end_time:
            current_overlap = 1
            current_end_time = timeline[0].timestamp() + 1
        else:
            current_overlap += 1
        
        max_overlap = max(max_overlap, current_overlap)
        # current_end_time = max(current_end_time, timeline[1].timestamp())
    
    return max_overlap

def sort_by_start_time(timeline_dt):
    for i in range(len(timeline_dt)):
        datetime_dt = datetime.strptime(' '.join(timeline_dt[i].split()[0:2]), '%Y-%m-%d %H:%M:%S.%f')
        time_diff = timedelta(seconds=-float(timeline_dt[i].split()[-1][:-1])+0.001)
        result_dt = datetime_dt + time_diff
        # result_str = result_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        timeline_dt[i] = [result_dt, datetime_dt]
    timeline_dt.sort(key=lambda x:x[0])
    return timeline_dt

timeline_data = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(count_max_overlap(timeline_data))


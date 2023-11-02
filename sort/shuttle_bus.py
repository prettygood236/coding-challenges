# ---
# title: Shuttle Bus
# tags: [CodingChallenges, Python, Sorting]
# created: '2023-01-22'
# ---

# ## Problem Description

# A shuttle bus operates n times from 09:00. It departs every t minutes and can carry up to m people. Given a list of crew arrival times in `timetable`, determine the latest time you should arrive to catch the shuttle bus. If there is not enough room on the bus for all the crew, you should arrive earlier to ensure you get a seat.

# ## Constraints

# - The shuttle bus operates n times (1 ≤ n ≤ 10).
# - The bus departs every t minutes (1 ≤ t ≤ 60).
# - The bus can carry up to m people (1 ≤ m ≤ 45).
# - Each time in `timetable` is given in the format "HH:MM".
# - `timetable` contains at least 1 and no more than 2,000 times.

# ## Solution

# The problem can be solved by sorting the timetable in descending order and then filling the bus for each departure time. If the bus is full or there are no more crew, the bus departs. If there is room on the last bus, you should arrive at the last departure time. If the last bus is full, you should arrive one minute before the last crew member that got a seat.

# ```python
def solution(n,t,m,timetable):
  answer = ''
  for i in range(len(timetable)):
    timetable[i] = int(timetable[i][:2])*60+int(timetable[i][3:5])
  timetable.sort(reverse=True)
  l = [[] for _ in range(n)]
  time = 0
  for i in range(n):
    time = 9*60 + i*t
    while True:
      if not timetable:
        break
      if len(l[i]) >= m or timetable[-1] > time:
        break
      if timetable[-1] <= time:
        l[i].append(timetable.pop())   

  if len(l[-1]) < m:
    answer = str(time//60).zfill(2) + ':' + str(time%60).zfill(2)
  else:
    time = max(l[-1]) - 1
    answer = str(time//60).zfill(2) + ':' + str(time%60).zfill(2)

  return answer

# n,t,m = map(int,'1	1	5'.split())
# timetable = ["08:00", "08:01", "08:02", "08:03"]

# n,t,m = map(int,'2	10	2'.split())
# timetable = ["09:10", "09:09", "08:00"]	

# n,t,m = map(int,'2	1	2'.split())
# timetable = ["09:00", "09:00", "09:00", "09:00"]	

# n,t,m = map(int,'1	1	5'.split())
# timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]	

# n,t,m = map(int,'1	1	1'.split())
# timetable = ["23:59"]	

n,t,m = map(int,'10	60	45'.split())
timetable = 	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

print(solution(n,t,m,timetable))
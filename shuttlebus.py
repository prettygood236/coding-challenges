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
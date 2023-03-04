from datetime import datetime, timedelta

a = "2016-09-15 01:00:07.000 2s"


datetime_dt = datetime.strptime(' '.join(a.split()[0:2]), '%Y-%m-%d %H:%M:%S.%f')
time_diff = timedelta(seconds=-float(a.split()[-1][:-1])+0.001)
result_dt = datetime_dt + time_diff
result_str = result_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
a = result_str

breakpoint()
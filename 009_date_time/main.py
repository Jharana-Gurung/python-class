import datetime

# supports days, hours, minutes, seconds, micro seconds

jharana_bod_with_time = datetime.datetime(2002, 10, 19, 4, 0, 0)
print(jharana_bod_with_time)

ten_years_ago = jharana_bod_with_time - datetime.timedelta(hours=5, minutes=60, seconds=90, microseconds=80)
print(ten_years_ago)

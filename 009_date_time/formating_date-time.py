import datetime

jharana_bod_with_time = datetime.datetime(2002, 10, 19)


formating = jharana_bod_with_time.strftime("%y, %B, %d")
print(formating)


user_input_data = "12 December 2022"
date_object = datetime.datetime.strptime(user_input_data, "%d, %B, %Y")
print(date_object)

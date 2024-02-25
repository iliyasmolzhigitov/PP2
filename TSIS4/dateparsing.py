from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Five days ago:", five_days_ago)




from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)




from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current datetime:", current_datetime)
print("Datetime without microseconds:", current_datetime_without_microseconds)




from datetime import datetime

date1 = datetime(2024, 2, 20, 12, 0, 0)
date2 = datetime(2024, 2, 25, 12, 0, 0)

difference_in_seconds = abs((date2 - date1).total_seconds())

print("Difference between the two dates in seconds:", difference_in_seconds)

from datetime import datetime, timedelta

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
today = current_date
tomorrow = current_date + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

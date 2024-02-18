from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Date five days ago:", new_date.strftime("%Y-%m-%d"))

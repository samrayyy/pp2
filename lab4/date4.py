from datetime import datetime, timedelta

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
today = current_date

difference = yesterday - today

difference_in_seconds = difference.total_seconds()

print(difference_in_seconds)

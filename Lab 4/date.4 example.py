from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

difference_in_seconds = (tomorrow - yesterday).total_seconds()

print(difference_in_seconds)




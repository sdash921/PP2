from datetime import datetime, timedelta

now = datetime.now()
print(now)

target_date = datetime(2026, 12, 25, 10, 0, 0)
print(now.strftime('%A, %B %d, %Y'))

diff = target_date - now
print(diff.days)

future_date = now + timedelta(weeks=1)
print(future_date)
from datetime import datetime
target = datetime(2027,1,1)
now = datetime.now()
diff = target - now
print(diff.days)
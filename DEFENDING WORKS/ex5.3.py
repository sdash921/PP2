from datetime import datetime
a = datetime.now()
print("Today is",a.strftime("%A"), a.strftime("%B"), a.strftime("%d"))
from datetime import datetime
now = datetime.now()
print("Hi today's day is", now.strftime("%A"), "and the full date is", now.strftime("%D"))

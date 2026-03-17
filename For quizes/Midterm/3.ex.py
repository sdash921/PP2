import re
from datetime import datetime
logs = """
[2026-02-01] User_Ivan_login
[2026-02-05] System_error_404
[2026-02-15] User_Anna_logout
[2026-03-01] Update_success
"""
pattern = re.findall("(\d{4}-\d{2}-\d{2})",logs)
print(pattern[1])
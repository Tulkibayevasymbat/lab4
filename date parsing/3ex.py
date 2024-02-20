#Write a Python program to drop microseconds from datetime

from datetime import datetime

# с микросекундой
current_datetime = datetime.now()

# без микросекунды
without_microsec = current_datetime.replace(microsecond=0)

print("қазіргі дата мен уақыт микросекундсыз:", without_microsec)

#output: қазіргі дата мен уақыт микросекундсыз: 2024-02-18 18:03:47
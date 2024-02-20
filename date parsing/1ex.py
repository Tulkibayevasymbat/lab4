#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta
current_date_time = datetime.now()

result_date = current_date_time - timedelta(days=5)

print(f"қазіргі дата: {current_date_time}")
print(f"результат: {result_date}")

#output:
#қазіргі дата: 2024-02-18
#результат: 2024-02-13
#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta
# бүгінгі дата
current_date = datetime.now()

# кешегі дата
yesterday = current_date - timedelta(days=1)

# ертеңгі дата
tomorrow = current_date + timedelta(days=1)

# результаты
print("кеше:", yesterday.date())
print("бүгін:", current_date.date())
print("ертең:", tomorrow.date())

#output:
#кеше: 2024-02-17
#бүгін: 2024-02-18
#ертең: 2024-02-19

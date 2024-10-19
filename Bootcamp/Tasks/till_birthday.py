from datetime import datetime

print("Введите день рождения в формате 'гггг-мм-дд': ")
year, month, day = input().split("-")
year, month, day = int(year), int(month), int(day)

# Selecting the date from which we will count the days till the birthday
today = datetime.now()
# today = datetime(int(2025),int(1), int(15))

# Finding out whether the birthday is this year or next one
if month < today.month or month == today.month and day < today.day:
    year = today.year + 1
else:
    year = today.year

birthday = datetime(year, month, day)

days_until_birthday = (birthday - today).days
print(f"До дня рождения осталось {days_until_birthday} дней.")

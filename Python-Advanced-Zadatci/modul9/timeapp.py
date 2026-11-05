
import datetime

now = datetime.datetime.now()

print("--- Individual components ---")
print(f"Year:             {now.year}")
print(f"Month:            {now.month}")
print(f"Day:              {now.day}")
print(f"Hour:             {now.hour}")
print(f"Minute:           {now.minute}")
print(f"Second:           {now.second}")
print(f"Microsecond:      {now.microsecond}")



period = datetime.timedelta(days=100)
future = now + period
past = now - period

date_format = "%d.%m.%Y at %H:%M:%S"

print("\n--- Shifting time ---")
print(f"Currently:                 {now.strftime(date_format)}")
print(f"100 days in the future:    {future.strftime(date_format)}")
print(f"100 days in the past:      {past.strftime(date_format)}")



specific_time = datetime.datetime(year=2024, month=9, day=1, hour=8, minute=0, second=0)

with open("formatted_dates.txt", "w", encoding="utf-8") as file:
    file.write(f"Created date & time: {specific_time}\n")
    file.write(f"Formatted view: {specific_time.strftime('%d.%m.%Y. at %H:%M:%S')}\n")

print("\nData about specific time successfully saved in 'formatted_dates.txt.")
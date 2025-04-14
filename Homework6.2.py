seconds_input = int(input("Please input number of seconds (from 0 to 8640000): "))

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

days, remaining_seconds = divmod(seconds_input, SECONDS_IN_DAY)
hours, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_HOUR)
minutes, seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)

if days == 1:
    day_word = "day"
elif 2 <= days % 10 <= 4 and not 12 <= days % 100 <= 14:
    day_word = "days"
else:
    day_word = "dayss"

time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(f"{days} {day_word}, {time_str}")
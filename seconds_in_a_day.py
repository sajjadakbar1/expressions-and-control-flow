# current_hours = 14;
# current_minutes = 34;
# current_seconds = 42;
# 14:34:42
day_in_seconds = 24 * 60 * 60
print("There are "+str(day_in_seconds)+" seconds in a day.")
# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables above

remaining_hours = 23 - 14
remaining_hours_in_sec = remaining_hours * 60
print("Remaining hours 23 - 14 = "+str(remaining_hours)+" hours.")
print("Remaining hours in seconds "+str(remaining_hours_in_sec)+" seconds.")
# current_minutes_in_seconds = 34 * 60
# total_hours_and_mins_in_seconds = current_hours_in_seconds + current_minutes_in_seconds
# print(total_hours_and_mins_in_seconds + current_seconds)
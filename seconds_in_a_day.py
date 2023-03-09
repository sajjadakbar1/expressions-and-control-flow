current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables above

current_hours_in_seconds = 14 * 60 * 60
current_minutes_in_seconds = 34 * 60
total_hours_and_mins_in_seconds = current_hours_in_seconds + current_minutes_in_seconds
print(total_hours_and_mins_in_seconds + current_seconds)
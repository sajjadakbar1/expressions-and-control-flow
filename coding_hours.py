# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

daily_hours = 6
semester_workingDays = 17 * 5
semester_totalDays = 17 * 7

#print("semester_totalDays "+semester_totalDays)

hours = str(daily_hours * semester_workingDays)
print("An Attendee is spending "+hours+" hours in a semester.")

percentage_coding_hours = str(52 / 168 * 100)
print(percentage_coding_hours+" %")


# hours_per_week = 6 * 5
# print("Coding hours per week: " + str(hours_per_week),"weeks\n")    # casting

# total_hours = 52 * 17
# print("Total hours: " + str(total_hours),"hours\n")

# coding_hours = 30 * 17
# print("Total coding hours: " + str(coding_hours),"hours\n")

# percentage_cal = coding_hours/total_hours

# print("Percentage calculation: " + str(percentage_cal),"\n")

# print("Working code hours in percentage: " + str(percentage_cal * 100) + "%" , "\n")

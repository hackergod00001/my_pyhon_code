# Write a program to display
# the calendar of any given year.
import calendar  # importing a built in module called calendar
year = int(input("Enter Year: "))
print("\nCalendar for year %d is:" % year)
print(calendar.calendar(year, 2, 1, 6))

# NOTE: calendar(year, w, l, c):-
# This function displays the year,
# width of characters,
# no. of lines per week and column separations.

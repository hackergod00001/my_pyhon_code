#!/bin/python3

months = open("month.txt")
print(months)
print(months.mode)
print(months.readable())
print(months.read())
print(months.seek(0))
print(months.readline()) #reads one line
print(months.readline()) #reads next line
print(months.seek(0))
print(months.readlines()) #prints an array
print(months.readlines()) #prints an empty array because we already read it
months.seek(0)
print(months.seek(0))
for month in months:
	print(month)

print(months.seek(0))
for month in months:
	print(month.strip())
	
	
months.close()

# write a file
days = open("days.txt", "w")
print(days)
print(days.mode)
days.write("Monday")  #- appends

# write a file
days = open("days.txt", "a")
print(days)
print(days.mode)
days.write("\nTuesday")  #- appends
	
days.close()

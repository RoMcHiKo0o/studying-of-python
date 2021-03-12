import sys

year = int(sys.argv[1])

print(year % 400 == 0 or (year % 100 != 0 and year % 4 == 0))	

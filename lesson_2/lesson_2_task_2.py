is_year_leap = input("Какой сейчас год?")
year = int(is_year_leap)
if (year % 4 == 0):
   print("год ", is_year_leap, ":", True)
else:
   print("год ", is_year_leap, ":", False)

start_year = 1900
end_year = 2100
moving_years = []
non_moving_years = []
for year in range(start_year, end_year + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        moving_years.append(year)
    else:
        non_moving_years.append(year)
choice = input("Kuriuos metus nori kad rodytu? Enter 'keliamieji' or 'nekeliamieji': ")
if choice == "keliamieji":
    print("keliamieji metai:")
    for year in moving_years:
        print(year)
elif choice == "nekeliamieji":
    print("nekeliamieji:")
    for year in non_moving_years:
        print(year)
else:
    print("Blogas pasirinkimas. Iveskite 'keliamieji' or 'nekeliamieji'.")
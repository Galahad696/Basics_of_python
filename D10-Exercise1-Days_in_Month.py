def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return Fals


def days_in_month(chosen_year, chosen_month):
    """
    Take the year and month's number and return the number of days of that month.
    """
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap(chosen_year)
    if is_leap(chosen_year):
        month_days[2] = 29
    return month_days[chosen_month]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


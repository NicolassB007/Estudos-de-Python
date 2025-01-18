def is_leap_year(year):
    if year % 4 == 0:
        return f"{year} É BISSEXTO"
    return f"{year} NÃO É BISSEXTO"

year = input("Informe um ano: ")

valid_year = None
int_year = 0

try:
    int_year = int(year)
    valid_year = True
except:
    valid_year = None

leap_year = is_leap_year(int_year)
if valid_year is True:
    print(leap_year)
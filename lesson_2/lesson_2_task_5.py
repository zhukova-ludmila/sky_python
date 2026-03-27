month_number = int(input("Введите число от 1 до 12: "))
def month_to_season(month_number):
    if month_number in [1, 2, 12]:
        print("Зима")
    if month_number in [3, 4, 5]:
        print("Весна")
    if month_number in [6, 7, 8]:
        print("Лето")
    if month_number in [9, 10, 11]:
        print("Осень")
month_to_season(month_number)

from adress import Adress
from mailing import Mailing

to_adress = Adress(123456, "Moscow", "Dostoevskogo", 15, 4)
from_adress = Adress(234567, "Novosibirsk", "Chehova", 50, 17)
cost = 1000
track = "12345678"
mailing = Mailing (Adress, Adress, 1000, 12345678)
print("Отправление", track, "из", from_adress, "в", to_adress, ". Стоимость", cost, "рублей.")

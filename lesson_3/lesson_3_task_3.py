from mailing import Mailing
from adress import Adress

to_adress = Adress(123456, "Moscow", "Pushkina", 24, 17)
from_adress = Adress(654321, "Novosibirsk", "Chehova", 36, 3)
cost = 1000
track = 12345678
mailing = Mailing(to_adress, from_adress, cost, track)
print(
    "Отправление",
    track,
    "из",
    from_adress,
    "в",
    to_adress,
    ". Стоимость",
    cost,
    "рублей.",
)

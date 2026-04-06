from mailing import Mailing
from address import Address

to_address = Address(123456, "Moscow", "Pushkina", 24, 17)
from_address = Address(654321, "Novosibirsk", "Chehova", 36, 3)
cost = 1000
track = 12345678
mailing = Mailing(to_address, from_address, cost, track)
print(
    "Отправление",
    track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    cost,
    "рублей.",
)

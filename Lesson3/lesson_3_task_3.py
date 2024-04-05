from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 143541, "г. Павловское", "ул. Центральная", 23, 1
from_address = 143500, "г. Истра", "ул. Ленина", 43, 1

sending = Mailing
sending(to_address, from_address, 500, 9876543210)

print(
    "Отправление", sending.track,
    "из", from_address,
    "в", to_address,
    ". Стоимость", sending.cost, "рублей.",
)
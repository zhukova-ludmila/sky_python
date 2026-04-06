from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S", "+79520000000"),
    Smartphone("Samsung", "Galaxy S25 Ultra", "+79210100101"),
    Smartphone("Honor", "200", "+79500210131"),
    Smartphone("Honor", "200 Pro", "+79110010101"),
    Smartphone("Realme", "C61", "+79520030101"),
]

for smartfon in catalog:
    print(f"{smartfon.mark} - {smartfon.model}. {smartfon.number}")

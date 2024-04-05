seznam = [42, "Hello", 3.14, True, "OpenAI", [1, 2, 3], {"key": "value"}, None, 7, "Python"]

prvni_hodnota = seznam[0]
stredni_hodnota = seznam[len(seznam)//2]
posledni_hodnota = seznam[-1]

print("První hodnota:", prvni_hodnota)
print("Střední hodnota:", stredni_hodnota)
print("Poslední hodnota:", posledni_hodnota)

soucet = sum(seznam)
print("Součet prvků seznamu:", soucet)

nejmensi_hodnota = min(seznam)
nejvetsi_hodnota = max(seznam)
print("Nejmenší hodnota v seznamu:", nejmensi_hodnota)
print("Největší hodnota v seznamu:", nejvetsi_hodnota)

unikatni_seznam = list(set(seznam))
print("Seznam bez duplicitních hodnot:", unikatni_seznam)

seznam[0] = "Nová_hodnota_1"
seznam[len(seznam)//2] = "Nová_hodnota_2"
seznam[-1] = "Nová_hodnota_3"

print("Upravený seznam po výměně hodnot:", seznam)

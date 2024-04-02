# 1. Vytvořte seznam s různými druhy dat.
seznam = [42, "Hello", 3.14, True, "OpenAI", [1, 2, 3], {"key": "value"}, None, 7, "Python"]

# 2. Pomocí indexu vypište první, střední a poslední zadané hodnoty.
prvni_hodnota = seznam[0]
stredni_hodnota = seznam[len(seznam)//2]
posledni_hodnota = seznam[-1]

print("První hodnota:", prvni_hodnota)
print("Střední hodnota:", stredni_hodnota)
print("Poslední hodnota:", posledni_hodnota)

# 3. Sečtěte prvky seznamu a vypište jejich výsledek.
soucet = sum(seznam)
print("Součet prvků seznamu:", soucet)

# 4. Vypište nejmenší a největší hodnotu v seznamu.
nejmensi_hodnota = min(seznam)
nejvetsi_hodnota = max(seznam)
print("Nejmenší hodnota v seznamu:", nejmensi_hodnota)
print("Největší hodnota v seznamu:", nejvetsi_hodnota)

# 5. Pokud se v seznamu objevují stejná data, odstraňte je a znovu vypište.
unikatni_seznam = list(set(seznam))
print("Seznam bez duplicitních hodnot:", unikatni_seznam)

# 6. Vyměňte 3 hodnoty seznamu za libovolné hodnoty. (První, střední a poslední)
seznam[0] = "Nová_hodnota_1"
seznam[len(seznam)//2] = "Nová_hodnota_2"
seznam[-1] = "Nová_hodnota_3"

print("Upravený seznam po výměně hodnot:", seznam)

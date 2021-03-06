# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# Можно приобрести книги Пушкина и Тютчева

magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
domknig = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
bykmarket = {"Пушкин", "Достоевский", "Маяковский"}
galerea = {"Чехов", "Тютчев", "Пушкин"}
shops_list = []

print("Магистр -", ', '.join(magistr))
print("ДомКниг -", ', '.join(domknig))
print("БукМаркет -", ', '.join(bykmarket))
print("Галерея -", ', '.join(galerea))

if "Пушкин" and "Тютчев" in magistr:
    shops_list.append("Магистр")

if "Пушкин" and "Тютчев" in domknig:
    shops_list.append("ДомКниги")

if "Пушкин" and "Тютчев" in bykmarket:
    shops_list.append("БукМаркет")

if "Пушкин" and "Тютчев" in galerea:
    shops_list.append("Галерея")

print("\nМагазины с книгами Пушкина и Тютчева:", ', '.join(shops_list))
